
class Node:

    def __init__(self, link):

        self.song = link
        self.next = None

    def get_song(self):
        return self.song

    def queue_next(self, link):
        if self.next is not None:
            self.next.queue(link)
        else:
            self.next = Node(link)

    def get_next(self) -> object:
        if self.next is None:
            return
        else:
            return self.next


class Queue:
    def __init__(self, link):
        self.current = Node(link)
        self.playlist = []

    def update_playlist(self):

        self.playlist.append()

    def skip_song(self):
        self.current = self.current.get_next()
