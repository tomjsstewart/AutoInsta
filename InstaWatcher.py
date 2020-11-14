from instapy_cli import client
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from time import sleep
from datetime import datetime

from eventHandler import InstaHandler
from PostQueue import PostQueue

import credentials as creds




image = "keep-calm-testing-in-progress.png"
text = "TESTING\r\n\r\nPlease Ignore"

# with client(creds.USERNAME, creds.PASSWORD) as cli:
#     cli.upload(image, text)

class InstaWatcher:
    """ Class that watches the images directory for added image files. """
    def __init__(self, path, recrsive=True):
        self._src_path = path
        self._recrsive = recrsive
        self._event_handler = InstaHandler()
        self._observer = Observer()

    def run(self):
        """ Waiting loop, upon keyboard interrupt halt. """

        print("Running")
        self.start()
        try:
            while True:
                # update the post queue
                print("Updating post Queue")
                post_queue = PostQueue()
                while post_queue.top().post_time < datetime.now():
                    # Post this item
                    post = post_queue.get()
                    self.post_item(post)
                    post_queue.save() # Transitivly destructive
                    post_queue.retrieve() # Retrieve new queue
                print("sleeping 60 secs")
                sleep(60)
        except KeyboardInterrupt:
            self.stop()
    
    def post_item(self, post):
        print(f"posted image: {post.image} at time: {post.post_time}")
        # with client(creds.USERNAME, creds.PASSWORD) as cli:
        #     cli.upload(post.image, post.desc)

    def start(self):
        """
        Start the observer.

        The observer will wait for changes in the src_path directory and call the event handler
        function for the relevant observation.
        """

        print("Starting")
        self._observer.schedule(self._event_handler, self._src_path, recursive=self._recrsive)
        self._observer.start()
        print("Started")

    def stop(self):
        """ Stop observing src_path directory. """

        print("Stopping")
        self._observer.stop()
        self._observer.join()
        print("Stopped")
