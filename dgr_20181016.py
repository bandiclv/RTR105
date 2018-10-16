n = 5
while n > 0:
    print(n)
          n = n - 1
    print("Blastoff!")
    print(n)

a = 5
while a > 0:
    print("Lather")
    print("Rinse")
print("Dry Off!")

b = 0
while a > 0:
    print("Lather")
    print("Rinse")
print("Dry Off!")

while True:
    line = input("> ")
    if line == "done"
        break
    print(line)
print("Done!")

while True:
    line = input("> ")
    if line[0] == "#":
        continue
    if line == "done":
        break
    print(line)
print("Done!")


for i in [5, 4, 3, 2, 1]:
    print(i)
print("Blastoff!")

friends = ["Josepeph", "Glenn", "Sally"]
for friend in friends:
    print("Happy New Year", friend)
print("Done!")

print("Before")
for thing in [9, 41, 12 ,3, 74, 15]:
    print(thing)
print("After")


largest_so_far = -1
print("Before", largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)

print("After", largest_so_far)


zork = 0
print("Before", zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print(zork, thing)
print("After", zork)

zork = 0
print("Before", zork)
for thing in [9 ,41, 12, 3, 74, 15]:
    zork = zork + thing
    print(zork, thing)
print("After", zork)



count = 0
sum = 0
print("before", count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print("After", count, sum, sum / count)


print ("Before")
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
        print("Largest Number", value)
print("After")
