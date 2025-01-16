import mysql.connector as sql

def db_query(str):
    cursor.execute(str)
    result=cursor.fetchall()
    return result


mydb=sql.connect(
    host="bank-management.mysql.database.azure.com",
    user="Jay1509",
    passwd="Chotaliya@1509",
    database="Bank"
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