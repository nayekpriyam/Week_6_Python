class QueueTwoStacks:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, x):
        self.s1.append(x)

    def dequeue(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        if not self.s2:
            return None
        return self.s2.pop()

q = QueueTwoStacks()
q.enqueue(10)
q.enqueue(20)
print(q.dequeue()) 