# find() methods
my_name="Radhakant Panda"
print(my_name.find('Panda')) # returns the startinf index of sub-str if present else returns -1

str="kant"
si=my_name.find(str)
# printing all the indexes of str
for i in range(len(str)):
    print(si+i)

# count() returns the number of occurences of particular sub str
print("count",my_name.count('a'))

# split() split based on the parameter
print(my_name.split('a')) # returns a list
print(my_name.split()) # by default based on space
 
# to upper case upper()
print(my_name.upper())

 # to lower case .lower()
print(my_name.lower())

# .swap()
print(my_name.swapcase())

# .join()
print("*".join(my_name))

print(list(reversed(my_name)))

# reversed() returns a object
new_name="         sinu          "
print(new_name.strip())
print(new_name.lstrip())
print(new_name.rstrip())

print(my_name.replace('a','p'))
# returns a new string with replaced data

