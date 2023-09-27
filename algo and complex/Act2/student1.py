class Student:
    def __init__(self, name, g1,g2,g3,g4):
        self.name = name
        self.g1 = g1
        self.g2 = g2
        self.g3 = g3
        self.g4 = g4
        
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def G1(self):
        return self.g1
    def average(self):
        total = self.g1 + self.g2 + self.g3 + self.g4
        return total/4