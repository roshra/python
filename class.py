#!/usr/bin/python
"""
class starts with name class followed by class name then colon
example : class <class name>:

Object example: object name eq class name followed by parenthesis 
<object name>=<classname()>

define variable 

access variable using object with dot operator
<object name>.variable name should give variable value

"""

# simple class 
class roshclass:
    var=10
roshobj = roshclass()
print(roshobj.var)

# Data abstraction 
"""
show essential details to outside and imlemtation details are hidden
Data encapsulation ensure hiding , organizes data and method into structure thatprevents data access by any function that is not specified in class

any data with access level public can be accessed by any function belonging by any class
any data with access level private can be accessed only by the class in which its declared. highest level of protection

In python private variables are prefixed with double underscore (_)
example : __var is a private variable of the class 

functions defines in the class is called class methods

class methods 
The self arguments referes to the object itself, the object that has called the method
Even though method takes no argument. its built to take self as argument

functions defined to accept one parameter will actually take two

since class method uses self, they require instance of class t be used , often called instance methods 
"""

# program to access class member using class object 
class ABC():
    var =20
    def display(self):
        print("In class method ....")
obj = ABC()
print(obj.var)
obj.display()


# class constructor
# __init__ is automatically executed when object of class is created
# The methos is helpfu; to initialize the variables of class object 
# __init__ accepts one argument val
# like other class methods, first argument has to be self
# the newly created variable self.val123


# class variable and object variable

# Program to differentiate between class and object variables
class myclass():
    # class variable
    class_var = 0
    def __init__(self,var):
        myclass.class_var += 1
        print("value of early var is ", var)
        # Object variable
        self.rosh = var

        print("The object value is ", var)
        print("The value of class variable is : ", myclass.class_var)
obj1 = myclass(10)
obj1 = myclass(30)
obj1 = myclass(40)