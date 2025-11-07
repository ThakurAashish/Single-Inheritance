class animal :
    def __init__(self, name , species) -> None:
        self.name =name
        self.species =species

    def makeSound(self):
        print("sound made by animal")

class Dog(animal):
    def __init__(self, name, breed) -> None:
        animal.__init__(self,name,species ="Dog")
    
    def makeSound(self):
       print("Brak")

d =Dog("Dog","Doggerman")
d.makeSound()

a = animal("Dog", "Dog")
a.makeSound()