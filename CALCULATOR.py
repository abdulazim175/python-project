#craete a calculator
#This code creates a simple calculator program that allows the user to input two numbers and an operator (+, -, *, /) and then performs the corresponding arithmetic operation on the two numbers.
#  The program then asks the user if they want to try the operation again and exits if the user inputs "no".
#  If the user inputs an invalid operator, the program will print an error message and ask the user to try again.

#import pystyle
from pystyle import *

print(Box.Lines("        ********* wolcome to calculator *********"))
Write.Print("---this program a calculator\n\n",Colors.blue_to_purple,interval=0.1)
#craete a number
while True :
    number1 = int(Write.Input("enter a first number :\n",Colors.blue_to_purple,interval=0.1))
    operator = Write.Input("enter a operator :\n",Colors.blue_to_purple,interval=0.1)
    number2 = int(Write.Input("enter a last number :\n",Colors.blue_to_purple,interval=0.1))
    if operator == "+":
        Write.Input("the result is : ",Colors.blue_to_purple,interval=0.1)
        print(number1 + number2)
       
    elif operator == "-":
        Write.Input("the result is : ",Colors.blue_to_purple,interval=0.1)
        print(number1 - number2)
        
    elif operator == "*":
        Write.Input("the result is : ",Colors.blue_to_purple,interval=0.1)
        print(number1 * number2)  
        
    elif operator == "/":
        Write.Input("the result is : ",Colors.blue_to_purple,interval=0.1)
        print(number1 / number2)
    yes =  Write.Input("do you want try agin yes/no :\n",Colors.blue_to_green,interval=0.1)
   
    if yes == ("yes")  :
        Write.Print("          hello agin\n\n",Colors.purple_to_blue,interval=0.1)
    elif yes == ("no") :
        Write.Input("\n pres any key to exit ...",Colors.red,interval=0.1)
        raise SystemExit
    else :
        Write.Input("\n Error writing question plaese try agin ...",Colors.red,interval=0.1)
    
        