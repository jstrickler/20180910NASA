#!/usr/bin/env python

from timeit import Timer

setup_code = 'values = []' # <1>

test_code_one = '''
for i in range(10000):
    values.append(i)
'''  # <2>

test_code_two = ''' 
i = 0
while i < 10000:
    values.append(i)
    i += 1
'''  # <2>

test_code_three = '''
values = list(range(10000))
'''  # <2>

test_code_four = '''
values = [i for i in range(10000)]
'''  # <2>


t1 = Timer(test_code_one, setup_code) # <3>
t2 = Timer(test_code_two, setup_code) # <3>
t3 = Timer(test_code_three, setup_code) # <3>
t4 = Timer(test_code_four, setup_code) # <3>

REPEATS = 1000
print("test one:")
print(t1.timeit(REPEATS))  # <4>
print()

print("test two:")
print(t2.timeit(REPEATS)) # <4>
print()

print("test three:")
print(t3.timeit(REPEATS)) # <4>
print()

print("test four:")
print(t4.timeit(REPEATS)) # <4>
print()

