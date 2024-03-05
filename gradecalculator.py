
print("Welcome to Grade Calculator!\n")
print("Please enter the following mandatory information:")



print("First and Second Name are mandatories. Try it again")
studentfullName = input("Student first and second name only: ")


countOfWords = len(studentfullName.split())
while countOfWords < 2 or countOfWords > 2:
    studentfullName = input("You have to enter only student's first and second name (mandatory)): ")
    countOfWords = len(studentfullName.split())

if not studentfullName.replace(" ", "").isalpha():
    print("The name has to have only alphabetic characters. Try again.")
    exit()



split_name = studentfullName.split()
first_Name = split_name[0]
second_Name = split_name[1]



score1 = input("Exame score 1 (out of 100): ")  
score2 = input("Exame score 2 (out of 100): ")
score3 = input("Exame score 3 (out of 100): ")
attendance = input("Attendance Percentage (out of 100): ")


check_values = score1 + score2 + score3 + attendance
if not check_values.isdigit():
    print("The scores and attendance have to be numbers. Try again.")
    exit()

score1 = int(score1)
score2 = int(score2)
score3 = int(score3)
attendance = int(attendance)




if score1 < 0 or score2 < 0 or score3 < 0 or attendance < 0:
    print("The score can not be less than 0. Try it again.")

elif score1 > 100 or score2 > 100 or score3 > 100 or attendance > 100:
    print("The score can not be more than 100, Try it again.")

else:
    scoreAverage = (score1 + score2 + score3) / 3

    first_inicial = first_Name[0].upper()
    second_inical = second_Name[0].upper()
    studentInitials = first_inicial + second_inical


    overallGrade = ""

    if attendance < 75:
        overallGrade = "F (due to low attendance)"

    elif scoreAverage >= 85:
        overallGrade = "A"

    elif scoreAverage >= 70:
        overallGrade = "B"
    
    elif scoreAverage >= 55:
        overallGrade = "C"

    elif scoreAverage >= 40:
        overallGrade = "D"
    
    else:
        overallGrade = "F"


    gpa = scoreAverage / 25       

    print(f"Average Exam Score: {scoreAverage}%")
    print(f"The student Initials: {studentInitials}")
    print(f"The student second name: {second_Name}")
    print(f"The student Overall: {overallGrade}")
    print(f"The student GPA: {gpa}")














