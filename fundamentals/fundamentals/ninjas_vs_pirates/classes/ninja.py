class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        pirate.health -= self.strength
        print(f"{self.name} has just attacked {pirate.name} with a throwing star")
        return self

    def hide(self, pirate):
        pirate.health -= self.strength / 2
        print(f"{self.name} hid from {pirate.name}'s attack. So {self.name}'s health remains at {self.health}. {pirate.name} takes damage from embarrassment!")