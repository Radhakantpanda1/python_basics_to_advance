list_a=['hello',True,[1,2,3,4],['apple','mango']]
for i in list_a:
    if type(i)==list:
        print(i)
new_l=['a','b','c']
print(new_l+list_a) # concatenation
print('hello' in list_a) # returns a boolean value
print(max([2,5,8,9,6])) # p is max
print(max(['a','b','c'])) # c is max
print(max(['sinu','radhakant'])) # sinu is max
print(min(['sinu','radhakant'])) # radhakant
print(max(['a','A'])) # as per ascii values
print(max(['sinu','sinp']))
print('sinu' in ['sinu','rkp']) # true

# append() it appends data at end of list 
list_a.append('sinu')
list_a.append(3+5j)
# insert() it inserts data at any position
list_a.insert(2,'name')
list_a.insert(-2,'rkp')# objects at -1 and at -2 were pushed forward
print(list_a)
print(list_a[-1])
print(list_a.count('sinu'))
# extend()
l=[1,2,3,4,5,6]
l.append('rkp')
l.extend("rkp1")#[1, 2, 3, 4, 5, 6, 'rkp', 'r', 'k', 'p', '1']
# extend() unwraps a string and insert one by one
# extend() only intakes iterable objects like strings , lists
# extend() can't take number as they are not iterable
# l.extend(123) #'int' object is not iterable
l.extend(['av','lk']) # unwraps it and the inserts
l.append(['sinu','rkp'])
print(l.index('rkp'))
nl=[1,2,3,4,5,6,7,8,9,10]
print('popped=',l.pop())
print(l.pop(1)) # popping from a index
print(l)
new=[1,2,2,3,5,6,6]
print(new.remove(2))# removes the element not the index
print(new.sort())
print(new)
