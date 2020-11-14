from Post import Post
from PostQueue import PostQueue

from watchdog.events import FileSystemEventHandler
from datetime import datetime


class InstaHandler(FileSystemEventHandler):
    """
    Class to handle different changes detected in the src_path directory.
    """
    def __init__(self):
        super().__init__()
        
    def on_created(self, event):
        """
        Called if a new file or directory is created.

        Create a new post item in the posts.json file, this post is then scheduled for posting.
        """
        if event.is_directory:
            print("Ignoring directory creation")
            return
        
        pq = PostQueue()
        desc = "Assign"
        post_time = datetime.now()
        posted = False

        post = Post(event.src_path, desc, post_time, posted)
        pq.put(post)
        pq.save()
    
    def on_deleted(self, event):
        if event.is_directory:
            print("Ignoring directory removal")
            return
        
        pq = PostQueue()


