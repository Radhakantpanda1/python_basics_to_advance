x={} # dictionary
print(type(x))
y={25} # set
print(type(y))
d={
    "name":"Radhakant Panda",
    "age":21,
    "subjects":['maths','physics','chemistry'],
    "hobby":('reading')
}
# key can be string boolean number
print(d)
print(type(d))
data={
    "name":"sinu",
    "name":"Radhakant"
}
# overwrites no duplicates in key
print(data["name"])
print(data)
d2={
    "name":"Radhakant Panda",
    "age":21,
    "subjects":['maths','physics','chemistry'],
    "hobby":('reading'),
    "data":{
    "name":"sinu",
    "name":"Radhakant"
}
}
print("sub-",d2["subjects"][2])
print(d2["data"])
#***************************** important****************************
# key-wise
dict={
   # [1,2,3]:"sinu",
   # {1,2,5}:"rkp"
   (1,2,9):"lp",
   9:"pl"
}
dict[9]="jppp" # dict is mutable
print(dict)
for i in d2:
    print(i)
    print(d2[i])

print(d2.keys())
print(d2.values())
print(d2.items())
print("name" in d2.keys())
print(len(d2))

for i in d2:
    if i=="subjects":
        for j in d[i]:
            if j=="maths":
                print(j)