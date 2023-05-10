import statistics
import psycopg2
# ------------------ DATA -------------------

day1 = ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW", "ORANGE",
        "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"]
day2 = ["ARSH", "BROWN", "GREEN", "BROWN", "BLUE", "BLUE", "BLEW", "PINK", "PINK", "ORANGE",
        "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "WHITE", "BLUE", "BLUE", "BLUE"]
day3 = ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "RED", "YELLOW", "ORANGE", "RED",
        "ORANGE", "RED", "BLUE", "BLUE", "WHITE", "BLUE", "BLUE", "WHITE", "WHITE"]
day4 = ["BLUE", "BLUE", "GREEN", "WHITE", "BLUE", "BROWN", "PINK", "YELLOW", "ORANGE", "CREAM",
        "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"]
day5 = ["GREEN", "WHITE", "GREEN", "BROWN", "BLUE", "BLUE", "BLACK", "WHITE", "ORANGE", "RED",
        "RED", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "WHITE"]
total_days = day5 + day4 + day3 + day2 + day1

# ------------------- FREQUENCIES -------------------

red = total_days.count("RED")
blue = total_days.count("BLUE")
green = total_days.count("GREEN")
white = total_days.count("WHITE")
orange = total_days.count("ORANGE")
brown = total_days.count("BROWN")
cream = total_days.count("CREAM")
pink = total_days.count("PINK")
blew = total_days.count("BLEW")
yellow = total_days.count("YELLOW")
arsh = total_days.count("ARSH")
black = total_days.count("BLACK")

all = (red + blue + green + white + orange + brown + cream + pink + blew + yellow + arsh + black) 
frequencies = [red, blue, green, white, orange, brown, cream, pink, blew, yellow, arsh, black]
mean = all / len(frequencies)

# ------------------------ SAVING DATA ------------------

# connection establishment
conn = psycopg2.connect(
database="postgres",
	user='postgres',
	password='12345',
	host='localhost',
	port= '5432'
)


# Creating a cursor object
cursor = conn.cursor()

# query to create a table in the database
sql = '''CREATE TABLE colors(
 id  SERIAL NOT NULL,
 name varchar(60) not null,
 frequency varchar(200) not null
)'''

# executing the query inorder to create the table
cursor.execute(sql)
print("Database has been created successfully !!")

# list to be inserted into table
data = [('Red', red), ('Blue', blue),
        ('Green', green), ('White', white),
        ('Orange', orange), ('Black', black),
        ('Brown', brown), ('Pink', pink), ('Cream', cream),
         ('Blew', blew), ('Yellow', yellow), ('Arsh', arsh)]

# inserting record into school table
for d in data:
        cursor.execute("INSERT into colors(name, frequency) VALUES (%s, %s)", d)
        print("List has been inserted to database successfully...")

# Commit your changes in the database
conn.commit()

print("Records successfully saved")

# Closing the connection
conn.close()

# The mean color is 7.9
# The most worn color was blue
# Red is the median color
