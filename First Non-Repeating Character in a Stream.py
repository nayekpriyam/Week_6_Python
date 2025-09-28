from collections import deque, Counter

def first_non_repeating(stream):
    q = deque()
    count = Counter()
    result = []
    for ch in stream:
        count[ch] += 1
        q.append(ch)
        while q and count[q[0]] > 1:
            q.popleft()
        result.append(q[0] if q else '#')
    return result

stream = "aabc"
print(first_non_repeating(stream)) 