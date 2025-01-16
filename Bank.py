#For Bank Services
from database import *
from customer import *
from datetime import datetime

import streamlit as st
class Bank:
    def __init__(self,username,password):
        self.__username=username
        self.__password=password
        pass
    
    def Create_Transaction_Table(self):
        cursor.execute(f'''
                       CREATE TABLE IF NOT EXISTS {self.__username}transactions
                       (Username VARCHAR(20),
                       Balance BIGINT,
                       Transaction_type VARCHAR(10),
                       Date DATE)''')
        cursor.execute(f'''INSERT INTO {self.__username}transactions VALUES('{self.__username}',0,'Created',CURDATE())''')
        mydb.commit()
import streamlit as st

class AllTransactions:
    def __init__(self, username):
        self.__username = username

    def CheckBalance(self):
        # Query the balance for the current user
        temp = db_query(f'SELECT Balance FROM customers WHERE username="{self.__username}";')
        balance = temp[0][0] if temp else 0
        return st.success(f"Your current balance is: {balance}")

    def Deposit(self, amount):
        # Fetch the current balance
        temp = db_query(f'SELECT Balance FROM customers WHERE username="{self.__username}";')
        balance = temp[0][0] if temp else 0

        # Update balance
        balance += amount
        db_query(f'UPDATE customers SET Balance={balance} WHERE username="{self.__username}";')
        db_query(f'INSERT INTO {self.__username}transactions VALUES("{self.__username}", {amount}, "Deposit", CURDATE())')
        mydb.commit()

        return st.success(f"Deposited {amount}. Your current balance is: {balance}")

    def Withdraw(self, amount):
        # Fetch the current balance
        temp = db_query(f'SELECT Balance FROM customers WHERE username="{self.__username}";')
        balance = temp[0][0] if temp else 0

        if balance >= amount:
            # Update balance
            balance -= amount
            db_query(f'UPDATE customers SET Balance={balance} WHERE username="{self.__username}";')
            db_query(f'INSERT INTO {self.__username}transactions VALUES("{self.__username}", {amount}, "Withdraw", CURDATE())')
            mydb.commit()
            return st.success(f"Withdrew {amount}. Your current balance is: {balance}")
        else:
            return st.error("Insufficient Balance.")

    def Transfer(self, recipient, amount):
        # Check if recipient exists
        recipient_exists = db_query(f'SELECT * FROM customers WHERE username="{recipient}";')
        if not recipient_exists:
            return False, st.error("Recipient does not exist.")

        # Fetch the current user's balance
        temp = db_query(f'SELECT Balance FROM customers WHERE username="{self.__username}";')
        balance = temp[0][0] if temp else 0

        if balance >= amount:
            # Deduct from sender
            balance -= amount
            db_query(f'UPDATE customers SET Balance={balance} WHERE username="{self.__username}";')
            db_query(f'INSERT INTO {self.__username}transactions VALUES("{self.__username}", {amount}, "Transfer", CURDATE())')

            # Add to recipient
            temp = db_query(f'SELECT Balance FROM customers WHERE username="{recipient}";')
            recipient_balance = temp[0][0] if temp else 0
            recipient_balance += amount
            db_query(f'UPDATE customers SET Balance={recipient_balance} WHERE username="{recipient}";')
            db_query(f'INSERT INTO {recipient}transactions VALUES("{recipient}", {amount}, "Transfer", CURDATE())')
            mydb.commit()
            return True, st.success(f"Transferred {amount} to {recipient}. Your current balance is: {balance}")
        else:
            return False, st.error("Insufficient Balance.")
