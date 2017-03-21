
class Node:

    def __init__(self, link):

        self.song = link
        self.next = None

    def get_song(self):
        return self.song

    def queue_next(self, node: object, link: object) -> object:
        if node.next is not None:
            self.queue_next(node.get_next(), link)
        else:
            self.next = Node(link)

    def get_next(self) -> object:
        if self.next is None:
            return
        else:
            return self.next

    def has_next(self):
        if self.next is None:
            return False
        else:
            return True


class Queue:
    def __init__(self, link):
        self.current = Node(link)
        self.playlist = []

    def skip_song(self):
        self.current = self.current.get_next()

    def update_playlist(self, node: Node):
        self.playlist.append(node.get_song())
        if self.has_next(node) is True:
            self.update_playlist(node.get_next())
        else:
            print("Playlist updated")

    def pop(self):
        s = self.current.get_song()
        if self.current.has_next():
            self.current = self.current.get_next()
        else:
            # playlist empty
            self.current = None
        return s
