# set  holds distinct values  || case sensitive
x=set()
print(type(x))
l=[12,69,45,12,45,85,96,56,66,'sinu','rkp','slp','rkp']
l_set=set(l)
print("Unordered -",l_set)
for i in l_set:
    print(i)

# print(l_set[0]) not permissable
# set gives unordered data

# function in set
ns=set()
ns.add(101)
# ns.add([12]) unleashed data only
print(ns.remove(101))
ns.add(1011)
ns.add(1201)
ns.clear()
ns.add(1011)
ns.add(1201)
print(ns)
s1={1,3,5,7,9}
s2={2,4,6,8,10}
# s1[2]=36 not possible
# print(s1+s2) not allowed
# s1*4 not allowed
# in order to duplicate elements we need to convert it to a list
t1=(25,36,96)
s4=set(t1)
print(s4)

