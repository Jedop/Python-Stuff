import mysql.connector as sql
connect=sql.connect(host='localhost',user='root',password='usingSQLisapain72',database='  abc')
cur=connect.cursor()
while True:
    p=""
    a=str(input('''==================================
Welcome to Weirdbank! What would you like to do-
1.Login
2.Register
3.Exit
==================================
-'''))
    a.lower()
    while a not in ("1","2","3","login","register","exit"):
        a=str(input('''==================================
Welcome to Weirdbank! What would you like to do-
1.Login
2.Register
3.Exit
==================================
-'''))
    while True:
        if p=="f":
            break
        m="no"
        if a in ("3","exit"):
            print("See you soon!")
            break
        elif a in ("2","register"):
            b=int(input("Create an account number(Maximum 4 digits)-"))
            l="select account_no from records"
            cur.execute(l)
            data=cur.fetchall()
            for i in data:
                if b==i[0]:
                    print("This account number already exists! Redirecting you to start!")
                    m="oh"                        
                    break
            if m=="oh":
                break
            c=int(input("Create pin(Maximum 4 digits)-"))
            d=str(input("Enter your name-"))
            lol="insert into records(account_no, password, name) values({},{},'{}')".format(b,c,d)
            cur.execute(lol)
            print("Account has been created!")
            connect.commit()
        e=int(input("Enter account number-"))
        cur.execute("select * from records")
        data=cur.fetchall()
        while True:
            for row in data:
                if e==row[0]:
                    f=int(input("Enter pin!"))
                    if e==row[1]:
                        print("Correct pin! You are logged in")
                        n="o"
                    else:
                        e=int(input("Incorrect pin! Try again!-"))
            if n=="o":
                break
        accountno=row[0]
        while True:
            f=str(input('''==================================
Hello! What would you like to do!"
1-Withdrawal
2-Deposit
3-Check balance
4-Change pin
5-Logout
==================================
-'''))
            f.lower()
            while f not in ("1","2","3","4","5","withdrawal","deposit","check balance","change password","logout"):
                f=str(input('''==================================
Incorrect input! Try again! What would you like to do!"
1-Withdrawal
2-Deposit
3-Check balance
4-Change password
5-Logout
==================================
-'''))
                f.lower()
            if f in ("1","withdrawal"):
                g=int(input("Enter amount of money to be withdrawn!"))
                cur.execute("select balance from records where account_no={}".format(accountno))
                data=cur.fetchall()
                h=data[0]
                while h[0]<g:
                    g=int(input("Not enough money. Current balance is"+str(h[0])))
                print("amount has been withdrawn! Current balance is",h[0]-g)
                st="update records set balance={} where account_no={}".format(h[0]-g,accountno)
                cur.execute(st)
                connect.commit()
            elif f in ("2","deposit"):
                g=int(input("Enter amount of money to be deposited!"))
                cur.execute("select balance from records where account_no={}".format(accountno))
                data=cur.fetchall()
                h=data[0]
                st="update records set balance={} where account_no={}".format(h[0]+g,accountno)
                cur.execute(st)
                connect.commit()
            elif f in ("3","check balance"):
                cur.execute("select balance from records where account_no={}".format(accountno))
                data=cur.fetchall()
                h=data[0]
                print("Your balance is",h[0])
            elif f in ("4","change pin"):
                cur.execute("select password from records where account_no={}".format(accountno))
                data=cur.fetchall()
                h=data[0]
                g=int(input("Enter new pin-"))
                st="update records set password={} where account_no={}".format(g,accountno)
                cur.execute(st)
                connect.commit()
            elif f in ("5","logout"):
                print("See you soon!")
                p="f"
                break
            
        
        
    

