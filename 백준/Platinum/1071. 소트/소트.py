import sys
input = sys.stdin.readline

n = int(input())
v = list(map(int, input().split()))
v.sort()

for i in range(n-1):
    if v[i] + 1 == v[i+1]:
        end = i + 2
        while end < n and v[end] == v[i+1]:
            end += 1
        if end == n:
            start = i - 1
            while start >= 0 and v[start] == v[i]:
                start -= 1
            v[start+1] += 1
            v[i+1] -= 1
        else:
            v[i+1], v[end] = v[end], v[i+1]

print(*v)