# Lambda - Anonymous Functions / Functions with no inherent name
'''
def Double(num):
    return 2 * num

def Square(num):
    return num**2

def Exponent(num):
    return 2**num

###############################

f1 = lambda num : 2* num
f2 = lambda num: num**2
f3 = lambda num: 2**num
'''

def Operate(num, Operation):
    return Operation(num)

print(Operate(5, lambda num : 2* num))
print(Operate(5, lambda num : num**2))
print(Operate(5, lambda num : 2**num))
print("Is Even?:", Operate(5, lambda num : num%2 == 0))
print("Next Even ->", Operate(6, lambda num : num+2 if num%2==0 else num+1))        # 'True clause'  if <coind> else 'False clause'


tools = {'Double': (lambda num : 2* num), 
         'Square': (lambda num : num**2), 
         'Exp': (lambda num : 2**num)}

print(tools['Double'](7))
