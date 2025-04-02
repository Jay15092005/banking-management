import streamlit as st
import os
from register import SignUp, SignIn, db_query
from Bank import AllTransactions

# Load configuration from Streamlit secrets
def load_config():
    # For deployment: use Streamlit secrets
    try:
        if hasattr(st, 'secrets'):
            if 'database' in st.secrets:
                return st.secrets
    except Exception as e:
        st.error(f"Error accessing secrets: {e}")
    
    # For local development: use default values
    return {
        "application": {"name": "Banking System"},
        "settings": {
            "session_timeout_minutes": 30,
            "default_deposit_limit": 100000,
            "default_withdrawal_limit": 50000
        },
        "ui": {"theme": "light", "primary_color": "#007bff"}
    }

# Load configuration
config = load_config()

def main():
    # Apply UI configuration if available
    try:
        if "ui" in config:
            ui_config = config["ui"]
            if "primary_color" in ui_config:
                primary_color = ui_config["primary_color"]
                st.markdown(f"""
                <style>
                .stButton button {{
                    background-color: {primary_color};
                    color: white;
                }}
                </style>
                """, unsafe_allow_html=True)
    except Exception as e:
        st.warning(f"Could not apply UI configuration: {e}")
        
    # Use application name from config
    try:
        app_name = config["application"]["name"] if "application" in config and "name" in config["application"] else "Banking System"
    except Exception:
        app_name = "Banking System"
        
    st.title(app_name)
    
    # Initialize session state for user login and selected action
    if "user" not in st.session_state:
        st.session_state.user = None
    if "selected_action" not in st.session_state:
        st.session_state.selected_action = None

    # If user is not logged in, show the login and sign-up options
    if st.session_state.user is None:
        st.subheader(f"Welcome to {app_name}")
        
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

        # Apply transaction limits from config if available
        try:
            deposit_limit = config["settings"].get("default_deposit_limit", 100000) if "settings" in config else 100000
            withdrawal_limit = config["settings"].get("default_withdrawal_limit", 50000) if "settings" in config else 50000
        except Exception:
            deposit_limit = 100000
            withdrawal_limit = 50000

        if choice == "Deposit":
            amount = st.number_input("Enter amount to deposit:", min_value=0, max_value=deposit_limit, format="%d")
            if amount and st.button("Deposit"):
                Helo.Deposit(amount)
        
        elif choice == "Withdraw":
            amount = st.number_input("Enter amount to withdraw:", min_value=0, max_value=withdrawal_limit, format="%d")
            if amount and st.button("Withdraw"):
                Helo.Withdraw(amount)
        
        elif choice == "Check Balance":
            if st.session_state.selected_action != "Check Balance":
                balance = Helo.CheckBalance()
        
        elif choice == "Transfer":
            recipient = st.text_input("Enter recipient's username:")
            amount = st.number_input("Enter amount to transfer:", min_value=1, max_value=withdrawal_limit, format="%d")
            if amount and recipient and st.button("Transfer"):
                Helo.Transfer(recipient, amount)
        
        elif choice == "Logout":
            st.session_state.user = None  # Reset session state
            st.session_state.selected_action = None
            st.info("You have been logged out.")
            st.rerun()  # Trigger rerun to show sign-in/signup options

if __name__ == "__main__":
    main()
