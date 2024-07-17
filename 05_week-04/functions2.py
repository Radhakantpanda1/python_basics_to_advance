# *args any number of parameters it can store
def static_args(*args):
    print(args)
    print(type(args))
static_args(1,2,3,4,"sinu")

# *kwargs anuynumber of key value pairs
def kw_args(**kwargs):
    print(kwargs)
    print(type(kwargs))

kw_args(z=1,b="sinu")

