import mysql.connector as sql
connect=sql.connect(host='localhost',user='root',password='usingSQLisapain72',database='abc')
if connect.is_connected():
    print("successfully connected")
c=connect.cursor()
mn="CREATE TABLE RECORDS( account_no  INT(4) primary key,password INT(4),name VARCHAR(20),balance INT default(0))"
c.execute(mn)
print("Sucessfully created")
c.close()
