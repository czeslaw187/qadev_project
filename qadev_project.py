# import mysql.connector
#
# mydb = mysql.connector.connect(
#       host="localhost",
#       user="yourusername",
#       password="yourpassword"
# )
#
# print(mydb)

users = [
      {'name': 'Tedd Bundy', 'score': 50},
      {'name': 'Homer Simpson', 'score': 75},
      {'name': 'John Doe', 'score': 68}
]
# find user


def find_user(users):
      print('Find user')
      fname = input('Enter your First name: ')
      lname = input('Enter your last name: ')
      name = fname + ' ' + lname
      for user in users:
            if user['name'] == name:
                  print(f'user: {user["name"]} \n score: {user["score"]} \n percentage: {user["score"]}%')
                  quit()
      return True

# add new user

def add_new_user(users):
      print('Add new user \n')
      fname = input('Enter your First name: ')
      lname = input('Enter your last name: ')
      name = fname + ' ' + lname
      score = input('Enter new score: ')
      users += {'name': name, 'score': score}

is_there = find_user(users)
if is_there:
      add_new_user(users)