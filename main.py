from register import *
from Bank import *


while True:
    try:
        register=int(input("1. Sign Up\n2. Sign In\n"))
        if register==1 or register ==2 :
            if register == 1:
                SignUp()
                user=SignIn()
                Helo=AllTransactions(user)
                
                break
            elif register == 2:
                user=SignIn()
                Helo=AllTransactions(user)
                print("It's Value Of Helo",Helo)
                break
        else:
            print("Invalid Input Try Again")
            continue 
    except ValueError:
        print("Invalid Input Try Again With Numbers")
        continue
            
            
while True:
    facility=int(input("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Transfer\n5. Logout\n"))
    
    
    if facility==1:
        amount=int(input("Enter Amount To Deposit: "))
        Helo.Deposit(amount)
    elif facility==2:
        amount=int(input("Enter Amount To Withdraw: "))
        Helo.Withdraw(amount)
    elif facility==3:
        Helo.CheckBalance()
    elif facility==4:
        username=input("Enter Username To Transfer: ")
        Helo.Transfer()
    elif facility==5:
        print("Logged Out")
        break
    else:
        print("Invalid Input Try Again")
        continue
    
