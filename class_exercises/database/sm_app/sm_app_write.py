import sqlite3

insert_query = """
INSERT INTO users (name, age, gender, nationality)
VALUES (?, ?, ?, ?);
"""

conn = sqlite3.connect('sm_app.sqlite')
cursor = conn.cursor()
for _ in [('James', 25, 'male', 'USA'),
          ('Leila', 32, 'female', 'France'),
          ('Brigitte', 35, 'female', 'England'),
          ('Mike', 40, 'male', 'Denmark'),
          ('Elizabeth', 21, 'female', 'Canada')]:
    cursor.execute(insert_query, _)

conn.commit()