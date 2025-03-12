N = int(input())

data = [tuple(map(int, input().split())) for _ in range(N)]

Q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(Q)]

sum1 = [0] * (N+1)
sum2 = [0] * (N+1)

for i in range(N):
    C, P = data[i]
    sum1[i+1] = sum1[i] + (P if C == 1 else 0)
    sum2[i+1] = sum2[i] + (P if C == 2 else 0)

for L, R in queries:
    print(sum1[R] - sum1[L-1], sum2[R] - sum2[L-1])
