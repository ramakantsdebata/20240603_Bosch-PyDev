'''
def Baz():
    print("Baz")
    # res = 10/0
    raise TypeError("Some exception happened")
    # return -1
    print("Returning from Baz")

def Bar():
    print("Bar")
    try:
        Baz()
    except TypeError:
        print("Handling TypeError")
        # raise TypeError
        res = 10/0
    finally:
        # CleanupCode

    print("Returning from Bar")

def Foo():
    print("Foo")
    try:
        Bar()
        print("After Bar call.")
    except ZeroDivisionError:           # Raised exception is lowered
        print("Handling the ZeroDivisionError.")
    except Exception as ex:
        print(str(type(ex)), ex)

    print("Returning from Foo")

Foo()
'''
## Custom Exception ###################################

class CustomError(Exception):
    def __init__(self, message, code) -> None:
        self.message = message
        self.code = code
        super().__init__(self.message, self.code)

class InvalidAgeError(CustomError):
    def __init__(self, message, code) -> None:
        self.message = message
        self.code = code
        super().__init__(self.message, self.code)







## Consumer code ####################################

def checkAge(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative", 1001)
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older", 1002)
    
    print("Age is valid")


def Main():
    try:
        checkAge(-5)
    # except InvalidAgeError as ex:
    #     print(f"InvalidAgeError occured: {ex.message} (Error Code: {ex.code})")
    except CustomError as ex:
        print(f"CustomError occured: {ex.message} (Error Code: {ex.code})")

    try:
        checkAge(15)
    except InvalidAgeError as ex:
        print(f"InvalidAgeError occured: {ex.message} (Error Code: {ex.code})")
    except CustomError as ex:
        print(f"CustomError occured: {ex.message} (Error Code: {ex.code})")


Main()