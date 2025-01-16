#Customer detail
from database import *
class Customer:
    def __init__(self,username , password , name , age , city ,balance, account_no , status):
        self.__username=username
        self.__password=password
        self.__name=name
        self.__age=age
        self.__city=city
        self.__balance=balance
        self.__account_no=account_no
        self.__status=status
        
        
    def  CreateUser(self):
        db_query(f"INSERT INTO customers VALUES('{self.__username}','{self.__password}','{self.__name}',{self.__age},'{self.__city}',{self.__balance},{self.__account_no},{self.__status});")
        mydb.commit()
        print("User Created Successfully")