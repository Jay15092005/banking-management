import mysql.connector as sql
import os
import streamlit as st

# Load configuration from Streamlit secrets
def load_config():
    # First try to use Streamlit secrets for deployment
    if hasattr(st, 'secrets') and 'database' in st.secrets:
        return {
            "database": {
                "host": st.secrets["database"]["host"],
                "user": st.secrets["database"]["user"],
                "password": st.secrets["database"]["password"],
                "name": st.secrets["database"]["name"]
            }
        }
    
    # For local development, fall back to .env file
    from dotenv import load_dotenv
    load_dotenv()
    return {
        "database": {
            "host": os.getenv("DB_HOST"),
            "user": os.getenv("DB_USER"),
            "password": os.getenv("DB_PASSWORD"),
            "name": os.getenv("DB_NAME")
        }
    }

# Load configuration
config = load_config()
db_config = config["database"]

def db_query(str):
    cursor.execute(str)
    result=cursor.fetchall()
    return result


# mydb=sql.connect(
#     host="127.0.0.1",
#     user="root",
#     passwd="",
#     database="Bank"
# )

mydb=sql.connect(
    host=db_config["host"],
    user=db_config["user"],
    passwd=db_config["password"],
    database=db_config["name"]
)

cursor=mydb.cursor()


def CreateCustomerTable():
    cursor.execute('''
               CREATE TABLE IF NOT EXISTS customers
               (Username VARCHAR(20),
               Password VARCHAR(20),
               Name VARCHAR(50),
               AGE INT,
               City VARCHAR(50),
               Balance BIGINT ,
               Account_no BIGINT,
               Status BOOLEAN)''')
 

mydb.commit()

if __name__ == "__main__":
    print("Database created successfully")
    CreateCustomerTable()
