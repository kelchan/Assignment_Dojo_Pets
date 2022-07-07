from asyncio.proactor_events import _ProactorBaseWritePipeTransport


class Ninja:
    def __init__( self, first_name, last_name, pet, treats, pet_food ):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
    def walk( self ):
        print( f"Walking {self.pet.name}!")
        self.pet.play()
        return self
    def feed( self ):
        print( f"Feeding {self.pet.name} some {self.pet_food}!")
        self.pet.eat()
        return self
    def bathe( self ):
        print( f"Bathing {self.pet.name}!" )
        self.pet.noise()
        return self


class Pets:
    def __init__( self, name, type, tricks, health, energy ):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
    def sleep( self ):
        print( f"{self.name} is sleeping...")
        self.energy += 15
        return self
    def eat( self ):
        print( f"{self.name} is eating...")
        self.energy += 5
        self.health += 10
        return self
    def play( self ):
        print( f"{self.name} is playing...")
        self.health += 5
        return self
    def noise( self ):
        print( f'{self.name} says WOOF!' )

pet1 = Pets( "Kumo", "dog", "sit", 100, 50 )
owner1 = Ninja( "Kelvin", "Chan", pet1, "bacon", "kibble" )
print( owner1.first_name )
print( owner1.pet.name )
owner1.feed().walk().bathe()