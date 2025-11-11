'''1. Create a class “Programmer” for storing information of few programmers 
working at Microsoft.'''

class Programmer:
    company = "Microsoft"

    def __init__(self , name , age , contct , salary):
        self.Name = name
        self.age = age
        self.contact_no = contct
        self.salary = salary

print("Details of programer working in microsoft : \n")
Riku = Programmer("Riku",19,"riku@gmail",1500000)
print(Riku.Name,Riku.age,Riku.contact_no,Riku.salary,Riku.company,"\n")

subham = Programmer("suv",19,"suv@gmail",1000000)
print(subham.Name,subham.age,subham.contact_no,subham.salary,subham.company,"\n")

aadu = Programmer("aadu",19,"aasu@gmail",900000)
print(aadu.Name,aadu.age,aadu.contact_no,aadu.salary,aadu.company,"\n")
        
