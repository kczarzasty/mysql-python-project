import mysql.connector

mydb = mysql.connector.connect(
       host = "localhost",
       user = "root",
       passwd = "abd",
       )

my_cursor = mydb.cursor()

#Create A Database
my_cursor.execute("CREATE DATABASE testdb")

#Show Database
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db[0])

#Create Table 
my_cursor.execute("CREATE TABLE users (name VARCHAR(255), email VARCHAR(255), age INTEGER(10), user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
my_cursor.execute("SHOW TABLES")
for table in my_cursor:
    print(table[0])

#Insert One Record
sqlStuff = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
record1 = ("Chris", "chris@chris.com", 40)
my_cursor.execute(sqlStuff, record1)
mydb.commit()

#Insert Multiple Records
sqlStuff = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
records = [("Tim", "tim@tim.com", 32),
    ("Mary", "Mary@mary.com", 21),
    ("Steve", "steve@stevee.com", 57),
    ("Tina", "tina@tina.com", 29),]

my_cursor.executemany(sqlStuff, records)
mydb.commit()

#Pull Data from Table
my_cursor.execute("SELECT * FROM users")
result = my_cursor.fetchall()
print("NAME\tEMAIL\t\t\tAGE\tID")
print("----\t-----\t\t\t---\t---")
for row in result:
    print(row[0] + "\t%s" %row[1] + "\t\t%s" %row[2] + "\t%s" %row[3])
