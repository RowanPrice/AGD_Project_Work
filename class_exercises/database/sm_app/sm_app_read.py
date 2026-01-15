import sqlite3

# Create a connection to the database
conn = sqlite3.connect("sm_app.sqlite")

# Create a cursor
cursor = conn.cursor()

# Create a SELECTION command
select_posts = """
SELECT title, desctiption
FROM posts
"""

# Fetch all posts
posts = cursor.execute(select_posts).fetchall()

# Close the connection
conn.close()
