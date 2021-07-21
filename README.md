# playtube

Personal Music Server that plays music from youtube

Note: No longer supported.

## Goals

- Run on a Raspberry Pi (raspian jessy)
- Download music using youtube-dl
- Cache Music (don't redownload)
- Present a web interface to queue and skip songs
- (Optional) Video support using omxplayer
    - This will run the youtube video on the raspberry pi remotely
- Maintain database of all downloaded tracks
- Search support over youtube and local files


## Tech

- `youtube-dl`
- `flask`
- `tinydb`

## TODO

- Add search inside tags
- Add playlist download and play support

## License

Licensed under [MIT](https://nemo.mit-license.org).
