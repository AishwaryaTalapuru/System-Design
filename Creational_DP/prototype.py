class Ninja:
    def __init__(self, name=None, points=100):
        self.name = name
        self.points = points
    def punch(self, other):
        if self.points > 0 and other.points > 0:
            other.points -=20
        else:
            print("Can't punch ", other.name)
    def kick(self, other):
        if self.points > 0 and other.points > 0:
            other.points -=50
            print(self.name, " points are ", self.points)
            print(other.name, " points are ", other.points)
        else:
            print("Can't kick ", other.name)
ninja1 = Ninja("Ninja1")
ninja2 = Ninja("Ninja2")
ninja1.kick(ninja2)
ninja2.punch(ninja1)
ninja1.kick(ninja2) 
ninja1.punch(ninja2) 
ninja2.kick(ninja1)