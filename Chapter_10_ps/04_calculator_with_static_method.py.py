'''4. Add a static method in problem 2, to greet the user with hello. '''
'''2. Write a class “Calculator” capable of finding square, cube and square root of a 
number. '''

class Calculator:
    n=8

    def square(self,n): # method
        # self.n = n
        print(f"Square of a number is {self.n*self.n}") # here n = 8 is work


    def cube(self,n):
        self.n = n
        print(f"Cube of a number is {self.n*self.n*self.n}")


    def square_root(self,n):
        # here self.n = n it is not work when we comment or not bcz cube method break the rule.
        #in def cube change the class attribute to insance attribute value that reason
        # self.n = n
        print(f"Square root of a number is {(self.n)**(1/2)}")

    @staticmethod
    def hello():
        print("Hello there!")



n = int(input("Enter a number : "))

no = Calculator() # object

no.hello()
no.square(n) # calling a method
no.cube(n)
no.square_root(n)