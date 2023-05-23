import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Asdf@1234',database='SAM')
cur=mydb.cursor()
f='select * from SWAP where emp_id=101'
cur.execute(f)
display=cur.fetchall()
for x in display:
    print(x)
