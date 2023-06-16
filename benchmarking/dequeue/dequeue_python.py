
class DequePython:
    def __init__(self):
        self.deque = []

    def add_front(self, item):
        self.deque.insert(0, item)

    def add_rear(self, item):
        self.deque.append(item)

    def remove_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.deque.pop(0)

    def remove_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.deque.pop()

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.deque[0]

    def peek_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.deque[-1]

    def is_empty(self):
        return len(self.deque) == 0

    def size(self):
        return len(self.deque)
