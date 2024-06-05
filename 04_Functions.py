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
'''
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



# Packing and Unpacking
lst1 = [1, 2, 3]
a, b, c = lst1          # Unpacking lst1 to 3 individual elements

lst2 = a, b, c
print(type(lst2), lst2)

[*lst3] = a, b, c
print(type(lst3), lst3)


print(lst3)
print(*lst3)        # Unpacking


# void Func(int, int)  -->     void (*fptr)(int, int) = Func;
# typename void (*FnType)(int, int)

# FnType f1, f2;
# f1 = Func


# {*lst4} = a, b, c     # <-- Doesn't work yet. 
# print(type(lst4), lst4)

'''
'''
def add(a, b):
    print(f"Adding a[{a}], b[{b}]")
    return a + b

print(add(1, 2))
lst = [1, 2]
print(add(lst[0], lst[1]))
print(add(*lst))


def mul(a, b, *dataSet):
    print(f"a -> {type(a)}, {a}")
    print(f"b -> {type(b)}, {b}")
    print(f"dataSet -> {type(dataSet)}, {dataSet}")
    prod = a * b
    for val in dataSet:
        prod *= val

    return prod

print(mul(1, 2, 3))
print(mul(1, 2, 3, 4, 5))
print(mul(1, 2))
print(mul(a = 1, b = 2))


def Print(*data):
    print(f"Data -> {type(data)}, {data}")
    for val in data:
        print(val, end='----')
    print()

lst = [1, 2, 3, 4, 5]
tp = (10, 20, 30)
Print(lst, tp)


# print(mul(a = 1, b = 2, dataSet=(3,)))


'''

'''
def add2(**kwData):
    print(f"Data -> {type(kwData)}, {kwData}")
    sum = 0
    print("Adding the datapoints -->", end='')
    for key, val in kwData.items():
        print(f"{key}[{val}]", end=' ')
    print()
    
    for val in kwData.values():
        sum += val

    return sum


print(add2(p = 1, q = 2, r = 3))

def add3(a, b, c):
    return a + b + c

lst = [1, 2, 3, 4]
print(add3(lst[0], lst[1], lst[2]))
print(add3(*lst))
'''
'''
lst = list()
a, b, c, *lst = 10, 20, 30, 40, 50
print(a, b, c, lst)
'''

def GenericFunc(a, b, *vArgs, **kwArgs):
    print(f"a[{a}], b[{b}], vArgs[{vArgs}], kwArgs[{kwArgs}]")

GenericFunc(1, 2)
GenericFunc(1, 2, 3)
GenericFunc(1, 2, 3, 4, 5)
GenericFunc(1, 2, 3, 4, 5, d1 = 6, d2 = 7)
GenericFunc(1, 2, d1 = 3, d2 = 4)
# GenericFunc(1, 2, d1 = 3, d2 = 4, 5, 6)  # ERROR: Pos args after KW args
# Func(PosArgs, /, Either, *, KwArgs)
