class Employee: # class
    langauge ="Python" # class Attributes
    salary = 1200000

    #It takes ‘self’ argument and can also take further arguments
    def __init__(self,name , salary , langauge): # dunder method which is called autometically.
        self.name = name
        self.salary = salary
        self.langauge = langauge
        print("I am creating a object .")




# Riku = Employee() # Constructor to call  auto ->def __init__(self):
Riku = Employee("Riku",1200000,"Python") # Constructor
print(Riku.name, Riku.salary, Riku.langauge)

Roshan = Employee("Roshan",110000,"Java Script")
print(Roshan.name, Roshan.salary, Roshan.langauge)