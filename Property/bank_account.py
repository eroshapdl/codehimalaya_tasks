#accessing bank acc balance with getter, setter and using deleter

class BankAccount:
    def __init__ (self, name, balance):
        self.name = name
        self._balance =  balance
    
    # Getter for balance
    @property
    def balance(self):
        return self._balance
    
    # Setter for balance with validation
    @balance.setter
    def balance(self, value):
        if value < 0:
            print ("balance cant be negative")
            return None
        self._balance = value
        return value
    
    # Deleter for balance 
    @balance.deleter
    def balance(self):
        print("Account has been deleted")
        del self._balance

    # Property for account
    @property
    def description (self):
        details = {
            "name": self.name,
            "balance": self._balance

        }
        
        return details

acc1 = BankAccount ("er", 500)
print (acc1.description) # Accessing account details via property
acc1.balance = 1000 # Setting a new balance
print (acc1.description)
acc1.balance = -400 #setting negative balance

del acc1.balance #deletes account
