new_list = [1, 2, 3]
new_value = new_list[2]

print(new_list)
print(new_value)

if 1 in new_list:
    print(True)

for n in new_list:
    if n == 1:
        print(True, "again!")

        break

new_list.append(4)
print(new_list)


numbers = []

print(len(numbers))
numbers.append(1)
print(len(numbers))
print(numbers)

numbers.extend([2, 3 ,4 ,5 , 6])
print(numbers)