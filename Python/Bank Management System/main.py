import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.load(fs)
        else:
            print("No such data exists")
    except Exception as err:
        print(f"An error occurred: {err}")

    @classmethod
    def __Update(cls):
        with open(cls.database, 'w') as fs:
            json.dump(cls.data, fs, indent=4)

    @classmethod
    def __accountGenerate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchr = random.choices("!@#$%^&*", k=1)
        id = alpha + num + spchr
        random.shuffle(id)
        return "".join(id)

    def CreateAccount(self):
        info = {
            "name": input("Tell your name: "),
            "age": int(input("Tell your age: ")),
            "email": input("Tell your email: "),
            "pin": int(input("Tell your 4-digit pin: ")),
            "accountNo": Bank.__accountGenerate(),
            "balance": 0
        }

        if info["age"] < 18 or len(str(info["pin"])) != 4:
            print("Sorry, you cannot create an account.")
        else:
            print("\n✅ Account created successfully!")
            for key, value in info.items():
                print(f"{key} : {value}")
            print("📌 Please note down your account details.\n")
            Bank.data.append(info)
            Bank.__Update()

    def DepositMoney(self):
        accNo = input("Enter your account number: ")
        pin = int(input("Enter your pin: "))

        userData = [i for i in Bank.data if i["accountNo"] == accNo and i["pin"] == pin]
        if not userData:
            print("❌ Sorry! No matching data found.")
        else:
            amount = int(input("Enter the amount you want to deposit: "))
            if amount > 10000 or amount <= 0:
                print("❌ Invalid amount to deposit.")
            else:
                userData[0]["balance"] += amount
                Bank.__Update()
                print("💰 Amount deposited successfully!")

    def WithdrawMoney(self):
        accNo = input("Enter your account number: ")
        pin = int(input("Enter your pin: "))

        userData = [i for i in Bank.data if i["accountNo"] == accNo and i["pin"] == pin]
        if not userData:
            print("❌ Sorry! No matching data found.")
        else:
            amount = int(input("Enter the amount you want to withdraw: "))
            if userData[0]["balance"] < amount:
                print("🚫 Insufficient balance.")
            else:
                userData[0]["balance"] -= amount
                Bank.__Update()
                print("💸 Amount withdrawn successfully!")

    def ShowDetails(self):
          accNo = input("Enter your account number: ")
          pin = int(input("Enter your pin: "))

          userData = [i for i in Bank.data if i["accountNo"] == accNo and i["pin"] == pin]
          print("Tour Account details are : ")
          for i in userData[0]:
              print(f"{i} : {userData[0][i]}")
          
    def UpdateDetails(self):
          accNo = input("Enter your account number: ")
          pin = int(input("Enter your pin: "))

          userData = [i for i in Bank.data if i["accountNo"] == accNo and i["pin"] == pin]

          if userData == False:
              print("No such user found")
          else:       
              print("You cannot change the account number , age and balance.")

              print("Fill details for change or leave it for no change")

              newData = {
                  "name": input("Please enter your updated name or press enter for no change"),
                  "email":input("Please enter your new email or press enter for no change"),
                  "pin":input("Please enter your new pin or press enter for no change")
              }
              if newData["name"] == "":
                  newData["name"] == userData[0]["name"]
              if newData["email"] == "":
                  newData["email"] == userData[0]["email"]
              if newData["pin"] == "":
                  newData["pin"] == userData[0]["pin"]        
              
              newData["age"] = userData[0]["age"] 
              newData["accountNo"] = userData[0]["accountNo"]
              newData["balance"] = userData[0]["balance"]

              if type(newData["pin"]) == str:
                  newData["pin"] = int(newData["pin"])

              for i in newData:
                  if newData[i] == userData[0][i]:
                      continue
                  else:
                      userData[0][i] = newData[i] 

              Bank.__Update()
              print("Details have been updated successfully!")           
    def DeleteAccount(self):
        accNo = input("Enter your account number: ")
        pin = int(input("Enter your pin: "))

        userData = [i for i in Bank.data if i["accountNo"] == accNo and i["pin"] == pin]

        if userData == False:
            print("No such data exists")
        else:
            check = input("Press y if you want to delete account or else n : ")
            if check == 'n' or 'N':
                print("Bypassed!")
            else:
                index = Bank.data.index(userData[0])
                Bank.data.pop(index)
                print("Your account has een deleted successfully!")
                Bank.__Update()        
        

user = Bank()

print("\n--- Bank System Menu ---")
print("1. Create Account")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. View Account Details")
print("5. Update Account Details")
print("6. Delete Account")

check = int(input("Enter your choice (1-6): "))
if check == 1:
    user.CreateAccount()
elif check == 2:
    user.DepositMoney()
elif check == 3:
    user.WithdrawMoney()
elif check == 4:
    user.ShowDetails()
elif check == 5:
    user.UpdateDetails()
elif check == 6:
    user.DeleteAccount()
else:
    print("❌ Invalid selection.")


