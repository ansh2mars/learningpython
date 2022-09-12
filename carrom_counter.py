print("Welcome to carrom counter. Turns are unlimited. (2 player game)\n\n")
game = True
NP1 = (input("What do you want to name Player 1: "))
NP2 = (input("What do you want to name Player 2: "))
P1S = 0
P2S = 0
while game == True:
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
    elif P1S < P2S:
      print(str(NP2) + " wins!")
      game = False
    else:
      print("Draw!")
  elif GM.lower() == 'no':
    continue  