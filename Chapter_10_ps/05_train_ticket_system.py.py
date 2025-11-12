'''5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
and get fare information of train running under Indian Railways. '''

# import random
from random import randint # use of from keyword.

class Train :
    def __init__(self,train_no):
        self.train_no = train_no

    def book_ticket(self, fro, to):
        print(f"Ticked is booked in train no: {self.train_no} from {fro} to {to}.")

    def get_status(self):
        print(f"Train no: {self.train_no} is running in time.")

    def get_fare(self, fro, to):
        print(f"Ticked fare in train no: {self.train_no} from {fro} to {to} is {randint(60,1100)}")

t = Train(19005)
t.book_ticket("Barpali","Kesinga")
t.get_status()
t.get_fare("Barpali","Kesinga")