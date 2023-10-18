"""
Non local variables - code examples
Scope of the names defined in the class block; it does not extend to the code blocks of methods - this includes comprehensions and
generator expressions since they are implemented using a functions scope.
"""
foo = 100

class Fred:
    a =42
    # b = list(a+i for i in range(10)) # will fail as generators and comprehensions are implemented using function scope.


# This is an example of python closures
def counter():
    num = 200
    
    def incrementer():
        nonlocal num
        num += 1
        return num
    return incrementer()


print(counter())

