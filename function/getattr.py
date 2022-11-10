# get the value of the "age" property of the "Person" object.
# The getattr() function returns the value of the specified attribute
# from the specified object.

# Syntax:
# getattr(object, attribute, default)


# object:required . an object.
# attribute:the name of the attribute you want to get the value from.
# default: The value to return if the attribute does not exist.
# class Person:
#     name="john"
#     age=34
#     country="Norway"

# x=getattr(Person, 'page','my message')
# print(x)

# class Person:
#     name='shilpa'
#     age=43
#     gender='f'

# x=getattr(Person,'age')
# print(x)

# delattr() function
# The delattr() function will delete the specified attribute from 
# the specified object.

# Syntax:
# delattr(object, attribute)

# Delete the "age" property from the "person" object.

# class Person:
#     name="john"
#     age=36 
#     country="Norway"

# delattr(Person,'age')
# x=getattr(Person,'age')
# print(x)


# hasattr() function:
# The hasattr() function returns True if the specified object has 
# the specified attribute,otherwise False.

# Syntax:
# hasattr(object, attribute)


# check if the "Person" object has the "age" property:
# class Person:
#     name="john"
#     age=36 
#     country="Norway"

# x=hasattr(Person,'age')
# print(x)

# setattr():
# The setattr() function sets the value of the specified attribute 
# of the specified object.

# Change the value of the "age" property of the "person" object.

class Person:
    name="john"
    age=36
    country='Norway'

setattr(Person,'age',48)
x=Person()
print(x.age)
