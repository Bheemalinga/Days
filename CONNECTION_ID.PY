import mysql.connector
mydb = mysql.connector.connect(host = "localhost",user="root",password="Asdf@1234",database="football")
cur=mydb.cursor()
f='select * from football_venue'
cur.execute(f)
display=cur.fetchall()
for x in display:
    print(x)
