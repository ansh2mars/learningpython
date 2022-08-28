import random
import sys
import time

def end():
  print("Thanks for using math quiz!")
  sys.exit()

def add_easy():
  num1 = random.randint(1, 1000)
  num2 = random.randint(1, 1000)
  ans = num1 + num2
  user_ans = int(input(str(num1) + " + " + str(num2) + ": "))
  if user_ans == ans:
    print("Corect! Run again to play more")
    sys.exit()
  else:
    print("Wrong! Let's try another question...")
    add_easy()

def add_intermediate():
  num1 = random.randint(1000, 100000)
  num2 = random.randint(1000, 100000)
  ans = num1 + num2
  user_ans = int(input(str(num1) + " + " + str(num2) + ": "))
  if user_ans == ans:
    print("Corect! Run again to play more")
    sys.exit()
  else:
    print("Wrong! Let's try another question...")
    add_intermediate()
    
def add_hard():
  num1 = random.randint(100000, 1000000000)
  num2 = random.randint(100000, 1000000000)
  ans = num1 + num2
  user_ans = int(input(str(num1) + " + " + str(num2) + ": "))
  if user_ans == ans:
    print("Corect! Run again to play more")
    sys.exit()
  else:
    print("Wrong! Let's try another question...")
    add_hard()
def subtract_easy():
  num1 = random.randint(1, 1000)
  num2 = random.randint(1, 1000)
  ans = num1 - num2
  user_ans = int(input(str(num1) + " - " + str(num2) + ": "))
  if user_ans == ans:
    print("Corect! Run again to play more")
    sys.exit()
  else:
    print("Wrong! Let's try another question...")
    subtract_easy()
def subtract_intermediate():
  num1 = random.randint(1000, 100000)
  num2 = random.randint(1000, 100000)
  ans = num1 - num2
  user_ans = int(input(str(num1) + " - " + str(num2) + ": "))
  if user_ans == ans:
    print("Corect! Run again to play more")
    sys.exit()
  else:
    print("Wrong! Let's try another question...")
    subtract_intermediate()
def subtract_hard():
  num1 = random.randint(100000, 1000000000)
  num2 = random.randint(100000, 1000000000)
  ans = num1 + num2
  user_ans = int(input(str(num1) + " - " + str(num2) + ": "))
  if user_ans == ans:
    print("Corect! Run again to play more")
    sys.exit()
  else:
    print("Wrong! Let's try another question...")
    subtract_hard()
def multiply_easy():
  num1 = random.randint(1, 1000)
  num2 = random.randint(1, 10)
  ans = num1 * num2
  user_ans = int(input(str(num1) + " * " + str(num2) + ": "))
  if user_ans == ans:
    print("Corect! Run again to play more")
    sys.exit()
  else:
    print("Wrong! Let's try another question...")
    multiply_easy()
def multiply_intermediate():
  num1 = random.randint(1, 100000)
  num2 = random.randint(1, 100)
  ans = num1 * num2
  user_ans = int(input(str(num1) + " * " + str(num2) + ": "))
  if user_ans == ans:
    print("Corect! Run again to play more")
    sys.exit()
  else:
    print("Wrong! Let's try another question...")
    multiply_intermediate()
def multiply_hard():
  num1 = random.randint(1, 1000000000)
  num2 = random.randint(1, 1000)
  ans = num1 * num2
  user_ans = int(input(str(num1) + " * " + str(num2) + ": "))
  if user_ans == ans:
    print("Corect! Run again to play more")
    sys.exit()
  else:
    print("Wrong! Let's try another question...")
    multiply_hard()

def divide_easy():
  num1 = random.randint(1, 1000)
  num2 = random.randint(1, 10)
  ans = num1 // num2
  ans2 = num1 % num2
  user_ans = int(input(str(num1) + " // " + str(num2) + ": "))
  user_ans2 = int(input(str(num1) + " % " + str(num2) + ": "))
  if user_ans == ans:
    if user_ans2 == ans2:
      print("Corect! Run again to play more")
      sys.exit()
  else:
    print("Wrong! Let's try another question...")
    divide_easy()

def divide_intermediate():
  num1 = random.randint(1, 100000)
  num2 = random.randint(1, 100)
  ans = num1 // num2
  ans2 = num1 % num2
  user_ans = int(input(str(num1) + " // " + str(num2) + ": "))
  user_ans2 = int(input(str(num1) + " % " + str(num2) + ": "))
  if user_ans == ans:
    if user_ans2 == ans2:
      print("Corect! Run again to play more")
      sys.exit()
  else:
    print("Wrong! Let's try another question...")
    divide_intermediate()

def divide_hard():
  num1 = random.randint(1, 1000000000)
  num2 = random.randint(1, 1000)
  ans = num1 // num2
  ans2 = num1 % num2
  user_ans = int(input(str(num1) + " // " + str(num2) + ": "))
  user_ans2 = int(input(str(num1) + " % " + str(num2) + ": "))
  if user_ans == ans:
    if user_ans2 == ans2:
      print("Corect! Run again to play more")
      sys.exit()
  else:
    print("Wrong! Let's try another question...")
    divide_hard()

def main():
  print("Welcome to math quiz\nAnswer the following questions:")
  time.sleep(0.5)
  equation = int(input("1 = add\n2 = subtract\n3 = multiply\n4 = divide\nchoose: "))  
  time.sleep(0.25)  
  mode = int(input("1 = easy\n2 = intermediate\n3 = hard\nchoose: "))
  time.sleep(0.125)
  if equation == 1 and mode == 1:
    add_easy()
  elif equation == 1 and mode == 2:
    add_intermediate()
  elif equation == 1 and mode == 3:
    add_hard()
  elif equation == 2 and mode == 1:
    subtract_easy()
  elif equation == 2 and mode == 2:
    subtract_intermediate()
  elif equation == 2 and mode == 3:
    subtract_hard()
  elif equation == 3 and mode == 1:
    multiply_easy()
  elif equation == 3 and mode == 2:
    multiply_intermediate()
  elif equation == 3 and mode == 3:
    multiply_hard()
  elif equation == 4 and mode == 1:
    divide_easy ()
  elif equation == 4 and mode == 2:
    divide_intermediate()
  elif equation == 4 and mode == 3:
    divide_hard()
  else:
    print("Invalid Input, Please Try again")
    main()
main()