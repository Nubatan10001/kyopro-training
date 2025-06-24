# https://atcoder.jp/contests/abc410/tasks/abc410_a

N = int(input())
A = list(map(int, input().split()))
K = int(input())

count = 0
for a in A:
    if K <= a:
        count += 1

print(count)