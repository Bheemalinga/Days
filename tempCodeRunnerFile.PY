import mysql.connector
mydb = mysql.connector.connect(host = "localhost",user="root",password="Svbb@0808",database="football")
cur=mydb.cursor()