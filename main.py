print('''
                             ___....___
                     __..-:'':__:..:__:'':-..__
                 _.-:__:.-:'':  :  :  :'':-.:__:-._
               .':.-:  :  :  :  :  :  :  :  :  :._:'.
            _ :.':  :  :  :  :  :  :  :  :  :  :  :'.: _
           [ ]:  :  :  :  :  :  :  :  :  :  :  :  :  :[ ]
           [ ]:  :  :  :  :  :  :  :  :  :  :  :  :  :[ ]
  :::::::::[ ]:__:__:__:__:__:__:__:__:__:__:__:__:__:[ ]:::::::::::
  !!!!!!!!![ ]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!![ ]!!!!!!!!!!!
  ^^^^^^^^^[ ]^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^[ ]^^^^^^^^^^^
           [ ]                                        [ ]
           [ ]                                        [ ]
           [ ]                                        [ ]
   ~~^_~^~/   \~^-~^~ _~^-~_^~-^~_^~~-^~_~^~-~_~-^~_^/   \~^ ~~_ ^
''')
print("Welcome to The TOON.")
print("Lets gan on the lash!.") 

player1_name = input("Enter your name...\n")
how_much_cash = input("How much cash have ye got mate? 10, 40 or 100\n")
notes = int(how_much_cash)
if notes == 10:
  print("Are yee a smoggie like?")
elif notes == 40:
  print("haway then")
elif notes == 100:
  print("oooooh looks like we have a southerner! shine ya shoes guvnor!?")
else:
  print("alright soft-shite, play the game or divint stop off at the toon ya Makem!")



print(f"Ok {player1_name}, you have just got off the train and exited Central Station, do you exit Left or Right?")
central = input("L or R\n" )
central = central.lower()
if central == "l":
   print("You've just met Brian Pince, begging do you... ")
brian = input("A- give him some money, B-Ignore him or C- tell him you have no change?\n")
if brian.lower() == "a":
    print("You spend 20mins trying to get away from Brian, In that time, his 'friends' have pickpocked you and you are now broke and in Newcastle with no money...Well done!")
    notes = 0
 
if brian.lower() == "b":
    print("Well done, you've managed to get away from 1 scallywag but keep your wits about you, there's plenty more about!")
elif brian.lower() == "c":
      print("we both know thats a bare-faced lie but well done! now lets get away as quickly as possible!")

gay_or_straight = input("where are you going to go right to that new bar or straight ahead?\n press n for new bar or s for straight ahead!")
if gay_or_straight.lower() == "n":
  print("you have a few drinks its ok, people keep going on about 'Gotham', do you to have another here or move on?\n")
  notes -= 5
  move_on = input("another or move on?\n A or M")
  if move_on.lower() == "a":
    notes -= 10
  elif move_on.lower() == "m":
    print("where next?")
  where_next1 = input("right and where you would have gone if straight forward or along and left\n")
elif gay_or_straight.lower() == "s":
  print("You start walking and come up to the LIFE Centre, take a left into TIMES square or have a drink in that pub across the road with pictures of 'Prince' and 'David Bowie' on it?")
  lifeOrDeathAndBowie = input("Type 'L' for life or 'D' for pub")
  if lifeOrDeathAndBowie.lower() == "l":
    print("Ok we are in times square and we've spent far too long without a drink in Newcastle are you Geordie or a Southerner!?")
    print("You're in Rustys now and you're drinking a Stella out of a can")
    notes -= 2
  elif lifeOrDeathAndBowie.lower() == "d":
    print("Ok you're in a indie bar, is this what you thought the toon was going to be like? No, get out and let the locals enjoy it")
    print("You've bought a drink now, just drink it and ask where the Big Market is\n ")
  big_market_or_Life = input("Are you going to go across the road and to the LIFE centre or find the Big Market? press L for LIFE or B for Big Market?\n ")
  if big_market_or_Life.lower() == "b":
    print("Oi Oi this is what you came for! Was that someone being sick in a traffic cone and then wearing it as a hat?! HEY LOOK! There's a girl with a mini skirt on kicking the shit out of a bloke!")
    print("")