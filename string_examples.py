#!/usr/bin/env python

s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r"spam\n"

print("It's a trap!")
print('The "musicians" played badly')

print('''It's a trap! -- that's no "moon"''')


movie_star = 'Billy Bob Thornton'

print(movie_star.upper())
print(len(movie_star))
print(movie_star.count('B'))
print(movie_star.upper().count('B'))

print(dir(movie_star))

print(movie_star.__len__()) # bad programmer! no biscuit!
print()


b = b'spam'
print(b)
print(b[0])

print(b.decode())
s = b.decode()

print(type(s), type(b))

w = "wombat"

print(w.encode())








