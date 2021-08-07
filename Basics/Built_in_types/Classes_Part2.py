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
