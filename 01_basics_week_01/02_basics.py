# boolean
a=True
b=False
print(a+a+a+b-a) # 2
print(a+5)
# print(True/False) # ZeroDivisionError: division by zero

# complex number is combination of real and imaginary
a=5+69j
b=25+61j
print(type(a)) # <class 'complex'>
print(a.real)
print(a.imag)
print(a*b)
print(a+b)
print(a/b)

"""
print(1+"radhakant")# TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(1+'2') # error
"""

name='Radhakant'
title='panda'
print(name+title) # Radhakantpanda  --> concatenation
a=input("Enter your name-")
