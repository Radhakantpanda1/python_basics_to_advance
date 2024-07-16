# Tuples 
t=()
print(type(t))
t1=(26,85,45,'sinu',True,0,'a')
print(t1[3])
print(t1[0:4])
print(t1[::-1])# reverse
print(t1[-1])
print(t1[0:-1])
# t1[2]="woww" tuples are immutable
print(t1)
t2=(26,69,12)
print(t1+t2) # append operation  returns a new tuple
print(t2*2) # returns a new tuple
print('sinu' in t1) # returns bolean value
print(max(t2))# retuns max value for homogeneous data
print(max('sinu','raja'))
print(t1.count('sinu'))# number of occurences of a element
print(t1.index('sinu'))# starting index of ver first element
print(min('sinu','rk'))
# direct insertion of element is not possible in tuple
l1=list(t1)  # tuple to list
l1[5]=69
print(l1)
print(tuple(l1)) # list to tuple
ta=((1),('abd'),'ad',((1,2,3,4)),[('a','b')])
print(ta[4][0][1])
for i in ta:
    print(i)
    if type(i)==tuple:
        print("in tuple", i[0])

if len(t1)==len(t2):
    print("same length")

else:
    print("Different lenght")

user_name=('sinu',"radhakant","lokesh","suresh","ramesh")
i=input("Enter name ")
if i in user_name:
    print("name is avilable")

l_data=['a','v','c']
l_data.pop()
print(l_data)