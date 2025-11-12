'''6. Can you change the self-parameter inside a class to something else (say 
“harry”). Try changing self to “slf” or “harry” and see the effects. '''
# Yes we can change , Nothing is change.


from random import randint # use of from keyword.

class Train :
    def __init__(slf,train_no):
        slf.train_no = train_no

    def book_ticket(harry, fro, to):
        print(f"Ticked is booked in train no: {harry.train_no} from {fro} to {to}.")

    def get_status(Riku):
        print(f"Train no: {Riku.train_no} is running in time.")

    def get_fare(self, fro, to):
        print(f"Ticked fare in train no: {self.train_no} from {fro} to {to} is {randint(60,1100)}")

t = Train(19005)
t.book_ticket("Barpali","Kesinga")
t.get_status()
t.get_fare("Barpali","Kesinga")