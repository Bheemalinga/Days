import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Asdf@1234',database='SAM')
cur=mydb.cursor()
z='insert into SWAP(emp_id,emp_name,salary) values(%s,%s,%s)'
a=[(109,'FARHA',10000),(101,'sABIYA',20000),(102,'SONY',24000)]
cur.executemany(z,a)
mydb.commit()
print('Data inserted succesfully')
