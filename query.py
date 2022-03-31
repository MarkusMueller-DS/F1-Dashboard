import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="f1db"
)

mycursor = mydb.cursor()

mycursor.execute("""
        SELECT *
        FROM circuits;
""")

myresult = mycursor.fetchall()

# get column names from table
column_names = mycursor.column_names
# print(column_names)

row_list = []
for x in myresult:
    row_list.append(x)

# print(type(row_list[0]))

df = pd.DataFrame(columns=column_names, data=row_list)

print(df.head())

mycursor.close()
mydb.close()