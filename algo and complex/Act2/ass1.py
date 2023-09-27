
from student1 import Student

students = []

while True:
    ask = input('Enter you want to do?\nA.Add\nB.List\nC.Exit\n').strip().upper()
    
    match ask:
        case "A":
            numStud = int(input("Enter number of students\n"))
            for i in range (numStud):
                name = input("Enter name: \n")
                g1 = int(input("Enter grade 1: "))
                g2 = int(input("Enter grade 2: "))
                g3 = int(input("Enter grade 3: "))
                g4 = int(input("Enter grade 4: "))
                s = Student(name, g1,g2,g3,g4)
                students.append(s)
                print()
        case "B": 
            if not students:
                print("No data")       
            for student in students:
                print(f"{student.getName()}")
                print()
                print(f"{student.average()}")
                print("-----------------")
        case "C":
            exit()
        case _:
            print("Invalid key")