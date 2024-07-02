print(8 and 4)
print(4 and 8)

a=10
b=20
print( a and b) # 20
print(b and a) # 10
# what happens here is precedence is fom left side so a is treated is 1 and b as 0 so 1 and 0 is 0 which is b

print(4 or 8)  # 4
print( 8 or 4) # 8

x=['a','b',['c']]
for i in range(len(x)):
    print(i)
    i=i-1