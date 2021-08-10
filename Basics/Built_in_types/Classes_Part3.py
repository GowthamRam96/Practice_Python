class FirstClass: # Define a class object
    def setdata(self, value): # Define class's methods
        self.data = value # self is the instance
    def display(self):
        print(self.data)

class SecondClass(FirstClass): # Inherits setdata
    def display(self): # Changes display
        print('Current value = "%s"' % self.data)

S = SecondClass()
S.setdata("Overridden Class method by finding the setdata in FIRST CLASS")
S.display()

class ThirdClass(SecondClass): # Inherit from SecondClass
    def __init__(self, value): # On "ThirdClass(value)"
        self.data = value
    def __add__(self, other): # On "self + other"
        return ThirdClass(self.data + other)
    def __str__(self): # On "print(self)", "str()"
        return '[ThirdClass: %s]' % self.data
    def mul(self, other):  # In-place change: named
        self.data *= other

a = ThirdClass('abc') # __init__ called
a.display() # Inherited method called

print("------------------------------")

print(a) # __str__: returns display string

print("------------------------------")

b = a + 'xyz' # __add__: makes a new instance
b.display() # b has all ThirdClass methods

print("------------------------------")

print(b)

print("------------------------------")

a.mul(3) # mul: changes instance in place
print(a)

print("------------------------------")
