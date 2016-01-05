import youtube_dl
import re
from os import stat
class DL:
    def __init__(self, url):
        self.url = url
        self.ydl = youtube_dl.YoutubeDL({
            'format': '140',
            'outtmpl': 'Music/%(id)s.m4a',
            'addmetadata': True,
            'extractaudio': True,
            'audioformat': 'm4a',
            'quiet': True,
            # Don't redownload tracks
            'nooverwrites': True
        })

    def already_downloaded(self):
        try:
            p = re.compile("^.*(youtu\.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]*).*")
            video_id = p.match(self.url).group(2)
            filepath = 'Music/{video_id}.m4a'.format(video_id=video_id)
            stat(filepath)
            return True
        except OSError:
            return False

    def download(self):
        if self.already_downloaded():
            result = self.ydl.extract_info(self.url, download=False)
            result['existing'] = True
        else:
            result = self.ydl.extract_info(self.url, download=True)
            result['existing'] = False
        
        # Now we filter out the correct format data
        audio = [x for x in result['formats'] if x['ext'] == 'm4a']

        # Drop the extra formats
        result.pop('formats', None)
        result['format'] = audio[0]

        return result

if __name__ == "__main__":
    DL('https://www.youtube.com/watch?v=akhmS1D2Ce4').download()
