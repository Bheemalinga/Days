import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Asdf@1234')
print(mydb.connection_id)
