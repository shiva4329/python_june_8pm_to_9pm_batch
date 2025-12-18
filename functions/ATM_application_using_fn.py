# ATM application:

# 1fn : card verification
# 2fn : options : bal,withdrwal,deposit

# verification
# bal
# withdrawl
# deposit
# global, local


# 1. bal, 2. deposit, 3,withdrwal

def bal(): # checking balance
    balance = 100
    print(f"Accout balance : {balance}")

def card_validation(card_number,pin): # card verification
    if card_number == '1234567':
        if pin == '4329':
            print("card is valid")
            input_1 = int(input("Enter options :"))
            options(input_1)
        else:
            print("Entered invalid pin")
    else:
        print('Invalid card')


def options(input_1): # user options for atm fn's
    if input_1 == 1:
        bal()


card = '1234567'
pin = '4329'
card_validation(card,pin) # main fn for ATM
