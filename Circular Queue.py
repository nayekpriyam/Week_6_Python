class CircularQueue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0
        self.capacity = capacity

    def enqueue(self, item):
        if self.size == self.capacity:
            print("Queue Overflow")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("Queue Underflow")
            return None
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def display(self):
        idx = self.front
        for _ in range(self.size):
            print(self.queue[idx], end=' ')
            idx = (idx + 1) % self.capacity
        print()

cq = CircularQueue(5)
cq.enqueue(1)
cq.enqueue(2)
cq.display() 