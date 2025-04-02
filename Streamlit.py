import streamlit as st
from register import SignUp, SignIn, db_query
from Bank import AllTransactions

def main():
    st.title("Banking System")
    
    # Initialize session state for user login and selected action
    if "user" not in st.session_state:
        st.session_state.user = None
    if "selected_action" not in st.session_state:
        st.session_state.selected_action = None

    # If user is not logged in, show the login and sign-up options
    if st.session_state.user is None:
        st.subheader("Welcome to the Banking System")
        
        # Authentication section
        action = st.sidebar.selectbox("Choose Action", ["Sign Up", "Sign In"])

        if action == "Sign Up":
            SignUp()  # Call the SignUp function
        elif action == "Sign In":
            st.title("Sign In")
            
            # Input fields for username and password
            username = st.text_input("Enter Username:")
            password = st.text_input("Enter Password:", type="password")
            
            # Validate if both fields are filled
            if not username or not password:
                st.warning("Please enter both username and password.")
            else:
                # Button to trigger login
                if st.button("Login"):
                    # Call the SignIn function
                    result = SignIn(username, password)
        
                    if result == username:
                        # Successful login
                        st.session_state.user = username  # Store logged-in user in session
                        st.success(f"Welcome {username}!")
                        st.session_state.selected_action = None  # Reset selected action
                        st.rerun()  # Trigger rerun to show banking options
                    elif result == "Username is Incorrect":
                        st.error("Invalid Username.")
                    elif result == "Password is Incorrect":
                        st.error("Invalid Password.")
                    else:
                        st.error("Login failed. Please check your credentials.")
        
    # If user is logged in, show the dashboard with banking options
    if st.session_state.user:
        st.subheader(f"Welcome {st.session_state.user}")
        options = ["Deposit", "Withdraw", "Check Balance", "Transfer", "Logout"]
        choice = st.selectbox("Choose an option:", options, key="action_select")
        
        # Instance of AllTransactions for the logged-in user
        Helo = AllTransactions(st.session_state.user)

        if choice == "Deposit":
            amount = st.number_input("Enter amount to deposit:", min_value=0, format="%d")  # Ensures integer input
            if amount and st.button("Deposit"):
                Helo.Deposit(amount)
        
        elif choice == "Withdraw":
            amount = st.number_input("Enter amount to withdraw:", min_value=0, format="%d")  # Ensures integer input
            if amount and st.button("Withdraw"):
                Helo.Withdraw(amount)
        
        elif choice == "Check Balance":
            if st.session_state.selected_action != "Check Balance":
                balance = Helo.CheckBalance()
        
        elif choice == "Transfer":
            recipient = st.text_input("Enter recipient's username:")
            amount = st.number_input("Enter amount to transfer:", min_value=1, format="%d")  # Ensures integer input
            if amount and recipient and st.button("Transfer"):
                Helo.Transfer(recipient, amount)
        
        elif choice == "Logout":
            st.session_state.user = None  # Reset session state
            st.session_state.selected_action = None
            st.info("You have been logged out.")
            st.rerun()  # Trigger rerun to show sign-in/signup options

if __name__ == "__main__":
    main()
