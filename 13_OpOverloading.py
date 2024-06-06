class Integer:
    def __init__(self, value) -> None:
        self.val = int(value)

    def __str__(self) -> str:
        return str(self.val)
    
    def __add__(self, other):
        if isinstance(other, Integer):
            return Integer(self.val + other.val)
        
        try:
            return Integer(self.val + int(other))
        except (ValueError, TypeError) as ex:
            return NotImplemented
            # return str(type(ex)) + "  -->  " + str(ex)
        except Exception as ex:
            print("Unexpected Exception")

    

##########################################################


i1 = Integer(10)
i2 = Integer(20)

print(i1, i2)

i3 = Integer(0)

res = i1 + i2
print(type(res), res)

res = i1 + 1
print(type(res), res)

res = i1 + "2"
print(type(res), res)

res = i1 + "One"
print(type(res), res)
