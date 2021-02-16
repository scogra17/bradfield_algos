import stack as s

# Queue is a queue implementation using stacks
class Queue(object):
    def __init__(self):
        self._items = s.Stack()

    def is_empty(self):
        return self._items.is_empty()

    def enqueue(self, item):
        self._items.push(item)

    def dequeue(self):
        tmp = s.Stack()
        while self._items.size() > 1:
        	tmp.push(self._items.pop())
        item = self._items.pop()

        while tmp.size() > 0:
        	self._items.push(tmp.pop())

        return item

    def size(self):
        return self._items.size()
