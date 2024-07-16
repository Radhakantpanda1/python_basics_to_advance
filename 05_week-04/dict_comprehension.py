# dictionary comprehension
num_sq_dict={}
for i in range(10):
    num_sq_dict[i]=i*i

print(num_sq_dict)

sq_dict={i:i*i for i in range(10)}
print(sq_dict)