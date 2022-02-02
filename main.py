numbers = []
k = 0
n = int(input(''))
while True:
    a = int(input())
    numbers.append(a)
    if len(numbers) >= n:
        break
for i in numbers:
    k += i
print(k)