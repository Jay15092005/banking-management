import mysql.connector as sql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

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
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    passwd=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
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
