class Ninja:
    def __init__(self,first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    
    def walk(self, pet):
        print (f"{self.first_name} is walking {self.pet.name}")
        pet.play()

    def feed(self, pet):
        print (f"{self.first_name} is feeding {self.pet.name}")
        pet.eat()

    def bathe(self, pet):
        print (f"{self.first_name} is giving {self.pet.name} a bath")
        pet.noise()

# implement __init__( first_name , last_name , treats , pet_food , pet )
    	
    
# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
# feed() - feeds the ninja's pet invoking the pet eat() method
# bathe() - cleans the ninja's pet invoking the pet noise() method

class Pet:
    def __init__(self, name, type, tricks, sound):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.sound = sound
        self.energy = 50
        self.health = 100
        pass

    def sleep(self):
        print (f"{self.name} is sleeping")
        self.energy += 25

    def eat(self):
        print (f"{self.name} is eating. Nom Nom Nom!")
        self.energy += 5
        self.health += 10

    def play(self):
        print (f"{self.name} is playing")
        self.health += 5

    def noise(self):
        print (f"{self.sound}!!!")
# implement __init__( name , type , tricks ):
# implement the following methods:
# sleep() - increases the pets energy by 25
# eat() - increases the pet's energy by 5 & health by 10
# play() - increases the pet's health by 5
# noise() - prints out the pet's sound

pet1 = Pet("Mr.Bibblesworth", "Hairless Cat", "Cat stuff", "Roar")
print (f"Name: {pet1.name}, Type: {pet1.type}, Tricks: {pet1.tricks}, Sound: {pet1.sound}")

ninja1 = Ninja("Leeroy", "Jenkins", "Snausages", "Meowmix", pet1)
print (f"Name: {ninja1.first_name} {ninja1.last_name}, Treats: {ninja1.treats}, Pet food: {ninja1.pet_food}, Pet: {ninja1.pet.name}")

pet2 = Pet("Baxter", "Mutt", "Eating a whole wheel of cheese", "Bork Bork Bork")

ninja2 = Ninja("Daniel", "Larusso", "Crane Kicks", "Wheel-o-cheese", pet2)

ninja1.feed(pet1)

ninja1.bathe(pet1)

ninja1.walk(pet1)

ninja2.feed(pet2)

ninja2.walk(pet2)

ninja2.bathe(pet2)