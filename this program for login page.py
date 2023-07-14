from pystyle import *
print(Box.Lines("    ********* wolcome to pc *********"))
Write.Print("---this program for login page \n",Colors.blue_to_purple,interval=0.1)
Write.Print("---please write username and password\n\n",Colors.blue_to_purple,interval=0.1)
while True:
    username = Write.Input("---write a username : ",Colors.blue_to_purple,interval=0.1)
    password = Write.Input("---write a password : ",Colors.blue_to_purple,interval=0.1)
    if username == "abdulazim" and password == "1432":
        Write.Print("       welcome\n",Colors.blue_to_purple,interval=0.1)
        input("\n pres any key to exit ...")
    else:
        print("try again",Colors.red,interval=0.1)
input("\n pres any key to exit ...")
