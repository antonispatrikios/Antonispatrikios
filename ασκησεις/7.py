import random

game = [0,1,2,3,4,5,6,7,8]

def gameboard():
  print game[0],"|",game[1],"|",game[2]
  print "-- --- --"
  print game[3],"|",game[4],"|",game[5]
  print "-- --- --"
  print game[6],"|",game[7],"|",game[8]

def Row(char, a, b, c):
  if game[a] == char and game[b] == char and game[c] == char:
    return True

def Winner(char):
  if Row(char, 0, 1, 2):
    return True
  if Row(char, 3, 4, 5):
    return True
  if Row(char, 6, 7, 8):
    return True
  if Row(char, 0, 3, 6):
    return True
  if Row(char, 1, 4, 7):
    return True
  if Row(char, 2, 5, 8):
    return True
  if Row(char, 0, 4, 8):
    return True 
  if Row(char, 2, 4, 6):
    return True

find = False

while not find:

  select = int(input("dialekste thn thesh: "))
  
  if game[select] != "x" and game[select] != "o":
    game[select] = "x"

    if Winner("x") == True:
      gameboard()
      print "!!-YOU-WIN-!!"
      find = True
      break;
    
    while True:
      random.seed()
      enemy = random.randint(0,8)

      if game[enemy] != "o" and game[enemy] != "x":
        game[enemy] = "o"

        if Winner("o") == True:
          gameboard()
          print "!!-ENEMY-WINS-!!"
          find = True
          break;

        break;

  else:
    print "H thesh auth einai piasmenh!"
  
  gameboard()
