import sys

input = sys.stdin.readline

C = int(input().strip())

for i in range(C):
    data = list(map(int, input().split()))
    n = data[0]
    S = data[1:]
    
    avg = sum(S) / n
    cnt = sum(1 for s in S if s > avg)
    
    ratio = cnt / n * 100
    print(f"{ratio:.3f}%")
