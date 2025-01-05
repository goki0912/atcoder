# 差分配列
N, Q= map(int, input().split())
A = list(map(int, input().split()))
queries = list([list(map(int, input().split())) for _ in range(Q)])

diff = [A[i+1] - A[i] for i in range(N-1)]
answer = sum(abs(d) for d in diff)

for l, r, v in queries:
    l -= 1
    r -= 1
    if l != 0:
        answer -= abs(diff[l - 1])
        diff[l-1] += v
        answer += abs(diff[l-1])
    if r != N-1:
        answer -= abs(diff[r])
        diff[r] -= v
        answer += abs(diff[r])
    print(answer)
