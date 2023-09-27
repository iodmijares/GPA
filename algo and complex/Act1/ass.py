from student import Student
students = []

while True:
    ask = input("What you want to do?\nA.ADD \nB.List \nC.Exit \n\n").strip().upper()
    if ask == "A": 
            numStud = int(input("Enter number of students: "))
            numCount = int(input("Enter number of grades: \n"))

            for i in range(numStud):
                name = input("Enter name:\n ")
                grades = []
                for j in range(numCount):
                    grade = float(input(f"Enter grade {j + 1}: \n"))
                    grades.append(grade)
                s = Student(name, grades)
                students.append(s)
                print()
                
                
    elif ask == "B":
        if not students:
            print("No data exist")
        else:
            for student in students:
                print("-----------------------")
                print(f"Name: {student.getName()}")
                print(f"Grades: {student.getGrades()}") 
                print(f"Average Grade: {student.getAverage()}\n")
                
                ask = input(ask)
                
    elif ask == "C":
            exit()       
    else:
            print("Invalid key")