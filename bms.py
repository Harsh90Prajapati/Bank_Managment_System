import mysql.connector

mydb=mysql.connector.connect(
host='sql9.freemysqlhosting.net',
port=3306,
user='sql9581662',
password='b1lthKkcZx',
database='sql9581662'
)

def OpenAcc(name, accNo, dob, address, phone, balance):
    if accNo == "": return ("Account number cannot be blank!")
    if balance == "": return ("Balance cannot be blank!")
    data=(name,accNo,dob,address,phone,balance)
    query=('insert into BANK values(%s,%s,%s,%s,%s,%s)')
    cursor=mydb.cursor()

    try:
        cursor.execute(query, data)
        mydb.commit()
        return("success")
    except:
        return("An error occured while saving the data!")    

def Deposit(accNo, amount):  
    if accNo == "" : return ("Account number cannot be blank!")
    query='select Balance from BANK where `Account No`=%s'
    data=(accNo,)
    cursor=mydb.cursor()

    try:
        cursor.execute(query,data)
        balance=cursor.fetchone()
    except Exception as e:
        print(e)
        return("An error occured while finding the bank account!")

    totalAmount=balance[0]+int(amount)
    query=('update BANK set Balance=%s where `Account No`=%s')
    data=(totalAmount,accNo)
    try:
        cursor.execute(query, data)
        mydb.commit()
        return("success")
    except:
        return("An error occured while updating the balance!")

def Withdraw(accNo, amount):    
    if accNo == "" : return ("Account number cannot be blank!")
    query='select Balance from BANK where `Account No`=%s'
    data=(accNo,)
    cursor=mydb.cursor()

    try:
        cursor.execute(query,data)
        balance=cursor.fetchone()
        if balance[0] < int(amount):
            raise Exception("Not enough balance to withdraw said amount!")
    except:
        return("An error occured while finding the bank account!")

    totalAmount=balance[0]-int(amount)
    query=('update BANK set Balance=%s where `Account No`=%s')
    data=(totalAmount,accNo)
    try:
        cursor.execute(query, data)
        mydb.commit()
        return ("success")
    except:
        return("An error occured while updating the balance!")

def CheckBal(accNo):    
    if accNo == "" : return ("Account number cannot be blank!")
    query='select Balance from BANK where `Account No`=%s'
    data=(accNo,)
    cursor=mydb.cursor()

    try:
        cursor.execute(query,data)
        balance=cursor.fetchone()
        return [balance[0]]
    except:
        return("An error occured while finding the bank account!")

def GetCustomerData(accNo):    
    if accNo == "" : return ("Account number cannot be blank!")
    query = 'select * from BANK where `Account No`=%s'
    data = (accNo,)
    cursor = mydb.cursor ( )
    try:
        cursor.execute ( query , data )
        result = cursor.fetchall()
        return [result[0]]
    except:
        return ("An error occured while finding the bank account!")

def CloseAcc(accNo):    
    if accNo == "" : return ("Account number cannot be blank!")
    query = 'delete from BANK where `Account No`=%s'
    data = (accNo,)
    cursor = mydb.cursor()
    try:
        cursor.execute (query, data)
        mydb.commit()
        return ["success"]
    except:
        return ("An error occured while closing the account!")