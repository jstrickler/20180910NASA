#!/usr/bin/env python

list1 = list()
list2 = ['a', 'b', 'c']
list3 = []

#  list(iterable)

for item in list2:
    print(item)
print()

list2.append('wombat')
print(list2)

things = ['egg', 'marmot', 'weasel']

list2.extend(things)
print(list2)

del list2[3]

print(list2)

x = list2.pop()  # pop(-1)
print(x)
print(list2)

x = list2.pop(2)
print(x)
print(list2)

y = list2.remove('marmot')
print(list2)

print(list2[-1])

print(list2[-0])

x = list2.append(5)
print(x)

list2.insert(3, "boots")

print(list2)

list2[1] = 'eggs'
print(list2, '\n')

for i in 1, 2, 99:
    try:
        result = list2[i]
    except Exception as err:
        print(type(err).__name__)
        print("Uh-oh,", err)
    else:
        print(result)
    finally:
        print("ALl done")



