from typing import List


class Queue():
    def __init__(self, items):
        self._items = []

        if items != []:
            for elem in items:
                self._items.append(elem)


    def is_empty(self):
        return self._items == []

    def enqueue(self, item: int) -> None:
        self._items.append(item)

    def dequeue(self) -> int:
        value = self._items.pop(0)
        return value


class LinkedQueue(Queue):
    def __init__(self, items):
        Queue.__init__(self, items)

    def enqueue(self, item: int):
        self._items.append(item)


if __name__ == '__main__':
    q = Queue([])
    lq = LinkedQueue([2, 3, 4, 5])
    lq.enqueue(1)
    print(lq._items)
