import psycopg2

conn = psycopg2.connect(
   database="blog", user='postgres', password='admin', host='localhost', port= '5432'
)
cursor = conn.cursor()


