a='hello'
print(a)
l='Learning python"s from ineuron'
p="hello ji's"
print(l)
print(p)
print(p[-1])
for i in range(0,len(p)):
    print(p[i])
print(p[2:5])
print(l[-1:-4:-1])
for i in l:
    print(i)
name=' Radhakant Panda'
print(name[::-1]*5)# reverse order
print(name[::-3])
l="mane"+"lane"
# m="mane"+36
# print(m) string can only be concatenated with string only
print(l)
for i in range(len(name)):
    if(name[i]=='a'):
        name[i]='#'
    print(name)
    # string in python is immutable
    
# list is mutable object
name_of_students=["rohan","sohan","mohan"]
for i in range(0,len(name_of_students)):
    if(name_of_students[i]=="mohan"):
        name_of_students[i]="Radhakant Panda"
    
print(name_of_students)