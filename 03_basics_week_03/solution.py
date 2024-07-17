
"""
Q)[[],[],[]]
a. append 2 more list and 1 complex number in between the existing list
b. if your nested list contain string find out it's index and print it then remove it
c. extract second element of each nested list
"""
temp_list=[['apple','mango','mango','mango',True],['fn','cln','gpn'],[['fk']]]
list_1=['al','al','lm']
list_2=['ps','as']
cmpl_no=3+6j
temp_list.insert(1,list_1)
temp_list.insert(3,list_2)
temp_list.insert(5,cmpl_no)
print(temp_list)

# bans)
for i in range(len(temp_list)):
    outer_index=i
    if type(temp_list[i])==list:
        for j in range(len(temp_list[i])):
            if type(temp_list[i][j])==str:
                inner_index=j
                print(temp_list[outer_index][inner_index])
                print('Inner index=',inner_index,"Outer index is =",outer_index)


str_counter=0
print("*************************")
for i in range(len(temp_list)):
    outer_index=i
    if type(temp_list[i])==list:
        for j in range(len(temp_list[i])):
            if type(temp_list[i][j])==str:
                str_counter+=1

        k=str_counter
        i_in=0
        while(i_in<k):
            if(len(temp_list[i])>0):
                print(len(temp_list[i]))
                if(type(temp_list[i][i_in])==str):
                    print(temp_list[i][i_in])
                    temp_list[i].pop(i_in)
                    k-=1
                
                else:
                    i_in+=1
print(temp_list)

            


