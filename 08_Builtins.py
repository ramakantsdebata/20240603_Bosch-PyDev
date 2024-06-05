# __builtin__ : Py-2 module that contains the built-in functions, exceptions and other objects provided by the interpreter
# builtins : Py-3 equivalent of __builtin__ from Py-2

# import builtins

def pow(a, b):
    print(f"{a} prisoners are now settled in {b} camps.")


def Test():
    # print(builtins.pow(4, 2))
    print(__builtins__.pow(4, 2))

Test()

