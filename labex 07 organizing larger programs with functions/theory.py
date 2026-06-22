def sumcount(n):
    '''
    Returns the sum of all integers less than or equal to n
    :param n:
    :return: int:
    '''
    total = 0
    while n>0 :
        total += n
        n -= 1
    return total

a = sumcount(3)
print(a)

'''
Examples of using import libraries
'''
import math
x = math.sqrt(10)
print(x)

import urllib.request
u = urllib.request.urlopen('http://www.google.com')
data = u.read()
print(data)

'''
Errors and exceptions
'''
with open('../labex/portfolio.csv', 'rt') as f:
    headers = next(f)
    for line in f:
        line.strip()
        if not line : continue
        fields = line.split(',')
        try:
            shares = int(fields[1])
        except ValueError:
            print("Couldn't parse", line)

'''
Defining function
'''
def greeting(name):
    'Issues a greeting'
    print("Hello, " + name + "!")
greeting('Guido')
greeting('Paula')
