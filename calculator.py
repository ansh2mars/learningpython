import math
import sys
import colorama
from colorama import Fore
colorama.init()
def Add():
    print(Fore.LIGHTBLACK_EX + "You chose addition")
    a1 = int(input("Enter Addend 1: "))
    a2 = int(input("Enter Addend 2: "))
    res = a1 + a2
    print("The sum of " + str(a1) + " and " + str(a2) + " is " + str(res))
   


def Subtract():
    print(Fore.LIGHTGREEN_EX + "You chose subtraction")
    mn = int(input("Enter Main Number: "))
    n1 = int(input("Enter Subtraction Number: "))
    res = mn - n1
    print(str(mn) + " minus " + str(n1) + " is " + str(res))


def Multiply():
    print(Fore.YELLOW + "You chose multiplication")
    n1 = int(input("Number 1: "))
    n2 = int(input("Number 2: "))
    res = n1 * n2
    print("The product of " + str(n1) + " multiplied by " + str(n2) + " is " +
          str(res))


def Divide():
    print(Fore.LIGHTBLUE_EX + "You chose division")
    D = int(input("Enter Denominator: "))
    N = int(input("Enter Numerator: "))
    res = D // N
    print(str(D) + " divided by " + str(N) + " is " + str(res))
    res = D % N
    print("The remainder is " + str(res))
    res = D / N
    print("Decimal Form = " + str(res))


def Powers():
    print(Fore.LIGHTMAGENTA_EX + "You chose powers")
    B = int(input("Enter base: "))
    P = int(input("Enter power: "))
    res = B**P
    print(str(B) + " To the power of " + str(P) + " is " + str(res))


def Average():
  print(Fore.LIGHTCYAN_EX + "You chose average")
  num = int(input("how many numbers do you want to find the average of: "))
  sum = 0
  for i in range(num):
    newnum = int(input("enter number #" + str(i + 1) + ": "))
    sum = sum + newnum
  avg = sum / num
  print("average is: " + str(avg))


def EAdd():
  print(Fore.LIGHTWHITE_EX + "You chose extended addition")
  num = int(input("How many numbers do you want to add?: "))
  sum = 0
  for i in range(num):
    newnum = int(input("enter number #" + str(i + 1) + ": "))
    sum = sum + newnum
  print("sum is " + str(sum))


def ESubtract():
  print(Fore.BLUE + "You chose extended subtraction")
  num = int(input("how many numbers do you want to subtract from the main number: "))
  MN = int(input("Main number: "))
  newnum = 0
  res = MN
  for i in range(num):
    newnum = int(input("enter number #" + str(i + 1) + ": "))
    res = res - newnum
  print("answer is " + str(res))


def S():
  print(Fore.MAGENTA + "You chose square")
  SqNum = int(input("Enter the number you want to square: "))
  res = SqNum * SqNum
  print(str(SqNum) + " squared is " + str(res))


def C():
  print(Fore.CYAN + "You chose cube")
  CuNum = int(input("Enter the number you want to cube: "))
  res = CuNum * CuNum * CuNum
  print(str(CuNum) + " cubed is " + str(res))


def SQRT():
  print(Fore.WHITE + "You chose square root")
  SqRoNum = int(input("Enter the number you want to square root: "))
  res = math.sqrt(SqRoNum)
  print("The square root of " + str(SqRoNum) + " is " + str(res))

def CBRT():
  print(Fore.BLACK + "You chose cube root")
  CbRoNum = int(input("Enter the number you want to cube root: "))
  res = round(CbRoNum**(1 / 3), 10)
  print(str(CbRoNum) + " cube root is " + str(res))
  

def End():
  print(Fore.LIGHTYELLOW_EX + "Thanks for using this calculator!")
  sys.exit()


def I():
  try:
    user_input = int(input(Fore.GREEN +" 1=Add,\n 2=Subtract,\n 3=Multiply,\n 4=Divide,\n 5=Powers,\n 6=Average,\n 7=Extend Add,\n 8=Extend Subtract,\n 9=Square,\n 10=Cube,\n 11=Square Root,\n 12=Cube Root,\n 13=End\n Choose: "))
  except:
    print( Fore.RED + "Invalid Input. Please try again...")
    
  if user_input == 1:
    Add()
    A = input("Thank you for trying addition. Want to try more? yes/no: ")
    if A.lower() == "yes":
      I()
    elif A.lower() == "no":
      End()
  if user_input == 2:
    Subtract()
    S = input("Thank you for trying subtraction. Want to try more? yes/no: ")
    if S.lower() == "yes":
      I()
    elif S.lower() == "no":
      End()
  if user_input == 3:
    Multiply()
    M = input("Thank you for trying multiplication. Want to try more?yes/no: ")
    if M.lower() == "yes":
      I()
    elif M.lower() == "no":
      End()
  if user_input == 4:
    Divide()
    D = input("Thank you for trying division. Want to try more?yes/no:  ")
    if D.lower() == "yes":
      I()
    elif D.lower() == "no":
      End()
  if user_input == 5:
    Powers()
    P = input("Thank you for trying powers. Want to try more?yes/no: ")
    if P.lower() == "yes":
      I()
    elif P.lower() == "no":
      End()
  if user_input == 6:
    Average()
    Am = input("Thank you for trying average. Want to try more?yes/no: ")
    if Am.lower() == "yes":
      I()
    elif Am.lower() == "no":
      End()
  if user_input == 7:
    EAdd()
    EA = input("Thank you for trying extended addition. Want to try more?yes/no: ")
    if EA.lower() == "yes":
      I()
    elif EA.lower() == "no":
      End()
  if user_input == 8:
    ESubtract()
    ES = input("Thank you for trying extended subtraction. Want to try more?yes/no: ")
    if ES.lower() == "yes":
      I()
    elif ES.lower() == "no":
      End()
  if user_input == 9:
    S()
    Squ = input("Thank you for trying square. Want to try more?yes/no: ")
    if Squ.lower() == "yes":
      I()
    elif Squ.lower() == "no":
      End()
  if user_input == 10:
    C()
    Cub = input("Thank you for trying cube. Want to try more?yes/no: ")
    if Cub.lower() == "yes":
      I()
    elif Cub.lower() == "no":
      End()
  if user_input == 11:
    SQRT()
    SR = input("Thank you for trying square root. Want to try more?yes/no: ")
    if SR.lower() == "yes":
      I()
    elif SR.lower() == "no":
      End()
  if user_input == 12:
    CBRT()
    CR = input("Thank you for trying cube root. Want to try more?yes/no: ")
    if CR.lower() == "yes":
      I()
    elif CR.lower() == "no":
      End()
  if user_input == 13:
    End()
  if user_input > 13 or user_input < 1:
    print(Fore.RED + "Invalid Input. Please try again...")
    I()


def main():
    I()

if __name__ == "__main__":
    main()
