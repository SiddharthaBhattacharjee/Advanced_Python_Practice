import sqlite3

con = sqlite3.connect('test.db')

con.execute("Create Table Data(id varchar(20),value varchar(20))")

con.execute("Insert into Data(id,value) values('One','1')")
con.execute("Insert into Data(id,value) values('Two','2')")
con.commit()

cur = con.execute("select * from Data")
for row in cur:
   print(row)
