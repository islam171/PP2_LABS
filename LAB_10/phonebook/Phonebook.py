import psycopg2
import csv 
import datetime

DB_HOST = "localhost"
DB_NAME = "phonebook"
DB_USER = "postgres"
PASSWORD = "2149pyKab!@"

try:
    conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=PASSWORD, port="5432")
    cur = conn.cursor()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)

# get id of last record
def get__lastId():
    cur.execute('''SELECT id FROM numbers ORDER BY id DESC;''')
    row = cur.fetchone()
    if(not row):
        return 0
    return row[0] 

def show__table():

    cur.execute("SELECT * FROM numbers ORDER BY id ASC;")
    rows = cur.fetchall()
    if(not rows): 
        print("Phone book is empty")
    for row in rows:
        print(row)
    

def insert__csv():

    date = datetime.datetime.now()
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                cur.execute(
                    '''INSERT INTO numbers (id, name, number, date) VALUES (%s, %s, %s, %s)''',
                    [get__lastId()+1,*row, date]
                )
            except(psycopg2.DatabaseError) as error:
                print(error)
                return 
    print("CSV is imported")

def insert__console():
    # input data
    name = input("Enter name: ")
    number = input("Enter number: ")
    date = datetime.datetime.now()

    # get last Id
    lastId = get__lastId(cur)

    try:
        #insert data
        cur.execute(
            '''INSERT INTO numbers (id, name, number, date) VALUES (%s, %s, %s, %s)''',
            [int(lastId+1), name, number, date]
        )
    except (psycopg2.DatabaseError) as error:
        print(error)
        return
    conn.commit()
    print("Number is added")

def delete():
    username = input("Enter username: ")
    try:
        cur.execute('''Delete from numbers where name = %s''', [username])
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
        return
    print("User is deleted")

def query():
    print("Choose option of filter")
    option = input("1 - by username or 2 - by phone: ")
    try:
        if(option == "1"):
            username = input("Enter username: ")
            cur.execute('''select * from numbers where name = %s''', [username])
        elif(option == "2"):
            phone = input("Enter username: ")
            cur.execute('''select * from numbers where number = %s''',[phone])
    except(psycopg2.DatabaseError) as error:
        print(error)
        return
    rows = cur.fetchall()
    if(not rows):
        print("Does not exist")
        return
    for row in rows:
        print(row)

def update():

    phone =  input("Enter phone: ")

    cur.execute('''SELECT * FROM numbers WHERE number = %s''', [phone])
    row = cur.fetchone()
    if(not row):
        print("Does not exist")
        return 

    username = row[1]
    phone = row[2]

    print(f"name: {username}, phone: {phone}")
    print("What column do you want to change?")
    text = input("1 - name or 2 - phone: ")

    process = True
    while process:
        if(text == "name"):
            newUsername = input("Enter name:")
            cur.execute('''UPDATE numbers SET name = %s WHERE number = %s''', [newUsername, phone])
            process = False
        elif(text == "phone"):
            newPhone = input("Enter phone:")
            cur.execute('''UPDATE numbers SET number = %s WHERE name = %s''', [newPhone, username])
            process = False
        else:
            print("Please choose phone or name")
            return 
    conn.commit()
    print("Number is updated")

while True:
    print("q - quit")
    print("1 - show table")
    print("2 - insert csv")
    print("3 - insert console")
    print("4 - update")
    print("5 - delete")
    print("6 - query")
    command = input("Enter command: ")
    if(command=="q"): break
    if(command=="1"): show__table()
    if(command=="2"): insert__csv()
    if(command=="3"): insert__console()
    if(command=="4"): update()
    if(command=="5"): delete()
    if(command=="6"): query()


cur.close()
conn.close()


