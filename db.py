from tinydb import TinyDB, Query
import re

class DB:
    def __init__(self,db_path):
        self.db = TinyDB(db_path)

    def add(self, data):
        # Only add it if you can't find it
        Track = Query()
        if not self.db.get(Track.display_id == data['display_id']):
            return self.db.insert(data)

    def searchById(self, video_id):
        Track = Query()
        return self.db.get(Track.display_id == video_id)

    def search(self, text):
        pattern = re.compile(text,re.IGNORECASE)
        def test(txt):
            return pattern.search(txt)

        Track = Query()
        q = Track.title.test(test) | Track.description.test(test)
        return self.db.search(q)

    def all(self):
        return self.db.all()

if __name__ == "__main__":
    db = DB('/tmp/test.json')
    db.add({'display_id':'123', 'tags':['a', 'abc', 'xyz'], 'title': 'num'})
    db.add({'display_id':'dumbledore', 'tags':['harry'], 'title': 'Hello HP'})

    assert not db.searchById('123') == None
    assert db.searchById('456') == None

    assert len(db.search('minerva')) == 0
    assert len(db.search('HP')) == 1
