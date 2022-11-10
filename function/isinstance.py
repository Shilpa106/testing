# The isinstance() function returns True if the specified object is 
# of the specified type, otherwise False.

# isinstance(object,type)

# x=isinstance("Hello",(float,int,str,list,dict,tuple))
# print(x)

# check if y is an instance of myObj.
class myObj:
    name='john'

y=myObj()

x=isinstance(y,myObj)
print(x)

