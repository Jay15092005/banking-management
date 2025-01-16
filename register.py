#User Registration SignIn And SignUp
import streamlit as st
import random
from database import *
from customer import *
from Bank import *

def db_query(str):
    cursor.execute(str)
    result=cursor.fetchall()
    return result
def SignUp():
    st.title("Sign Up")
    
    # Input fields for registration
    username = st.text_input("Enter Username").lower()
    password = st.text_input("Enter Password", type="password")
    name = st.text_input("Enter Name")
    age = st.number_input("Enter Age", min_value=1, max_value=120, step=1, format="%d")
    cities = ['Ahmedabad', 'Amreli', 'Anand', 'Bhavnagar', 'Bhuj', 'Bharuch', 'Botad', 'Deesa', 
 'Gandhidham', 'Gandhinagar', 'Godhra', 'Gondal', 'Himmatnagar', 'Jetpur', 'Jamnagar', 
 'Junagadh', 'Kalol', 'Mehsana', 'Morbi', 'Navsari', 'Nadiad', 'Palanpur', 'Porbandar', 
 'Rajkot', 'Surat', 'Surendranagar', 'Vadodara', 'Valsad', 'Vapi', 'Veraval']


    city = st.selectbox("Select a City", cities)
    balance = 0

    # Randomly generate account number
    account_no = random.randint(1000000000, 9999999999)
    while True:
        temp = db_query(f'SELECT * FROM customers WHERE account_no="{account_no}";')
        if temp:
            account_no = random.randint(1000000000, 9999999999)
        else:
            break
    
    status = True

    # Validation: Check if all fields are filled in
    all_fields_filled = username and password and name and city and age > 0

    # Button to register user (disabled until all fields are filled)
    if all_fields_filled:
        if st.button("Register"):
            temp = db_query(f'SELECT * FROM customers WHERE username="{username}";')
            if temp:
                st.error("Username already exists. Please try a different username.")
            else:
                # Create customer and add to database
                customer = Customer(username, password, name, age, city, balance, account_no, status)
                customer.CreateUser()

                # Create transaction table for the user
                bank = Bank(username, password)
                bank.Create_Transaction_Table()

                st.success(f"User Created Successfully! Your Account Number is {account_no}. Please Sign In.")
    else:
        # Show a message when not all fields are filled
        st.warning("Please fill in all the fields before submitting.")

def SignIn(username: str, password: str):
    # Query the database for username and password
    temp = db_query(f'SELECT * FROM customers WHERE username="{username}" AND password="{password}";')
    if temp:
        return username  # User successfully authenticated

    # Additional checks for incorrect username or password
    temp_username = db_query(f'SELECT * FROM customers WHERE username="{username}";')
    temp_password = db_query(f'SELECT * FROM customers WHERE password="{password}";')
    
    if not temp_username:
        return "Username is Incorrect"
    if not temp_password:
        return "Password is Incorrect"
    
    return None  # Generic failure case


