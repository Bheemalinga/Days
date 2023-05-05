import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Svbb@0808')
print(mydb.connection_id)