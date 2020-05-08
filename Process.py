import random
import string


main_option = input('''Welcome. To login select "A".
To Close App, select "B": ''').lower()

if main_option == "a":
    username = input("Enter username: ").lower()
    password = input("Enter password: ").lower()
    with open("staff.txt", "r") as staff:
        staff.seek(0)
        if str(username) and str(password) in staff.read():
            option1 = input('''To Create an Account, select "1".
            To Check Account Details, press "2".
            To Log out, press 3.''')
            if option1 == "1":
                account_name = input('''You"ve opted to create an account. 
                Enter account name: ''')
                opening_balance = int(input("Supply the opening balance: "))
                account_type = input("Account Type: ")
                account_email = input("Enter a valid and functional email address: ")
                account_number= "".join((random.choice(string.digits) for i in range (10)))
                print(f"Your Accont Number is" {account_number})
            elif 
        else:
            print("Invalid Login Details!")
else: