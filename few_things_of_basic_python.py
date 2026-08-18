# ***** Importing Ways *****

# import MODULE                 # [import whole module]
# import MODULE as m            # [import whole module with alias the whole module]
# from MODULE import NAME
# from MODULE import NAME1, NAME2
# from MODULE import NAME as n  # [alias a specific name]

# *****************************************
# --- Index & Slicing ---
username = "annonymous-user"
print(len(username))    # 15
print(username[0])      # "a"
print(username[-1])     # "r"     [Counts negative index from last]
print(username[-2])     # "e"
print(username[:])      # "annonymous-user"
print(username[:4])     # "anno"
print(username[1:])     # "nnonymous-user"
print(username[0:2])    # "an"    [character at 2nd index will not be printed as slices are end-exclusive]
print(username[0:4:2])  # "an"    [Syntax: [start:stop:step]]
print(username[0:10:2]) # 'annmu' [start 0, every 2nd char]
print(username[0:10:3]) # 'aoms'  [start 0, every 3rd char]
print(username[::2])    # 'annmu-sr'        [default start/stop, every 2nd]
print(username[::-1])   # 'resu-suomynonna' [reverse]
print(username[5:1:-1]) # 'ynon'            [reverse from 5 to 1]

# username[0] = 'A'     # It throws error as "Strings are Immutable"

print("""Abc
Def
    Ghi

  Jkl
""")

txt = """Abc
Def
    Ghi

  Jkl
"""
print(txt.split())          # Split by any white space
print(txt.split(' ', 3))    # Split by space, max 3 splits

txt1 = "    What "
txt2 = " Wh a t "

# .strip() removes leading and trailing whitespace from the entire string, but not from each line.
print(txt.strip())
print(txt1.strip())
print(txt2.strip())

greet = "hello world"
print(repr(greet))
print(str(greet))
print(greet)

# *** Python & Math & Conditions ***
print(2 ** 10)          # 2 power 10 = 1024

# If we import as `from math import pi`, then we would do `print(pi)` instead of `print(math.pi)`
import math             # what is the format? is it import MODULE from LIBRARY
print(math.pi)          # Prints the value of π

# TODO: Add brief comments for what happened at each of thing below and why
print(math.floor(3.5))
print(math.floor(-3.5))
print(math.floor(3.9))
print(math.ceil(3.2))
print(math.ceil(-3.2))
print(math.trunc(2.9))

import random
print(random.random())  # Returns float in [0.0, 1.0)  — 0.0 inclusive, 1.0 exclusive
print(random.randint(2, 4))
lst0 = [9, 14, "Hammad", -1, (1, 2, 3), 6]
print(random.choice(lst0))
lst0 = [9, 14, "Hammad", -1, 1, 2, 3, 6]
print(random.shuffle(lst0))

print("\nInteger: ", int(12.25))
print("Float: ", float(3))

t = x, y, z = 2, 4, 6
# t[0] = 3              # Tuple is immutable
print(t)

print("\n" + str(1 == 2 < 3))   # OR `print("\n", 1 == 2 < 3, sep="")` as `print()` inserts a default separator space between its arguments
print(1 == (2 < 3))             # True    [`1` behaving as True]
print(True == 1)
print(True + 5)
print()

# `and` does not always return `True` / `False` immediately.
# It returns:
#   - the first falsy value, or
#   - the last value if all are truthy
print(1 == 2 and 2 < 3)         # False
print(5 and 2 < 3)              # True
print(5 and 1)                  # 1
print(5 and 0)                  # 0
print(0 and 5)                  # 0
print(5 and 7)                  # 7
print(7 and 5)                  # 5

print()
print(1 << 2)                   # [Bitwise Left Shift]
print(4 | 2)                    # [Bitwise OR]

# --- Union & Intersection ---
# Operators (|, &):
#   -> Require both sides to be actual set objects.
#   -> Passing a list or tuple will trigger a TypeError.

# Methods (.union(), .intersection()):
#   -> Accept any iterable object (like a list, tuple, or dictionary) as an argument.
#   -> Python automatically converts the iterable into a set behind the scenes.

seta = {1, 'A', 3, 5, 7, 9, 'C'}
setb = {0, 2, 'C', 4, 6, 8, 'M'}

print()

# Union
print(seta & setb)
print(seta.intersection(setb))

# Intersection
print(seta | setb)
print(seta.union(setb))

# Difference
print(seta - setb)

# --- Complex Numbers ---
x = 2 + 1j
print('\n', 2 * x, sep='')
print(5 + x)

# --- Numbers in Base-N ---
b2 = 0b10                       # For Bin --> 0b
# b2 = 0b3
b8 = 0o20                       # For Oct --> 0o
b16 = 0xFF                      # For Hex --> 0x
print()
print(b2, b8, b16)
print(bin(b2), oct(b8), hex(b16))
print(bin(84), oct(84), hex(84))
print(int('10', 2))
print(int('20', 8))
print(int('FF', 16))


# ***** Understanding Mutable vs Immutable *****
print("\n\n --- Mutable vs Immutable ---")

