import mysql.connector
mydb = mysql.connector.connect(host = "localhost",user="root",password="Asdf@1234",database="football")
cur=mydb.cursor()
x='update football_venue'
