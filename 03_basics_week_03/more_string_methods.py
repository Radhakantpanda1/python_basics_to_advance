name='radh\tak\tant'
print(name)

a='We all are a part of Full stack'
# convert it to lower case
print(a.lower())
# count number of 'a'
print(a.count('a'))
# index of every 'a'
count=0
a_indexer=[]
for i in range(0,len(a)):
    if(a[i])=='a':
        count=count+1
        a_indexer.append(i)

for i in range(len(a_indexer)):
    print(a_indexer[i])

print(a.replace('a','in'))
print(a.split())


