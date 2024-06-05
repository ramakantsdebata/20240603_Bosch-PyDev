__all__ = ['greet', 'greetName', 'greetAskName']

def greet():
    '''
    A Simple function to greet someone
    '''
    print("Hi there!")

def greetName(Name):
    '''
    A Function which accepts a name 
    and provides a personalised greeting
    '''
    print(f"Hi {Name}!")

def greetAskName():
    '''
    Interactively greets person
    '''
    name = input("Enter your name: ")
    print(f"How are you doing, {name}?")

if __name__ == '__main__':
    greet()
    greetName("Manish")
    # greetAskName()
    print("\n", "="*20, "\n")


'''
def Test():
    greet()
    greetName("Manish")
    # greetAskName()
    print("\n", "="*20, "\n")

if __name__ == '__main__':
    Test()
'''
# print("__name__:", __name__)