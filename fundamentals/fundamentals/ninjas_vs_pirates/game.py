from classes.ninja import Ninja
from classes.pirate import Pirate
import random

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

print("You are a ninja sneaking up on a pirate!")

while michelangelo.health > 0 and jack_sparrow.health > 0 :
    response = ""
    while not response == "1" and not response == "2":
        response = input("What do you want to? 1) Attack 2) Hide \n >>>")
        if response == "1":
            michelangelo.attack(jack_sparrow)
        elif response == "2":
            michelangelo.hide(jack_sparrow)
        else:
            print("That's not an option!!!")
    jack_sparrow.show_stats()        
    
    pirate_response = random.randint(1,2)
    if pirate_response == 1 and not response == "2":
        jack_sparrow.attack(michelangelo)
    elif pirate_response == 2 and not response == "2":
        jack_sparrow.pistol_attack(michelangelo)
    else:
        print("You successfully hid!")
    michelangelo.show_stats()

if michelangelo.health > 0:
    print("Congrats! You're a real ninja!!!")
elif jack_sparrow.health <= 0:
    print("You tied! Better luck next time!")
else:
    print("Obviously you're not a real ninja!")




michelangelo.attack(jack_sparrow)
jack_sparrow.show_stats()