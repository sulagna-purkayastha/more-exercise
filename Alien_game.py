

import random
alive = True
stamina = 10
def report(stamin):
     if stamina > 8:
      print ("The alien is strong! It resists your pathetic attack!")
     elif stamina > 5:
      print ("With a loud grunt, the alien stands firm.")
     elif stamina > 3:
      print ("Your attack seems to be having an effect! The alien stumbles!")
     elif stamina > 0:
      print ("The alien is certain to fall soon! It staggers and reels!")
     else:
      print ("That's it! The alien is finished!")
def fight(stamina):
 while stamina > 0:
  response = input("> Enter a move 1.Hit 2.attack 3.fight 4.run")
  if "1" in response or "2" in response:
   less = random.randint(0, stamina)
   stamina -= less
   report(stamina)
  elif "3" in response:
   print ("Fight how? You have no weapons, silly space traveler!")
  elif "4" in response:
   print ("Sadly, there is nowhere to run."),
   print ("The spaceship is not very big.")
  else:
   print ("The alien zaps you with its powerful ray gun!")
   return True
 return False

print ("A threatening alien wants to fight you!\n")
alive = fight(stamina)

if alive==0:
 print ("Congrats!! Finally you killed the alien.")          
else:
 print ("Sorry!! Alien killed you.")