N = int(input())
users = set()

for i in range(N):
    S = input()
    if S not in users:
        users.add(S)
        print(i+1)