from collections import deque

def reverse_first_k(q, k):
    stack = []
    for _ in range(k):
        stack.append(q.popleft())
    while stack:
        q.appendleft(stack.pop())
    q.extend(q[k:])

q = deque([1, 2, 3, 4, 5])
reverse_first_k(q, 3)
print(list(q)) 