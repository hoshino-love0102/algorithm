import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
targets = list(map(int, input().split()))
d = deque(range(1, N + 1))
answer = 0

for t in targets:
    idx = d.index(t)
    if idx <= len(d) - idx:
        d.rotate(-idx)
        answer += idx
    else:
        move = len(d) - idx
        d.rotate(move)
        answer += move
    d.popleft()

print(answer)
