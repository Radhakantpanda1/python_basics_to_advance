my_list=['hello',True,0,13.696]# holds data of various data types
print(my_list[3:0:-1])
print(my_list[0:3:1])
my_name='Radhakant'
# print(my_list+my_name) error different data-type
my_name=list(my_name)
print(my_name)# ['R', 'a', 'd', 'h', 'a', 'k', 'a', 'n', 't']
print(my_name+my_list)#['R', 'a', 'd', 'h', 'a', 'k', 'a', 'n', 't', 'hello', True, 0, 13.696]
mul=9*my_list
print(mul)
print("sinu" in my_list)
print(type(my_list))
user_list=[2,3,6,5,["apple","mango"],[45]]
for i in user_list:
    if type(i)==list:
        print(i)
my_list.append("sinu")
print(my_list)
    