class QueueEmpty(Exception):
    pass


class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, value):
        self.queue.insert(0, value)

    def dequeue(self):
        if self.is_empty():
            raise QueueEmpty("Queue is empty, nothing to dequeue")
        return self.queue.pop()


if __name__ == '__main__':
    q = Queue()
    q.enqueue(34)
    q.enqueue(23)
    q.enqueue(55)

    print(q.queue)  # [55, 23, 34]

    try:
        print(q.dequeue())  # 34
        print(q.dequeue())  # 23
        print(q.dequeue())  # 55
        print(q.dequeue())  # error
    except QueueEmpty:
        print("Queue is empty")
