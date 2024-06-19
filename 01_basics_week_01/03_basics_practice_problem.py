# Problem Statement
"""
take 3 integers as input from user say a,b,c then find (a+b)/c , add it with a complex number then show the result with your name
"""
a=int(input("Enter the value of a "))
b=int(input("Enter the value of b "))
c=int(input("Enter the value of c "))
after_opeation=(a+b)/c
print(after_opeation)
complex_num=36+59j
add_with_complex=after_opeation+complex_num
print(add_with_complex)
print(str(add_with_complex)+"Radhakant Panda")