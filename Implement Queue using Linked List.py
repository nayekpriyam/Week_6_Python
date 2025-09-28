class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None
        item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return item

    def peek(self):
        return None if self.front is None else self.front.data

    def is_empty(self):
        return self.front is None

q = QueueLinkedList()
q.enqueue(10)
q.enqueue(20)
print(q.dequeue()) 