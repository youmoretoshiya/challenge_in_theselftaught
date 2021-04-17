class Horse:
    def __init__(self, name, color, rider):
        self.name = name
        self.color = color
        self.rider = rider

class Rider:
    def __init__(self, name):
        self.name = name

john = Rider("John Lennon")
silver = Horse("Silver", "white", john)
print(silver.rider.name)
