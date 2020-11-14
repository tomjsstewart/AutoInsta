from instapy_cli import client
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from eventHandler import InstaHandler
from InstaWatcher import InstaWatcher

import credentials as creds
cookie = None

def test():
    image = "keep-calm-testing-in-progress.png"
    text = "TESTING\r\n\r\nPlease Ignore"

    with client(creds.USERNAME, creds.PASSWORD, cookie) as cli:
        cli.upload(image, text)


if __name__ == "__main__":
    path = "images"
    print(path)
    InstaWatcher(path).run()
