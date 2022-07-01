
connection = sqlite3.connect('shows.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Movies
              (MovieName TEXT,Actor TEXT,Actress TEXT, Year INT,Director TEXT)''')
cursor.execute('''INSERT INTO Movies (MovieName,Actor,Actress,Year,Director) VALUES ('Praveen', 'Kamal', 'Thara', 2024,'Lokesh Kanagaraj' )''')
cursor.execute('''INSERT INTO Movies (MovieName,Actor,Actress,Year,Director)VALUES ('Master', 'Vignesh', 'Malavika Mohan', 2025,'A.R Murugadoss' )''')
cursor.execute('''INSERT INTO Movies (MovieName,Actor,Actress,Year,Director)VALUES ('G-one', 'Revanth', 'Mahima','2014,'A R Murugadoss' )''')
cursor.execute('''INSERT INTO Movies (MovieName,Actor,Actress,Year,Director)VALUES ('Beast', 'Vijay', 'Pooja Hegde', 2022,'Nelson' )''')
cursor.execute('''SELECT * from Movies''')
result = cursor.fetchall();
print(result)
connection.commit()
connection.close()