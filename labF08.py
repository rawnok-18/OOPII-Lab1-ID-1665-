try:
  print(x)
except:
  print("An exception occurred")
  
  
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
  
  
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
  
  
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
  
  
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")
  

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")
  
  
values = [10,20,30,0]
divisor = int(input())
try:
    for i in values:
        result = i/divisor
        print(result)
except ZeroDivisionError:
    print(" value divided by zero")
except ValueError:
    print("Value error")
except TypeError:
    print("Type error")
except ValueError:
    print("Value error")
except TypeError:
    print("Type error")
except arithmeticError:
    print("Arithmetic error")
except:
    print("Error Occured")
finally:
    print("Done working with")
    
 
class InsufficientBalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def withdraw(self,amount):
        if self.balance<amount:
            raise InsufficientBalanceException
        else:
            self.balance -= amount
            print("Transaction successful")
ob = BankAccount(100)
try:
    amount = int(input("Enter amount: "))
    ob.withdraw(amount)
except InsufficientBalanceException:
    print("Rafi is a Hablu")
except:
    print("Errors Occured")
finally:
    print("Take Love Dear")

  
  
  
  
  
  
  
  
  
  
