'''
def Prep():
    print("Prepping...")

Prep()

#########################################################


def Foo():
    y = 20
    print("Inside Foo()")
    Bar()

def Bar():
    z = 30
    print("Inside Bar()")

def main():
    x=10
    print("In main()")
    Foo()


main()


# Define Higher (C++) vs. Define Earlier (Python)


# void Bar();
# 
# void Foo()
# {
#     cout << "Foo()" << endl;
#     Bar();
# }
# 
# void Bar()
# {
#     cout << "Bar()" << endl;
# }
# 
# int main()
# {
#     cout << "main()" << endl;
#     Foo();
# }

'''

####################################################################################################################################

## Argument Passing ##

def add(a, /, b = 0, *, c = 0):   # default args can only be on the rightmost side
    print(f"Adding a[{a}], b[{b}], c[{c}]")
    return a + b + c

print(add(1, 2))    # Utilises default args
# print(add(1, 2, 3)) # Positional args


# Named args

# print(add(c = 3, a = 1, b = 2))
# print(add(c = 3, a = 1))
# print(add(1, c = 3))
# print( add(b = 2, c = 3))     # Error


## Using the special args '/' & '*'
# '/' : Anything to its left has to be positional-only
# '*' : Anything to its right has to be keyworded
# anything between the two special args may be keyworded or positional, either.
print(add(1, c=3))
print(add(1, b =2, c=3))
print(add(1, 2, c=3))
print(add(1, 2, c = 3))
print(add(1, 2))

