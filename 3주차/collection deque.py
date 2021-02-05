from collections import deque

deq = deque(['a', 'b', 'c'])
deq.append('d')
deq.appendleft('d')
deq.pop()
deq.popleft()
deq.rotate(n)