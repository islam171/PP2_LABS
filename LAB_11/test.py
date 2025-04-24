import psycopg2

DB_HOST = "localhost"
DB_NAME = "phonebook"
DB_USER = "postgres"
PASSWORD = "2149pyKab!@"

try:
    conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=PASSWORD, port="5432")
    cur = conn.cursor()
except (psycopg2.DatabaseError) as error:
    print(error)

# cur.execute('''select get_discount(100, 10);''')
# cur.execute('''select get_grades(10);''')
# cur.execute('''call print_numbers(10);''')
cur.execute('''select * from SearchPhoneBook('islam');''')
# print(cur.fetchone()[0])
conn.commit()

cur.close()
conn.close()