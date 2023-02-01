import mysql.connector

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="Pa$$w0rd",
      database="qastore"
)

client = mydb.cursor()

users = [
      {'name': 'Tedd Bundy', 'score': 50},
      {'name': 'Homer Simpson', 'score': 75},
      {'name': 'John Doe', 'score': 68}
]

def add_new_user(name):
      print('Add new user \n')
      ict_score = input('Enter new ICT score: ')
      math_score = input("Enter new Math score: ")
      chemistry_score = input("Enter new chemistry score: ")
      client.execute("INSERT INTO students (name, ict, math, chemistry) VALUES (%s, %s, %s, %s)",(name, ict_score, math_score, chemistry_score))
      mydb.commit()
      if client.rowcount == True:
            print("Record inserted")

# find user

print('Find user')
fname = input('Enter your First name: ')
lname = input('Enter your last name: ')
name = fname + ' ' + lname
client.execute("SELECT * FROM students WHERE name=%s", (name,))
student = client.fetchone()
if  student == None:
      print("User doesn't exist \n")
      add_new_user(name)
else:
      print(f"Name: {student[1]} \n ICT score: {student[2]} \n Math score: {student[3]} \n Chemistry score: {student[4]}")



