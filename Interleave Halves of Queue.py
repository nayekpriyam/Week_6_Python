from collections import deque

def interleave_queue(q):
    half_size = len(q) // 2
    first_half = deque()
    for _ in range(half_size):
        first_half.append(q.popleft())
    while first_half:
        q.append(first_half.popleft())
        q.append(q.popleft())

q = deque([1,2,3,4])
interleave_queue(q)
print(list(q)) 