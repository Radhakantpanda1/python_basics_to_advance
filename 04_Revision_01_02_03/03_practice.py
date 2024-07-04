
# and and or upon numbers
print(36 and 25)
print(11 or 36)
print(12 and 12)
print(12 or 12)

# and and or on strings
print('sinu' and 'radhakant')
print('rkp' and 'sinu')
print('sinu' or 'sinu')
print('sinu' and 'sinu')

print([1,1,1] and ['sinu'])
print('sinu' and 0)

# The basic concept for the above types of problem is they are left precedence so the left one is 1 and right one is 0 , consider it and evaluate

# reversing a string
name='Radhakant Panda'
print(name[::-1])
for i in name:
    print(i)

print(len(name))
print('radhakant'+'panda')# concatenation
print(name[2:5])
print(name[2:-1])
print(name[3:1:-1])


name='Radhakant Panda'
print(name.find('anda'))
print(name.count('anda'))
print(name.split())
print(name.split('a'))
print(name.upper())
print(name.lower())
print(name.swapcase())
print(reversed(name))
print(name.replace('a','9'))
a=['rkp','sinu','radhakant','panda']
a.sort()
print(a)

