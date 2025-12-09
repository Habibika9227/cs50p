#.Grading program.
score=int(input("Enter your grade: "))

if 90<=score<=100:
    print("Grade: A")

elif 80<=score<90:
    print("Grade: B")

elif score>=70 and score<80:
    print("Grade: C")

elif 60<=score<70:
    print("Grade: D")

else:
    print("grade: F")