#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 09:35:39 2019

@author: sarun
"""

a = 10      # int
b = 4.2     # float
c = "abc"   # str
d = True    # bool
print(a)
print(b)
print(c)
print(d)

print('A number is ', a)
print(a, b, c)
print('Number = {:.3f}'.format(b))
print(f'Number = {b:10.3f}')

# casting
int(3.3)
str(3)

# Collections ~ Arrays
# 1. list
e = [a, 2.1, False, 'qwe']
e.append(100)
e[0] = 30   # indexing
e[1:3] = [True, 3.4] # slicing
print(e)

# 2. tuple
f = (9, b, 'zxc')
x,y,z = f   # unpacking
print(f)

# 3. dict
g = {'a':20, 'b':30, 1:890, 
     (2,3):[4,5,6]}
print(g)


# Control flow
# if statement
if a < 10:
    print('A is less than 10')
elif a==10:
    print('A is equal to 10')
else:
    print('A is greater than 10')
print('Done')

# while loop
i = 0
while i < 5 and a==10:
    i = i + 1
    if i == 3:
        continue
    print('loop', i)
        # break

# for loop
for i in range(5):
    print('loop', i)

for x in e:
    print(x)

# function
def func(name, age=21.5):
    print('Hello', name)
    print('Age = ', age)
    return 456, [1,2,3], age+10
    
a = func('Sarun')
print(func('Thammasat', 80))


# module
import os
h = os.path.join(
        '/home/sarun/Desktop', 
        'ex1.py')
cwd = os.getcwd()
os.path.isdir(cwd)
os.path.exists(cwd)

import datetime
print(datetime.datetime.now())

from os.path import join
k = join('/home/sarun/Desktop', 
        'ex1.py')

from datetime import datetime as dt
print(dt.now())

from os import path

import mycode
mycode.getdt()
mycode.getcwd()

from mycode import getdt, getcwd
getdt()
getcwd()





