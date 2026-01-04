import sqlite3

conn = sqlite3.connect("chinook.sql")

cursor = conn.cursor()

query = "SELECT FirstName, LastName, Address FROM customers;"

cursor.execute(query)

customer_data = cursor.fetchall()

query = "SELECT Name FROM tracks WHERE MediaTypeId = 2;"

cursor.execute(query)

track_data = cursor.fetchall()

query = "SELECT City, COUNT(*) AS num_customers FROM customers GROUP BY City ORDER BY num_customers DESC;"

cursor.execute(query)

customers_city_data = cursor.fetchall()

query = "INSERT INTO media_types (MediaTypeId,Name) VALUES (6,'Windows Media Audio'),(7,'FLAC audio file');"

cursor.execute(query)
conn.commit()

query = "SELECT FirstName, LastName FROM employees WHERE ReportsTo = 'Nancy Edwards';"

cursor.execute(query)

employee_data = cursor.fetchall()

conn.close()