names = ['Andrew', 'Lena', 'Olha', 'Karina']
print(names[2], names[3], names[4])
# Version 1
a = []
for i in range(101, 169):
    if i % 2 == 1:
        print(i)
# Version 2
b = []
for i in range(1, 99):
    if i % 2 == 1:
        b.append(i)
        print(b)
# Version 3
x = list(range(1001, 1090, 2))
print(x)
