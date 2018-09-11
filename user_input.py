#!/usr/bin/env python

while True:
    name = input('What.....is your name? ')
    if name == 'q':
        break
    if name == '':
        continue
    quest = input('What.....is your quest? ')
    print("Welcome, {} -- good luck with {}".format(name, quest))
