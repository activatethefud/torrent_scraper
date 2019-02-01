### Torrent scraper

![Screenshot](https://i.imgur.com/IHm1fCW.png)

This is a simple torrent scraper that works in the terminal. (Currently scrapes 1337x.to)

## Dependencies:
* transmission-daemon
* transmission-remote-cli
* python3 Beautiful Soup 4

```
sudo apt-get install python3-bs4 transmission-daemon transmission-remote-cli
```

## Installation
```
git clone https://github.com/nsutic/torrent_scraper
cd torrent_scraper
echo "alias torrent='$PWD/torrent.sh'" >> ~/.bashrc
```
## Possible issues

If authentication fails then change it to your username and password in torrent.sh


## Usage

Run *torrent* from a terminal.

 
