import math
x=0
"""
This problem asks for the number of routes through a 20x20 grid from 1 corner to the opposite, only moving towards it along lattice lines
Of 40 moves made, 20 of them must be down/up and 20 must be left/right
"""
x=math.factorial(40)
x/=math.factorial(20)**2
print(x)