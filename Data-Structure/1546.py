# https://www.acmicpc.net/problem/1546

N = int(input())
A = list(map(int, input().split()))

print(sum(A)/max(A)*100/N)

# max(N)은 O(N)의 시간복잡도를 가진다.
