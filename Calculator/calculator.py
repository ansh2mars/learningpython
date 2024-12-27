import sys 

def Add():
  a1=int(input("Enter Addend 1: "))
  a2=int(input("Enter Addend 2: "))
  res = a1+a2
  print("The sum of " + str(a1) + " and " + str(a2) + " is " +     str(res))
def Subtract():
  mn=int(input("Enter Main Number: "))
  n2=int(input("Enter Number 2: "))
  res=mn-n2
  print(str(mn) + " minus " + str(n2) + " is " + str(res))
def Multiply():
  n1=int(input("Number 1: "))
  n2=int(input("Number 2: "))
  res=n1*n2
  print("The product of " + str(n1) + " multiplied by " + str(n2) + " is " + str(res))
def Divide():
  D=int(input("Enter Numerator: "))
  N=int(input("Enter Denominator: "))
  res=D//N
  print(str(D) + " divided by " + str(N) + " is " + str(res))
  res=D%N
  print("The remainder is " + str(res))
  res=D/N
  print("Decimal Form = " + str(res))
def Powers():
  B=int(input("Enter base: "))
  P=int(input("Enter power: "))
  res=B**P
  print(str(B) + " To the power of " + str(P) + " is " + str(res))
def Average():
  num=int(input("how many numbers do you want to find the average of: "))
  sum = 0;
  for i in range(num):
    newnum = int(input("enter number #" + str(i+1) + ": "))
    sum = sum + newnum
  avg = sum / num  
  print("average is: " + str(avg));
def EAdd():
  num=int(input("How many numbers do you want to add?: "))
  sum=0;
  for i in range(num):
    newnum=int(input("enter number #" + str(i+1) + ": "))
    sum=sum+newnum
  print("sum is " + str(sum))
def ESubtract():
  num=int(input("how many numbers do you want to subtract from the main number: "))
  MN=int(input("Main number: "))
  newnum=0;
  res=MN
  for i in range(num):
    newnum=int(input("enter number #" + str(i+1) + ": "))
    res = res - newnum
  print("answer is " + str(res))
def S():
  SqNum=int(input("Enter the number you want to square: "))
  res=SqNum*SqNum
  print(str(SqNum) + " squared is " + str(res))
def C():
  CuNum=int(input("Enter the number you want to cube: "))
  res=CuNum*CuNum*CuNum
  print(str(CuNum) + " cubed is " + str(res))
def SR():
  import math
  SqRoNum=int(input("Enter the number you want to square root: "))
  res = math. sqrt(SqRoNum)
  print("The square root of " + str(SqRoNum) + " is " +          str(res))
def CR():
  CbRoNum=int(input("Enter the number you want to cube root: "))
  res = round(CbRoNum**(1/3), 10)
  print(str(CbRoNum) + " cube root is " + str(res))
def End():
  print("Thanks for using this calculator!")
  sys.exit()

def Next():
  I()

def I():
  user_input=int(input(" 1=Add,\n 2=Subtract,\n 3=Multiply,\n 4=Divide,\n 5=Powers,\n 6=Average,\n 7=Extend Add,\n 8=Extend Subtract,\n 9=Square,\n 10=Cube,\n 11=Square Root,\n 12=Cube Root,\n 13=End\n Choose: "))
  if user_input==1: 
    Add()
    print("Thank you for trying. Want to try again? ")
    Next()
  if user_input==2: 
    Subtract()
    print("Thank you for trying subtraction. Want to try again? ")
    Next()
  if user_input==3: 
    Multiply()
    print("Thank you for trying multiplication. Want to try again? ")
    Next()
  if user_input==4: 
    Divide()
    print("Thank you for trying divsion. Want to try again? ")
    Next()
  if user_input==5: 
    Powers()
    print("Thank you for trying powers. Want to try again? ")
    Next()
  if user_input==6: 
    Average()
    print("Thank you for trying average. Want to try again? ")
    Next()
  if user_input==7:
    EAdd()
    print("Thank you for trying extended addition. Want to try again? ")
    Next()
  if user_input==8:
    ESubtract()
    print("Thank you for trying extended subtraction. Want to try again? ")
    Next()
  if user_input==9:
    S()
    print("Thank you for trying square. Want to try again? ")
    Next()
  if user_input==10:
    C()
    print("Thank you for trying cube. Want to try again? ")
    Next()
  if user_input==11:
    SR()
    print("Thank you for trying square root. Want to try again? ")
    Next()
  if user_input==12:
    CR()
    print("Thank you for trying cube root. Want to try again? ")
    Next()
  if user_input==13:
    End()
  if user_input>13 or user_input<1:
    print("Invalid Input. Please try again")
    I()

def main():
    I()

if __name__ == "__main__":
    main()

