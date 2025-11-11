class Employee: # class
    langauge ="Python" # class Attributes
    salary = 1200000

    def getInfo(self): # Method
        print(f"The langauge is {self.langauge} . The salary is {self.salary}.")
    
    def greet(self):#we give self every method/function for run whenever we use that or not.
        print("Good Morning")

    @staticmethod # decorator to mark greet as a static method 
    def greet1():#when we use @staticmethod that time we are not pass self or full object details
        print("Have a nice day !!")

Riku = Employee() #Object
Riku.name = "Riku" # instance attributes
Riku.greet()
Riku.getInfo()
Riku.greet1()
# Employee.getInfo(Riku)
