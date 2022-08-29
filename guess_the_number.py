import random
import sys
print("Welcome to guess the number\nChoose what numbers it should be between.")
num1 = int(input("num1: "))
num2 = int(input("num2: "))
num = random.randint(num1, num2)
def check_ask(tries):
  guess = int(input("guess: "))
  tries = tries + 1
  if guess == num:
    print("correct, run again to play more")
    print("It took you", (tries), "try/tries")
    sys.exit()
  elif guess > num:
    print("Too High!")
    check_ask(tries)
  elif guess < num:
    print("Too Low!")
    check_ask(tries)
check_ask(0)