# --- Lists are Mutable while Strings are Immutable, so check the behaviour ---

lst1 = [2, 4, 6]
lst2 = lst1                 # [2, 4, 6]
print('\nlst2 = ', lst2)

lst1[1] = 3
print('\nlst1 = ', lst1)    # [2, 3, 6]
print('lst2 = ', lst2)      # [2, 3, 6]

# ---

lst3 = [1, 2, 3]
lst4 = [1, 2, 3]

lst3[0] = 5

print('\nlst3 = ', lst3)    # [5, 2, 3]
print('lst4 = ', lst4)      # [1, 2, 3]

# ---

score = 10
a_score = score             # `a_score` --> `10` [Now `a_score` references the same object as `score`]
print("\na_score = ", a_score)

score = 12                  # while `a_score` --> `10` as its still pointing to `10`
print("\nscore = ", score)
print("a_score = ", a_score)

# ---

ls1 = [1, 2, 3]
ls2 = ls1
ls1 = "my-string"

print("ls2 = ", ls2)        # `ls2` --> `[1, 2, 3]`
print("ls1 = ", ls1)        # `ls1` --> `"my-string"`

ls2[0] = 34                 # `[1, 2, 3]` to `[34, 2, 3]`
print("ls2 = ", ls2)        # `ls2` --> `[34, 2, 3]`

# ---

lst5 = [0, 1, "user", 3]
print("\nlst5 = ", lst5)

lst5[2] = "myuser"
print("lst5 = ", lst5)
print("lst5[2][:3] = ", lst5[2][:2])

# lst5[2][1] = "e"            # will throw error

# Alternative way:
s = lst5[2][:1] + "e" + lst5[2][2:]
lst5[2] = s
print("lst5 = ", lst5)


# ***** Reassignment, Shallow/Deep Copy *****

# In Python, a variable is not a box that holds a value.
# It is a label that points to an object in memory.
# And a list is not an array of values — it's an array of references (pointers) to objects.

# --- Shallow Copy: 4 Equivalent Methods ---
# h1 = [[1, 2], [3, 4]]

# h2 = h1[:]           # Slice syntax
# h2 = h1.copy()       # List method
# h2 = copy.copy(h1)   # copy module
# h2 = list(h1)        # list constructor

# ---

h1 = [1, 2, 3]
h2 = h1[:]                      # Shallow copy

print("\nh1 = ", h1)
print("h2 = ", h2)
print("Are 'h1' and 'h2' pointing to same list objects?        ", h1 is h2)
print("Are 'h1[0]' and 'h2[0]' pointing to same inner objects? ", h1[0] is h2[0])

h1[0] = 5

print("\nh1 = ", h1)
print("h2 = ", h2)

# ---

h2 = h1.copy()                  # Shallow copy

print("\nh1 = ", h1)
print("h2 = ", h2)
print("Are 'h1' and 'h2' pointing to same list objects?        ", h1 is h2)
print("Are 'h1[0]' and 'h2[0]' pointing to same inner objects? ", h1[0] is h2[0])

h1[0] = 7

print("\nh1 = ", h1)
print("h2 = ", h2)

# ---

import copy
h2 = copy.deepcopy(h1)      # Deep copy

print("\nh1 = ", h1)
print("h2 = ", h2)
print("Are 'h1' and 'h2' pointing to same list objects?        ", h1 is h2)
print("Are 'h1[0]' and 'h2[0]' pointing to same inner objects? ", h1[0] is h2[0])

h1[1] = 14

print("\nh1 = ", h1)
print("h2 = ", h2)

# h1[0] is h2[0] prints True even for deepcopy. It's a CPython optimization:
# deepcopy does not copy immutable objects like int, str, float, bool.
# Since they cannot be mutated, copying them would waste memory with zero benefit.
# The deepcopy module simply returns the same reference if an object is atomic.
# The deepcopy distinction only appears when a list contains mutable nested objects.

# ---

h2 = h1                     # Reference Assignment (alias)

print("\nh1 = ", h1)
print("h2 = ", h2)
print("Are 'h1' and 'h2' pointing to same list objects?        ", h1 is h2)
print("Are 'h1[0]' and 'h2[0]' pointing to same inner objects? ", h1[0] is h2[0])

h1[1] = 2

print("\nh1 = ", h1)
print("h2 = ", h2)

# ---

h1 = copy.copy(h2)          # Shallow copy

print("\nh1 = ", h1)
print("h2 = ", h2)
print("Are 'h1' and 'h2' pointing to same list objects?        ", h1 is h2)
print("Are 'h1[0]' and 'h2[0]' pointing to same inner objects? ", h1[0] is h2[0])

h2[1] = 88

print("\nh1 = ", h1)
print("h2 = ", h2)

# ***** == VS is *****

v1 = [1, 2, 3]
v2 = [1, 2, 3]
v3 = v1

print("Does v1, v2 and v3 have same values? ", v1 == v2 == v3)
print("Are v1 and v3 pointing to same objects? ", v1 is v3)
print("Are v1 and v2 pointing to same objects? ", v1 is v2)

