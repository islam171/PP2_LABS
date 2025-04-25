import psycopg2
import csv 
import json

DB_HOST = "localhost"
DB_NAME = "phonebook"
DB_USER = "postgres"
PASSWORD = "2149pyKab!@"

try:
    conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=PASSWORD, port="5432")
    cur = conn.cursor()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)

# ----- FUNCTION ------
# get id of last record
def get__lastId():
    cur.execute('''SELECT id FROM numbers ORDER BY id DESC;''')
    row = cur.fetchone()
    if(not row):
        return 0
    return row[0] 

def validInput(n):
    while True:
        value = input(f"Enter {n}: ")
        try:
            return int(value)
        except ValueError:
            print("Enter number!")

# ----- FUNCTION ------

   
# first task
def query():
    print("Choose option of filter")
    option = input("1 - by username, 2 - by phone 3 - by lastname: ")
    try:
        if(option == "1"):
            username = input("Enter username: ")
            cur.execute('''select * from getNumberByName(%s)''', [username])
        elif(option == "2"):
            phone = input("Enter phone: ")
            cur.execute('''select * from getNumberByPhone(%s)''', [phone])
        elif(option == "3"):
            lastname = input("Enter lastname: ")
            cur.execute('''select * from getNumberByLastName(%s)''', [lastname])
    except(psycopg2.DatabaseError) as error:
        print(error)
        return
    rows = cur.fetchall()
    if(not rows):
        print("Does not exist")
        return
    for row in rows:
        print(row)
    
# second task 
def insert__console():
    # input data
    name = input("Enter name: ")
    lastname = input("Enter lastname: ")
    number = input("Enter number: ")

    try:
        #insert data
        cur.execute('''call createPhone(%s, %s, %s)''', [name, lastname, number])
    except (psycopg2.DatabaseError) as error:
        print(error)
        return
    conn.commit()
    print("Number is added")

# third task
def insert__csv():
    with open('data.csv', 'r') as file:
        reader = list(csv.DictReader(file))
        reader = json.dumps(reader)
        try:
            cur.execute('call createUsers(%s)', [reader])
        except(psycopg2.DatabaseError) as error:
            print(error)
            return 
    print("CSV is imported")


# FORTH TASK
def show__table(): 
    limit = validInput("limit") 
    step = validInput("step") 
    offset = 0

    while True:
        command = input("back - l, next - r, to leave like that - s: ")
        if(command == 'r'):
            offset += step
        elif(command == 'l'):
            if offset >= 1:
                offset -= step
        elif(command == 's'):
            pass
        elif(command == 'q'): 
            break
        else:
            continue
        cur.execute("SELECT * FROM pagination(%s, %s)", [limit, offset])
        rows = cur.fetchall()
        if(not rows): 
            print("Phone book is empty")
            offset-=step
        for row in rows:
            print(row)


def delete():
    phone = input("Enter phone: ")
    try:
        cur.execute('''call deleteUserByPhone(%s)''', [phone])
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
        return
    print("User is deleted")



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


