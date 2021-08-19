print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

alive = True



firstChoice= input("You find yourself in a dark chasm. You are looking for a way out. \nYou are at an intersection. Cobblestone pathways lead left and right. \nAhead, light from your torch illuminates a glossy stone wall. \nWould you like to go left or right?:  \n").upper()

if firstChoice == "RIGHT":
  print("You have died.")
  alive = False
elif firstChoice != "LEFT":
  firstChoice = input("Try again, left or right: ")
  alive = False #delete this when reset implemented
  #Send user back to the start
else:
  print("You walk for a long distance through the stone hallway until you enter a new chasm. \n You feel a cool breeze. You can't see the end of the chasm ahead. \n All that lies ahead is a silent lake of water.")

if alive:
  secondChoice = input("You look ahead into the lake and ponder your options. \nYou could hope for someone to bring a boat or another way across the lake. \n Or turnabout and try to see what was down the other hallway. \n Or you could try to swim across the dark lake, sacrificing your torch in the process. \n Do you want to WAIT, RETURN, or SWIM?: \n").upper()

if alive:
  if secondChoice == "SWIM":
    print("You have died.")
    alive = False
  elif secondChoice =="RETURN":
    print("You went back and died")
    alive = False
  elif secondChoice != "WAIT":
    print("What was that? WAIT, RETURN, or SWIM?: ")
    alive = False #delete this when reset implemented
    #Reset the second choice
  else:
    print("After a surprisingly short wait, a rowboat appears.\n As the rowboat nears shore you see there is nobody on board. \n The oars of the rowboat seem to be moving themselves. \n The contraption lets out a horrific hissing noise and expels a jet of steam \nas it slowly approaches your location.\n You board the strange beast and drift asleep as it begins to turn and propel you elsewhere. \n Some time later, you awake to find the boat has stopped moving. \n You lift your head to see the rowboat has shored near another cobblestone wall. \n Ahead, you see three stone archways leading down three paths. \n Between the archways and all around, \neverything is enclosed in glossy stone walls save for the calm lake behind. \n You disembark your boat and approach the three archways. \n They have been painted in three distinctive, vibrant colors. \n To the left, a cherry red archway. \nIn the middle, a banana yellow archway. \nTo the right, a blueberry colored archway.")

if alive:
  thirdChoice = input("Which archway will you pass? RED, YELLOW, or BLUE?:  \n").upper()

if alive:
  if thirdChoice =="RED":
    print("lol Red = ded")
    alive=False
  elif thirdChoice =="YELLOW":
    print("BEEEEEEES")
    alive = False
  elif thirdChoice =="GREEN":
    print("Green is the color of envy. \nYou fall through a plot hole \n And land on a pile of $CASH$. \n You win?")
  elif thirdChoice !="BLUE":
    print("You got to the third choice and still haven't figured out what to type.\n We all lose.")
  else:
    print("You won, a brand new CAR! (In the game (Which means you actually won the game))")
