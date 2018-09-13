#!/usr/bin/env python
import sys
M = 100  # GLOBAL

# def print(*things):
#     __builtins__.print("HA HA HA")

def spam():
    M = "xylophone"
    print("M is", M)
    y = 36  # LOCAL variable
    print("in spam() x is", M)

spam()
# print("in main y is", y)  WILL NOT WORK
print("main: x is", M)

def outer():
    m = 100

    def inner():
        print("inner(): m is", m)

    return inner

f = outer()
f()

#  local->nonlocal->global->builtin

class Toast():
    x = 5

    def mymethod(self):
        m = 99
        print(self.x)

print(Toast.x)

t = Toast()
t.mymethod()
