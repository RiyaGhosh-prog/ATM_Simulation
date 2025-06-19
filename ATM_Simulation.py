#ATM Class Defination
class ATM:
    #Constructor to initialize accoumt with PIN, balance and transaction History
    def __init__(self, pin):  
        self.balance = 0.0      #initial balance
        self.pin = pin          #user PIN
        self.transaction = []   #List to store transaction history

    # method to verify if entered PIN is correct
    def verify_pin(self):
        pin = int(input("Enter PIN: "))  
        if pin == self.pin:
            return True
        else:
            print("Wrong PIN")
            return False
        
    # method to display current balance    
    def check_balance(self):
        print(f"current Balance: {self.balance}")   

    # method to deposit amount into account
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount} successfully. Balance: {self.balance}")
            self.transaction.append(f"Deposited{amount}")
        else:
              print("Enter a valid amount.")
            
    # method to withdraw amount from account
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}. Balance: {self.balance}")
            self.transaction.append(f"withdrawn {amount}")
        else:
            print("Insufficient balance or invalid amount.")
    # method to change the current PIN
    def pin_change(self):
        old_pin = int(input("Enter old PIN: "))
        if old_pin == self.pin:
            new_pin = int(input("Enter new PIN: ")) 
            confirm_pin = int(input("Enter confirm pin: "))
            if new_pin == confirm_pin and len(str(new_pin))==4:
                self.pin = new_pin
                print("Successfully PIN changed.")
                self.transaction.append("PIN changed")
            else:
                print("PIN didn't match.please enter 4-digit")          
        else:
            print("incorrect old PIN")

    # method to dispaly the transaction history 
    def transaction_history(self):
        if self.transaction:
            print("Transaction History: ")
            for trans in self.transaction:
                print(trans)
        else:
            print("No transaction yet")

# Main function to intract with the ATM
def main():
    pin = int(input("Enter your 4-digit PIN:  "))
    account = ATM(pin)
    if not account.verify_pin():
        print("Access Denied")
        return
    
    # Menu-driven interface
    while True:
      print("\n---- Choose action ----")
      print("1. Balance Enquiry")
      print("2. Withdraw")
      print("3. Deposite")
      print("4. PIN change")
      print("5. Transaction History")
      print("6. Exit")
    
      
      choice =int(input("Enter your choice....: "))
    
      if choice == 1:
          account.check_balance()
      elif choice == 2:
          account.withdraw(float(input("Enter amount: ")))
      elif choice == 3:
          account.deposit(float(input("Enter amount: ")))
      elif choice== 4:
          account.pin_change()
      elif choice == 5:
          account.transaction_history()
      elif choice == 6:
          print("Thank you for visiting!")
          break
      else:
        print("Please enter the valid input.......")

 # This must also be outside the class and not indented.
if __name__ == "__main__":
    main()
        
