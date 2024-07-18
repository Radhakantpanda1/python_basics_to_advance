# ****************************     tuple     **********************************
t1=()
# t1.add("sinu") no such functions
t1=(1,3,5,"rkp","sinu")
print(type(t1))
print((t1))
print(t1[::-1])# reversing a tuple
print(t1[::2])
t2=("apple","True","apple")
print(t1+t2) # appends the existing tuples and returns a new tuple
print(t1*2+t2)
#  t1[2]="ok"   'tuple' object does not support item assignment
print("sinu" in t1)
print(max(t2))
print(t2.count("a")) # 0
l1=list(t1)
l1.append("apple")
l1.remove("rkp")
print(l1)
t1=tuple(l1)

#*********************************** set *******************************************
s1=set()
print(type(s1))
for i in range(10):
    s1.add(i)
print(s1)
# print(s1[2]) # 'set' object is not subscriptable
# s1.add([12]) # unhashable type: 'list'
# s2={[1,2,3,"sinu"],(2,4,5)}   print(s2)
# print(s1*2)
s2={"rkp","sinu"}
# print(s1+s2) # unsupported operand type(s) for +: 'set' and 'set'

l1_s1=list(s1)
# print(l1_s1*1.5) can't multiply sequence by non-int of type 'float'
print(l1_s1*2)

#***************************************     dictionary         ***********************
d1={}

print(type(d1))
user_details={
    "name":"Radhakant Panda",
    "age":21,
    "isMarried":False,
    "Subjects":["Physics","Chemistry","Maths"],
    "user_account":{
        "userId":"radhakant@gmail.io",
        "userPswd":"IwillNotTell@hehe"
    }
}
print(user_details)
print("User Id-",user_details["user_account"]["userId"])
user_details["age"]=22
print(user_details) # mutable
print((user_details.keys()))
print(user_details.values())
print(user_details.items())
print((user_details["user_account"].keys()))
print((user_details["user_account"].values()))

# ****************** dictionary comprehension *******************************
# rank vs name 
rank={r:"rkp" for r in range(10)}
print(rank)



# *************************** functions ************************************
def add(x,y):
    return x+y
print(add(12,36))

def arithmetic(x,y):
    return x+y,x*y,x-y
sum,mul,sub=arithmetic(23,11)
print(sum, mul, sub)
x=arithmetic(22,2)
print(type(x))