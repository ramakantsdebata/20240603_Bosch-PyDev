from multipledispatch import dispatch

@dispatch(int, int)
def add(a, b):
    return a + b


@dispatch(int, int, float)
def add(a, b, c):
    print("(int, int, float)")
    return a + b + c

@dispatch(int, float, int)
def add(a, b, c):
    print("(int, float, int)")
    return a + b + c

print(add(1, 2))
print(add(1, 2, 3.0))
print(add(1, 2.0, 3))

