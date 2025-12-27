import sys
n = sys.stdin.readline().strip()
m = sorted(n, reverse=True)
print(''.join(m))
