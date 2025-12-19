# ATM application:

# 1fn : card verification
# 2fn : options : bal,withdrwal,deposit

# verification
# bal
# withdrawl
# deposit
# global, local


# 1. bal, 2. deposit, 3,withdrwal

balance = 100

def card_validation(card_number,pin): # card verification
    if card_number == '1234567':
        if pin == '4329':
            print("----- card is valid :) -----")
            options()
        else:
            print("Entered invalid pin")
    else:
        print('** Invalid card **')


def withdrawl():
    wamount = int(input('Enter withdrawl amount : '))
    global balance

    if wamount > balance:
        print(f'Insufficiant Funds Available')
        exit()
    else:
        balance = balance - wamount
        print(f'Remaining Amount : {balance}')


def deposit():
    damount = int(input('Enter deposit amount : '))
    global balance
    balance = balance + damount
    print(f'Remaining Amount : {balance}') 



def options(): # user options for atm fn's
    input_1 = int(input('Enter options : '))
    if input_1 == 1:
        print(f'Account balance {balance}')
        options()
    elif input_1 == 2:
        withdrawl()
        options()
    elif input_1 == 3:
        deposit()
        options()
    else:
        print('Transaction Completed, Please Remove Card !')
        exit()



info = """ Select below Options
option 1 for Balance
option 2 for Withdrawl
option 3 for Deposit
other than above option for Exit
"""
print(info)

card = '1234567'
pin = '4329'

card_validation(card,pin) # main fn for ATM
