name='Radha kant'
print(name.islower())
print(name.isspace())
print(name.endswith('kant'))
print(name.isdigit())
print(name.startswith('R'))
print(name.isalnum())
print(name.isalpha())
print(name.istitle())# if first alphabate is capital

# find length of string
c=0
for i in name:
    c=c+1
print('length = ',c)

# iterating through string
for i in name:
    print(i)

# reverse a string using loop
for i in range(1,len(name)):
    print(name[-i])

print("******************************")
username='Radhakant'
vowels='AaeEiIoOuU'
for i in username:
    for j in vowels:
        if(i==j):
            print(i)
            break;

for i in  name:
    if i in vowels:
        print("{} is a vowel".format(i))

# pallindrome check
data=input('Enter the word-')
end=len(data)-1
s=0
while s<=end:
    if(data[s]!=data[end]):
        break
    else:
        s=s+1
        end=end-1

if(s<end):
    print('not a pallindrome')

else:
    print('pallindrome')

# another method
s=input("Enter your string-")
s_rev=s[::-1]
print(s_rev)
if s==s_rev:
    print("Pallindrome")
else:
    print("Not a pallindrome")