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
