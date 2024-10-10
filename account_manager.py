import usernames 

user = input("Username: ")

password = input("Password: ")

if user in usernames.usernames :
  userspace = usernames.usernames.index(user)
  if password == usernames.password[userspace] :
    print("hi", user)
  else:
    print("invalid password")
else:
  print("invalid username")
