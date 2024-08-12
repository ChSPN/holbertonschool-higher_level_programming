# 29. Python3: Mutable, Immutable... everything is object!

## Understanding Python's Object Model: Key Concepts in Identity, Mutability, and Functions

### Introduction
Python treats everything as an object, from simple data types like integers to complex structures like lists. This post covers the core concepts of identity, mutability, and how Python handles function arguments, which are essential for effective coding.

### ID and Type
Every Python object has a unique identity and a type. The id() function returns the object's identity (essentially its memory address), and type() reveals the kind of object it is, such as an integer or list. These characteristics define how Python treats each object.

x = 10
print(id(x))  # Unique ID
print(type(x))  # <class 'int'>


### Mutable vs. Immutable Objects
Mutable objects, like lists and dictionaries, can be altered in place, meaning changes affect all references to that object. Immutable objects, like integers and strings, can not be changed once created; modifying them creates a new object.

my_list = [1, 2, 3]
my_list.append(4)  # Changes the list in place


### Why It Matters
Understanding these differences is crucial. Mutable objects allow for changes that can have unintended side effects, while immutable objects ensure data remains unchanged unless explicitly altered.

### Function Arguments
Python passes arguments to functions by reference, meaning mutable objects passed to functions can be modified within the function, affecting the original object. Immutable objects, however, remain unchanged.

def modify_list(lst):
    lst.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # [1, 2, 3, 4]


### Conclusion
Grasping Python’s object model helps prevent bugs and optimize your code. Understanding how Python handles identity, mutability, and function arguments is essential for writing efficient and predictable programs.

