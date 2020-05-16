# This code is written to ensure that whatever details entered
# are of the standard format. This includes the prompts required
# to take certain actions, valid staff log in details, 
# integer where digits are required, savings and current
# where account type is required, valid email etc.
# If I may be so immodest, I would say appropriate measures
# were taken to make the code totally bug free.

from email_validator import validate_email, EmailNotValidError
import os
import random
import re
import string


# Making the email and main_option variables global to enable their use
# in different functions throughout the code.
account_email = " "
main_option = " "

# Ensuring correct username is used.
def valid_username(instruction):
    staff = open("staff.txt", "r")
    while True:
        try:
            staff = input(instruction)
            find1 = re.match(r"neptune109", str(staff))
            if find1.group(0):
                pass
        except AttributeError:
            print("This username does not exist. Try again.")
        else:
            return staff
            staff.close()
            break

# Ensuring correct password is used.
def valid_password(instruction):
    staff = open("staff.txt", "r")
    while True:
        try:
            staff = input(instruction)
            find2 = re.match(r"asterisk", str(staff))
            if find2.group(0):
                pass
        except AttributeError:
            print("Wrong password for username entered. Try again.")
        else:
            return staff
            staff.close()
            break


# Function to create staff details in staff.txt file
def create_staff_details():
    with open("staff.txt", "w") as staff:
        staff.write("STAFF ONE")
        staff.write("\nUsername: neptune109")
        staff.write("\nPassword: asterisk")
        staff.write("\nEmail: johndoe@gmail.com")
        staff.write("\nFull Name: John Doe")

        staff.write("\n")
        staff.write("\nSTAFF TWO")
        staff.write("\nUsername: uranus487")
        staff.write("\nPassword: asteroid")
        staff.write("\nEmail: janedoe@gmail.com")
        staff.write("\nFull Name: Jane Doe")


# Ensuring digits are entered for account number and opening balance.
def digit_validation(instructions):
    
    while True:
        
        try:
            entry = int(input(instructions))
        
        except ValueError:
            print("Entry error! Please enter digits.")
        
        else:
            return entry
            break


# Ensuring only valid email address is entered.
def email_validation():

    global account_email
    
    while True:
        
        error_message = "Email format is invalid. Check and try again."
        account_email = input("Enter a Valid and Functional Email Address: ")
        
        try:
            enter_email = validate_email(account_email, allow_smtputf8=False, check_deliverability=False)
            break

        except EmailNotValidError as error_message:
            print(error_message)
    
    return enter_email


# Ensuring valid account type is entered.
def account_type_validation():
    
    while True:
        
        account_type = input("Account Type: ").lower()
        
        if account_type == "savings":
            break
        
        elif account_type == "current":
            break
        
        else:
            print('''Error! Account Type must either be "Savings" or "Current".''')
    
    return account_type


# Enables staff create account.
def create_account():

    global account_email
    account_name = input('''\nYou've opted to Create an Account. Proceed below. 
Enter Account Name: ''')
    
    opening_balance = digit_validation('''Enter Opening Balance(Naira): ''')
    
    # Calling the account_type_validation function which
    # collects account type and also validates before accepting.
    account_type = account_type_validation()
    
    # Calling the email_validator function which collects email
    # and also validates before accepting.         
    enter_email = email_validation()
    
    # Generating 10 digit account number.
    num = "".join((random.choice(string.digits) for i in range (10)))
    account_number = num
    
    with open ("customer.txt", "a+") as customer_details:
        
        customer_details.write("\nAccount Name: " + account_name)
        customer_details.write("\nOpening Balance: " + str(opening_balance))
        customer_details.write("\nAccount Type: " + account_type)
        customer_details.write("\nAccount Email: " + account_email)
        customer_details.write("\nAccount Number: " + account_number)
        customer_details.write('''
        \n''') 
               
    print("\nAccount has been created. \nAccount Number is " + account_number + ".")
    

# Enables Staff check customer's account details.    
def check_account_details():
    
    while True:
        
        check_details = digit_validation('''\nYou've opted to Check Account Details.
Enter the Account Number for which details are sought to proceed: ''')
        customer_details = open("customer.txt", "r")
        (customer_details).seek(0)
        database = customer_details.read()

        if str(check_details) in database:
            customer_details = open("customer.txt", "r")
            print("\nHere are the customer's details: \n" + customer_details.read())
            break
        
        else:
            print("The account number entered does not exist. Check and try again.")
            customer_details.close()


# Allows Staff to log out. Also deletes
# User session file. 
def log_out():
    user_session = open("session.txt", "w")
    user_session.truncate(0)
    user_session.close()
    if os.path.exists("session.txt"):
        os.remove("session.txt")
    else:
        print("The file does not exist")
    
    print("You've been Logged Out.")


# Houses actions Staff would take on logging in.
def actions():
    
    actions = True
    while True:
        
        option = input('''\nSelect an Action.
To Create an Account, select "C".
To Check Account Details, select "D".
To Log out, select "E".\n''').lower()

        if option == "c":
            create_account()
        
        elif option == "d":
            check_account_details()
           
        elif option == "e":
            log_out()
            break
            
        else:
            
            while True:
                
                print('''\nInvalid Entry. Try again.''')
                break
                
                if option == "c":
                    create_account()
                    break
                
                elif option == "d":
                    check_account_details()
                    break
            
                elif option == "e":
                    log_out()
                    break
                break


# Function which ensures the right option is enetered
# on opening app.
def main_option_validation():

    global main_option
    while True:
           
            print('''Invalid Entry. Please enter an appropriate letter.''')
            break
            
            if main_option == "a":
                username = input("Enter username: ").lower()
                password = input("Enter password: ").lower()
            
            elif main_option == "b":
                print("Have a lovely day. \nApp CLOSED.")
                main_option = False
                break     


# Beginning of execution.
main_option = True

# Calling the function which creates Staff details in staff.txt file.
create_staff_details()
        
while True:

    main_option = input('''\nWelcome to the Start Page. 
For Staff Log In, select "A".
To Close App, select "B": ''').lower()

    if main_option == "a":
        
        print("\nEnter log in details below to continue.")
        
        # Calling the username and password validation functions.
        username = valid_username("Enter username: ")
        password = valid_password("Enter password: ")

        # Creating a file to store user session.
        user_session = open("session.txt", "w+")
        user_session.close()        
        
        option = True
        while True:
            
            # Calling the functions which allows staff
            # take different actions.
            actions()
            break

    elif main_option == "b":
        print("Have a lovely day. \nApp CLOSED.")
        break
    
    # Ensuring the right letter is entered when app is opened.
    else:
        main_option_validation()
