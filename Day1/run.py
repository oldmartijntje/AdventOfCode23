numbers = []
first = -1
last = -1
total = 0

f = open("input.txt", "r")
data = f.read().splitlines()
print(data)

for line in data:
    first = -1
    last = -1
    for char in line:
       if char.isdigit():
           if first == -1:
               first = int(char)
           else:
               last = int(char)
    if last == -1:
        last = first
    numbers.append(f"{first}{last}")

for number in numbers:
    total += int(number)
print(total)