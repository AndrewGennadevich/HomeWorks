n = input().split()
for i in range(len(n)):
    n[i] = int(n[i])

for i in range(2, len(n)):
    if n[i] == 0:
        n[i] = n[i - 1] + n[i - 2]
print(n)
