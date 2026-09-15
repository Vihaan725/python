class parrot:
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age
bird = parrot("Ben", 15)
print("The birds name is", bird.name)
print("The birds age is", bird.age)