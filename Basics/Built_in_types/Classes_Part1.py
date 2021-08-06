class FirstClass: # Define a class object
    def setdata(self, value): # Define class's methods
        self.data = value # self is the instance
    def display(self):
        print(self.data)

x = FirstClass()
y = FirstClass()

x.setdata("Gowtham Ram")
y.setdata(1996)

#displays respective resutls
x.display()
y.display()

#Printing the above instances
#None Data will be presented because of second print statement.
#First is inside function and second is outside function. When a function doesn't return anything, it implicitly returns None.
print(x.display())
print(y.display())
