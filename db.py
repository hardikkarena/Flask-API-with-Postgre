import psycopg2

conn = psycopg2.connect(
   database="blog", user='postgres', password='admin', host='localhost', port= '5432'
)
cursor = conn.cursor()

# cursor.execute("select version()")
# data = cursor.fetchone()
# print("Connection established to: ",data)

# cursor.execute("INSERT INTO author(id,email,password,first_name,last_name)values(4,'hardik@gmail.com','admin','hardik','karena')")
# cursor.execute("INSERT INTO post(id,title,description)values(2,'Hardsdfbmik','asdjkasda')")
# cursor.execute('''SELECT * FROM author;''')
# cursor.execute('''SELECT * FROM post;''')

# result = cursor.fetchall()
# print(result)
# conn.commit()
# print("Inserted")
# conn.close()
