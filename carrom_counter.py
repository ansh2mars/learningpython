import sys
def player2():
  game2 = True
  NP1 = (input("What do you want to name Player 1: "))
  NP2 = (input("What do you want to name Player 2: "))
  P1S = 0
  P2S = 0
  while game2 == True:
    P1P = int(input("How many points did " + str(NP1) + " make in this turn: "))
    P1S = P1S + P1P
    P2P = int(input("How many points did " + str(NP2) + " make in this turn: "))
    P2S = P2S + P2P
    GM = (input("is the game over: "))
    if GM.lower() == 'yes':
      print(str(NP1) + " has " + str(P1S) + " points")
      print(str(NP2) + " has " + str(P2S) + " points")
      if P1S > P2S:
        print(str(NP1) + " wins!")
        game2 = False
      elif P1S < P2S:
        print(str(NP2) + " wins!")
        game2 = False
      else:
        print("Draw!")
        sys.exit()
    elif GM.lower() == 'no':
      continue 

def player3():
  game3 = True
  NP1 = (input("What do you want to name Player 1: "))
  NP2 = (input("What do you want to name Player 2: "))
  NP3 = (input("What do you want to name Player 3: "))
  P1S = 0
  P2S = 0
  P3S = 0
  while game3 == True:
    P1P = int(input("How many points did " + str(NP1) + " make in this turn: "))
    P1S = P1S + P1P
    P2P = int(input("How many points did " + str(NP2) + " make in this turn: "))
    P2S = P2S + P2P
    P3P = int(input("How many points did " + str(NP3) + " make in this turn: "))
    P3S = P3S + P3P
    GM = (input("is the game over: "))
    if GM.lower() == 'yes':
      print(str(NP1) + " has " + str(P1S) + " points")
      print(str(NP2) + " has " + str(P2S) + " points")
      print(str(NP3) + " has " + str(P3S) + " points")
      if P1S > P2S and P1S > P3S:
        print(str(NP1) + " wins!")
        game3 = False
      elif P2S > P1S and P2S > P3S:
        print(str(NP2) + " wins!")
        game3 = False
      elif P3S > P1S and P3S > P2S:
        print(str(NP3) + " wins!")
        game3 = False
      else:
        print("Draw!")
        sys.exit()
    elif GM.lower() == 'no':
      continue

def player4():
  game4 = True
  NP1 = (input("What do you want to name Player 1: "))
  NP2 = (input("What do you want to name Player 2: "))
  NP3 = (input("What do you want to name Player 3: "))
  NP4 = (input("What do you want to name Player 4: "))
  P1S = 0
  P2S = 0
  P3S = 0
  P4S = 0
  while game4 == True:
    P1P = int(input("How many points did " + str(NP1) + " make in this turn: "))
    P1S = P1S + P1P
    P2P = int(input("How many points did " + str(NP2) + " make in this turn: "))
    P2S = P2S + P2P
    P3P = int(input("How many points did " + str(NP3) + " make in this turn: "))
    P3S = P3S + P3P
    P4P = int(input("How many points did " + str(NP4) + " make in this turn: "))
    P4S = P4S + P4P
    GM = (input("is the game over: "))
    if GM.lower() == 'yes':
      print(str(NP1) + " has " + str(P1S) + " points")
      print(str(NP2) + " has " + str(P2S) + " points")
      print(str(NP3) + " has " + str(P3S) + " points")
      print(str(NP4) + " has " + str(P4S) + " points")
      if P1S > P2S and P1S > P3S and P1S > P4S:
        print(str(NP1) + " wins!")
        game4 = False
      elif P2S > P1S and P2S > P3S and P2S > P4S:
        print(str(NP2) + " wins!")
        game4 = False
      elif P3S > P1S and P3S > P2S and P3S > P4S:
        print(str(NP3) + " wins!")
        game4 = False
      elif P4S > P1S and P4S > P3S and P4S > P2S:
        print(str(NP4) + " wins!")
        game4 = False
      else:
        print("Draw!")
        sys.exit()
    elif GM.lower() == 'no':
      continue

print("Welcome to carrom counter. Turns are unlimited. (2, 3, or 4 player game)\n\n")
def ask():
  P = int(input("How many players(2, 3, 4): "))
  if P == 2:
    player2()
    sys.exit() 
  elif P == 3:
    player3()
    sys.exit()
  elif P == 4:
    player4() 
    sys.exit()
  else:
    ask()
ask()
