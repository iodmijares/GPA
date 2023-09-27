class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def getGrades(self):
        return self.grades

    def getAverage(self):
        total = sum(self.grades)
        return total / len(self.grades)
