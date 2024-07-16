# take input from user a paragraph
#1 convert it into a list
#2 remove duplicates
#3 use above distice elements as keys for dictionary and assign your name as value of all the key for dictionary
#4 print tupple of all the values
#5 print list of all the keys
para_from_user=input("Enter your paragraph-")
para_list=para_from_user.split(' ')
print(para_list)
set_para=set(para_list)
print(set_para)
para_dict={}
for i in set_para:
    
    para_dict.update({i:"rkp"})

print(para_dict)
print(tuple(para_dict.keys()))
print("values=",tuple(para_dict.values()))
print("Values=",list(para_dict.values()))


para_dictionary_form={i:"radhakant" for i in set_para}
print(para_dictionary_form)

