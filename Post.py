from datetime import datetime


class Post:
    """
    Class to store an instance of each post.

    Holds the image path, image description, the time at which the image should be posted, and if
    the post has been posted.
    """

    def __init__(self, image, desc, post_time, posted=False):
        self.image = image
        self.desc = desc
        self.post_time = post_time
        self.posted = posted

    def __lt__(self, other):
        """ Used to order posts in the Priority Queue. Posts to be posted sooner are smaller. """

        return self.post_time < other.post_time
    
    def __gt__(self, other):
        """ Used to order posts in the Priority Queue. Posts to be posted sooner are smaller. """

        return self.post_time > other.post_time
    
    def __le__(self, other):
        """ Used to order posts in the Priority Queue. Posts to be posted sooner are smaller. """

        return self.post_time <= other.post_time
    
    def __ge__(self, other):
        """ Used to order posts in the Priority Queue. Posts to be posted sooner are smaller. """

        return self.post_time >= other.post_time
    
    def __eq__(self, other):
        """ Used to order posts in the Priority Queue. Posts to be posted sooner are smaller. """

        return self.post_time == other.post_time

    def serialise(self):
        """ Convert Post object to a dictionary representation that can be stored as JSON """

        time = self.post_time.strftime("%Y-%m-%d %H:%M:%S")
        return {
            "image" : self.image,
            "desc" : self.desc,
            'post_time' : time,
            'posted': self.posted
        }

