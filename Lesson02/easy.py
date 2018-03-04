#задача 1
list_of_fruits = ["яблоко", "банан", "киви", "арбуз"]

counter = 1
for fruit in list_of_fruits:
    print(f"{counter}.{fruit}")
    counter +=1

#задача 2
list1 = ['a', 'b', 'c', 'd', 'e']
list2 = ['a', 'z', 'x', 'y', 'e']

difference = set(list1) - set(list2)
print(difference)

# задача 3
integer_list = range(1,11)
new_list = []

for i in integer_list:
    if i % 2 == 0:
        new_list.append(i / 4)
    else:
        new_list.append(i * 2)

print(new_list)




