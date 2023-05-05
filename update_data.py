import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Samrin@1220',database='SAMRIN')
cur=mydb.cursor()
x='update SWAP set salary=salary+100 where emp_id=101'
cur.execute(x)
mydb.commit()