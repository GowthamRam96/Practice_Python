class Number:
    def __init__(self, start): # On Number(start)
        self.data = start
    def __sub__(self, other): # On instance - other
        return Number(self.data - other) # Result is a new instance

X = Number(5)
Y = X-2
print(Y.data)
#Results
#3
#Notes
'''
__init__ used to initialize the newly created instance object using any arguments passed to
the class name.

__sub__ method plays the binary operator role.
'''
