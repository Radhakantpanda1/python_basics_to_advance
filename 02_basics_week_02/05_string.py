name="RadhakantPanda"
print(name)
print(name[0])
print(name[5:10]) #kantP  10 is excluded
print(name[5:13:2]) # name([starting:ending:step-size])
print(name[0:14:3]) # step size=3
# printing in reverse order
# print(name[12:0]) error bcoz stepsize is 1
print(name[14:0:-1])  # starting from 13 we are moving towards zero by stepping -1
print(name[::-1])# complete string reversal
print(name[5:-3]) # from 5 to -3
print(name[0:-1]) # negetive is for reversing from end to start
print(name[-1])
print(name[0:12:5])

# for loop in string
for i in name:
    print(i)    # i = R A D H A K A N T A P A N D A  iterated one by one character

for i in name:
    print(i)
    if i== 't':
        print("Found it")
        break;
s='My name is sudhansu'

# for else loop
# the else part of for loop is only executed when for loops completes itself not when it breaks


for i in s :
    if i == "n":
        continue 
    print(i)
else :
    if i == 'u':
        print("last char was u ")
    print("this is a else condtion ")

print('******************************************************')
print(len(name))
new_name=''
for i in range(len(name)):
    if(name[i]=='a'):
        pass
    else:
        new_name=new_name+name[i]
print(new_name)
