from itertools import permutations

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

M = int(input())
kenaku = [[False] * N for _ in range(N)]
for _ in range(M):
   x, y = map(int, input().split())
   kenaku[x-1][y-1] = True
   kenaku[y-1][x-1] = True

answer = float('inf')

for perm in permutations(range(N)):
   valid = True
   cost = 0
   for i in range(N-1):
      if kenaku[perm[i]][perm[i+1]]:
         valid = False
         break
   if valid:
      for i in range(N):
         cost += A[perm[i]][i]
      answer = min(answer, cost)

if answer == float('inf'):
   print(-1)
else:
   print(answer)