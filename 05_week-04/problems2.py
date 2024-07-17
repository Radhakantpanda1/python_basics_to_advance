# given multiple lists to a function return a single list

def list_collector(*List):
    empty_list=[]
    for i in List:
        for j in i:
            empty_list.append(j)

    return empty_list
print(list_collector([1,3,4,5],[22,45],['sinu','rkp']))
# m-02 using list comprehension
def list_collector2(*List):
    empty_list=[j for i in List for j in i if type(i)==list]
    return empty_list
print(list_collector2([1,3,4,5],[22,45],['sinu','rkp'],"sinu"))


#q) create a function to take any number of mixed data and try to create a list of separate datatype and return multiple result
def separate_data(*args):
    for i in args:
        



# soln



#q2) create a function which will be able to use *args and **kwargs and it will bw able to do all list value concatenation and return a list