
from datetime import datetime
import time
import pgeocode
import geocoder
g = geocoder.ip('me')
print(g.latlng)
country = 'india'
city_name="Anantapur"
place_name = "Tadipatri"
postal_code="515411"


userName = "Amarnath"
pin = 123456
balance= 0.00
account_no = str("xxxxxxxxxxxxxxx6008")
dep = 0.00
withdraw = 0.00

print("===============================")
c_name = input("Enter Username: ")
c_pin = int(input("Enter Pin Number: "))
print("-----------------------")
time.sleep(1)

if c_name.lower() != userName.lower() or c_pin != pin:
    print("Wrong password or username")
else:
    time.sleep(1)
    print(".........")
    time.sleep(0.5)
    print("You Have Successfully Login to your account")

print("------------------------------")
print("Your Balance is: {}".format(balance))
print("-" * 50)
print("""
            1. Deposit
            2. Withdraw
            3. Mini statement
            4. Pin change
            5. Exit
            """)

while True:
    ch = int(input("ENTER YOUR CHOICE: "))
    if ch == 1:
        dep = int(input("Enter Deposit Amount: "))
        balance += dep
        print("-"*25)
        print("After Deposit, your Bank Balance is Rs. : {}".format(balance))
        print("-"*25)
    elif ch == 2:
        withdraw = int(input("Enter how much amount you Withdraw: "))
        if withdraw>=balance:
            print("INSUFFICIENT BALANCE, YourBank Account of No Money is there")
        elif withdraw<300:
            print("you can't withdraw , minimum withdrawl balance is 300")
        else:
            balance = balance - withdraw
            print("-"*25)
            print("After withdraw, your Bank Balance is Rs. : {}".format(balance))
            print("-"*25)
    elif ch == 3:
        min_stat = input("Do you want to get mini statement: ")
        if min_stat.lower() == "yes":
            print("=" * 25, "Tadipatri Local Bank", "=" * 25)
            print(" "*10,"-" * 12, "Mini Statement", "-" * 12)
            print("Name:", userName," "*20,"Date:", datetime.now())
            print("Country:",country,"Palce:",place_name,"City:",city_name,"Pincode:",postal_code)
            print("Lattitude:",g,)
            print("Account Number:", account_no)
            # print("Date:", datetime.now())
            print("=" * 25)
            print("You Deposit Amount in Rs. :", dep)
            print("You Withdrawing amount in Rs. :", withdraw)
            print("-"*18)
            print("Current Balance in Rs. :", balance)
            print("-"*18)
        else:
            break
        print("-" * 25)
        print("Take your physical mini statement below print part")
        print("-"*25)
    elif ch == 4:
        pinc = input("Do you want to change your Pin Number: ")
        if pinc.lower() == "no":
            break
        elif pinc.lower() == "yes":
            new_pin = int(input("Enter your new Pin: "))
            print('*****************************')
            if new_pin != pin and len(str(new_pin)) == 6:
                print('------------------')
                print('******************')
                new_ppin = int(input('CONFIRM NEW PIN: '))
                print('*******************')
                print('-------------------')
                if new_ppin != new_pin:
                    print('------------')
                    print('************')
                    print('PIN MISMATCH')
                    print('************')
                    print('------------')
                else:
                    pin = new_pin
                    print('NEW PIN SAVED')
            else:
                print('-------------------------------------')
                print('*************************************')
                print('   NEW PIN MUST CONSIST OF 6 DIGITS \nAND MUST BE DIFFERENT FROM THE PREVIOUS PIN')
                print('*************************************')
                print('-------------------------------------')
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")
    elif ch == 5:
        break
    else:
        print("Invalid choice. Please choose a valid option.")

print("-" * 25)
print("" * 15, "Thank you for using our services", " " * 15)
print("-" * 25)


