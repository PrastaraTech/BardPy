import sqlite3
import csv


# Connect to a SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('ncert_books.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# # Create a table
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS users (        
#                book_id INTEGER PRIMARY KEY,
#                grade TEXT,
#                class INTEGER,        
#                book_name TEXT,
#                web_url TEXT,
#                local_url TEXT,
#                pdf_name TEXT,
#                pdf_web_url TEXT,
#                pdf_local_url TEXT
#     )
# ''')

# # Commit the changes and close the connection
# conn.commit()
# conn.close()


# alter_query = "ALTER TABLE books ADD COLUMN subject_name TEXT"

# try:
#     cursor.execute(alter_query)
#     print("Column added successfully.")
# except sqlite3.Error as e:
#     print("An error occurred:", e)

# # Commit the changes and close the connection
# conn.commit()
# conn.close()

# Insert data into the table
# try:
#     cursor.execute("INSERT INTO books (grade, class,subject_name,book_name) VALUES (?, ?, ?, ?)", 
#                ('XII', 12, 'Computer Science', 'Informatics Practices')#,               ("XII", 12, 'Computer Science', 'Computer Science with Python')
#                )
#     print("Column added successfully.")
# except sqlite3.Error as e:
#     print("An error occurred:", e)

# conn.commit()

# Function to insert data into SQLite table
def insert_data(cursor, subject, grade, class_, book_name):
    insert_query = '''
        INSERT INTO books (subject_name, grade, class, book_name)
        VALUES (?, ?, ?, ?)
    '''
    cursor.execute(insert_query, (subject, grade, class_, book_name))

# Read data from CSV and insert into the SQLite table
# with open('NCERT_Books.csv', 'r') as file:
#     csv_reader = csv.DictReader(file)
#     for row in csv_reader:
#         # Extract data from CSV
#         subject = row['Subject']
#         grade = row['Grade']
#         class_ = int(row['Class'])
#         book_name = row['Book Name']

#         # Insert data into SQLite table
#         insert_data(cursor, subject, grade, class_, book_name)
# conn.commit()

cursor.execute("SELECT * FROM books")


rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)
conn.close()
