user = "ryanflaharty"
passw = "flaharty"
username = input("Enter username here:")
password = input("Enter the password here:")

def passCheck():
    if username == "ryanflaharty" and password == "flaharty":
        print("Access granted!")
    elif username == "ryanflaharty" and password != "flaharty":
        print("Wrong password")
    elif username != "ryanflaharty" and password == "flaharty":
        print("Wrong username")
    else:
        print("Wrong username and password")
passCheck()


        
