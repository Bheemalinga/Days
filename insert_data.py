import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Asdf@1234',database='SAM')
cur=mydb.cursor()
z='insert into SWAP(emp_id,emp_name,salary) values(%s,%s,%s)'
a=(100,'MUSSU',10000)
cur.execute(z,a)
mydb.commit()
print('Data inserted succesfully')
