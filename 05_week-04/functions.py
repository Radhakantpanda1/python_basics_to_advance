# set of codes to perform a particular task , promotes code reusability , easier to understand
# less chances of error

# function to add two numbers
def add(a,b):
    return a+b
print(add(11,25))

#
def mul(a,b):
    return a*b
print(mul(25,36))

def newAdd(a,b):
    print(a+b)

print(newAdd(2,9)) # None is returned

def arithmetic(a,b):
    return a+b,a-b,a/b
print((arithmetic(36,45))) # tuple
p,q,r=arithmetic(26,45)
l,m,_=arithmetic(23,11)# holding 2 out of 3 values
print("l,m,_",l,m,_) 
print(p,q,r) # holding multiple returned values
# print statement print the data where as return statement returns the value which can be used later
# passing list 
def List(a,b):
    return a*3,b*2
print(List([1,2,3,"rkp"],[11,"sinus"]))

def sub(p,q=10):
    print(p-q)
(sub(12))

def b_boolean(x=True,y=False):
    p=x or y
    return x,y,p
m,n,o=b_boolean(y=True)# it overwrites 
print(m , n , o)

# multiple inputs to a function
def hold(*hld): # *args --> static of args when we dont know how many arguments user will send
    print(type(hld))

hold('sinu','rkp',[1,5,9])
