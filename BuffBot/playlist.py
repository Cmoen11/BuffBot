import random
class Node:

    def __init__(self, link):
        self.song = None
        self.next = None
        if self.is_youtubelink(link):
            self.song = link
            self.next = None
        else:
            print("The link submited is not valid")

    def __str__(self):
        return str(self.song)

    def get_song(self):
        return self.song

    def queue_next(self, node: object, link: object) -> object:
        if node.next is not None:
            n = node.get_next()
            node.queue_next(n, link)
        elif node.next is None:
            node.next = Node(link)
        else:
            return

    def get_next(self) -> object:
        if self.next is None:
            print("get_next called with nothing in queue")
        else:
            return self.next

    def has_next(self):
        if self.next is None:
            return False
        else:
            return True

    @staticmethod
    def is_youtubelink(link):
        valid = "https://www.youtube.com/"
        if valid in link:
            return True
        else:
            return False


class Queue:
    def __init__(self):
        self.current = None
        self.playlist = []

    def add_song(self, link):
        if self.current is None:
            self.current = Node(link)
        else:
            self.current.queue_next(self.current, link)

    def make_playlist(self, node: Node):
        if node.has_next() is True:
            self.playlist.append(node.get_song())
            n = node.get_next()
            self.make_playlist(n)
        else:
            # end of the queue
            self.playlist.append(node.get_song())

    def pop(self):
        if self.current is not None:
            s = self.current.get_song()
            if self.current.has_next():
                self.current = self.current.get_next()
            else:
                self.current = None
            return s
        else:
            # playlist empty
            self.current = None

    def update_playlist(self):
        self.playlist.clear()
        self.make_playlist(self.current)

    def peter(self):
        r = random.randint(0, 1)
        songs = ["https://www.youtube.com/watch?v=_r0n9Dv6XnY", "https://www.youtube.com/watch?v=3GwjfUFyY6M"]
        return songs[r]
