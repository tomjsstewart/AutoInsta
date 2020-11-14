from Post import Post

import queue as Q
from datetime import datetime
from dateutil import parser
import json



class PostQueue():
    """
    Stores all posts in the order in which they should be posted.

    PostQueue will read posts.json file to populate itself.
    """

    def __init__(self):
        self.queue = Q.PriorityQueue()
        self.retrieve()

    def put(self, post):
        """ Add a new post to the queue. """

        self.queue.put(post)

    def get(self):
        """ Remove and return first item in queue. """

        return self.queue.get()
    
    def remove_by_image_name(self, image):
        """
        Remove post with file name `image`.
        
        This will NOT affect items that have already been posted to instagram.
        """
        quel = []
        while not self.isEmpty():
            item = self.queue.get()
            if item.image == image:
                # Don't keep item to be removed
                if item.posted:
                    print("This item has already been posted and removing will not delete the post from instagram.")
                continue
            quel.append(item)

        for i in quel:
            self.queue.put(i)

    def top(self):
        """ Return but do not remove first item in queue. """

        p = self.queue.get()
        self.queue.put(p)
        return p

    def isEmpty(self):
        """ Check if the queue is empty. """

        return self.queue.empty()
    
    def clear(self):
        """ Empty the queue. """

        while not self.isEmpty():
            self.get()

    def serialise(self):
        """
        Return the queue in dictionary equivalent of JSON format. 
        
        Note that this is a destructive function
        """

        posts = []
        while not self.isEmpty():
            posts.append(self.get())
        return {'posts': [post.serialise() for post in posts]}
    
    def retrieve(self):
        """ Load previously saved version of the queue from JSON file. """

        with open('posts.json', 'r') as jsonFile:
            data = json.load(jsonFile)

        posts = data['posts']
        for p in posts:
            post = Post(p['image'], p['desc'], parser.parse(p['post_time']), p['posted'])
            self.put(post)

    
    def save(self):
        """ Save the queue to JSON file. """

        with open('posts.json', 'w') as jsonFile:
            json.dump(self.serialise(), jsonFile, indent=4)



if __name__ == "__main__":
    p = PostQueue()
    p.put(Post("path", "desc3", datetime.now()))
    p.put(Post("path", "desc", datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')))
    p.put(Post("path", "desc2", datetime.strptime('Jun 1 2015  1:33PM', '%b %d %Y %I:%M%p')))
    p.save()
    p.retrieve()
