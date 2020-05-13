import random
import string


constant = int(309)
num1 = "".join((random.choice(string.digits) for i in range (7)))
account_number = (str(constant) + num1)


def digit_validation(instructions):
    
    while True:
        try:
            entry = int(input(instructions))
        except ValueError:
            print("Entry error! Please enter digits.")
        else:
            return entry
            break

def create_account():

    global account_number
    account_name = input('''You've opted to create an account. Proceed below.\n 
Enter account name: ''')
    opening_balance = digit_validation('''Enter the opening balance(Naira): ''')
    account_type = input("Account Type: ")
    account_email = input("Enter a Valid and Functional Email Address: ")
    with open ("customer.txt", "w+") as customer_details:
        customer_details.write("Account Name: " + account_name)
        customer_details.seek(0)
        data = customer_details.read(100)
        if len(data) > 0:
            customer_details.write("\n")
            customer_details.write("Opening Balance: " + str(opening_balance))
            customer_details.write("\nAccount Type: " + account_type)
            customer_details.write("\nAccount Email: " + account_email)
            customer_details.write("\nAccount Number: " + account_number)
            print("\nAccount has been created. \nAccount Number is " + account_number + ".")
        else:
            print("Can't add customer details.")
    
    return account_number
    

def check_account_details():
    
    global account_number
    while True:
        check_details = digit_validation('''\nYou've opted to Check Account Details.
Enter the Account Number for which details are sought to proceed: ''')
        customer_details = open("customer.txt", "r")
        customer_details.seek(0)
        check = True
        while True:
            if check_details in str(customer_details.read()):
                customer_details = open("customer.txt", "r")
                print(
    '''Here are the customer's details: \n''' + customer_details.read())
                break
            else:
                print("The account number entered does not exist. Check and try again")
                break
                customer_details.close()


def log_out():
    
    customer_session = open("session.txt", "r+")
    customer_session.truncate(0)
    customer_session.close()
    
    print("You've been logged out.")

def option():
    option1 = input('''\nYou're logged in.
To Create an Account, select "C".
To Check Account Details, select "D".
To Log out, select "E".\n''').lower()
 
    return option1


def actions():
    option1 = option()
    if option1 == "c":
        create_account()
        
    elif option1 == "d":
        check_account_details()
        
    elif option1 == "e":
        log_out()
        
    else:
        while True:
            print('''Invalid Entry. Try again.''')
            option1 = input('''To Create an Account, select "C".
To Check Account Details, select "D".
To Log out, select "E".\n''')
            if option1 == "c":
                create_account()
                break
            
            elif option1 == "d":
                check_account_details()
                break
        
            elif option1 == "e":
                log_out()
                break



# Beginning of execution.
main_option = True

main_option = input('''Welcome to the Start Page. 
To Log In, select "A".
To Close App, select "B": ''').lower()
    
while True:

    
    if main_option == "a":
        
        print("\nEnter log in details below to continue.")
        user_session = open("session.txt", "w+")
        username = input("Enter username: ").lower()
        password = input("Enter password: ").lower()
        
        with open("staff.txt", "r") as staff:
            staff.seek(0)
            
            if str(username) and str(password) in staff.read():
                
                option1 = True
                while True:
                    actions()

            else:
                print("Incorrect log in details. Check and try again.")


    elif main_option == "b":
        print("Have a lovely day.")
        break


    else:
        
        while True:
           
            print('''Invalid Entry. Please enter an appropriate letter.''')
            break
            
            if main_option == "a":
                username = input("Enter username: ").lower()
                password = input("Enter password: ").lower()
            
            elif main_option == "b":
                print("Have a lovely day.")
                main_option = False
                break
            
