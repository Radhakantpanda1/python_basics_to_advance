# constrol flow or conditional
age_of_user=int(input("Enter your age-"))
if age_of_user<=18:
    print("You are under age")
else:
    print("You are eligible")

# make a student mark grading system
user_marks=int(input("Enter your marks-"))
if user_marks<=100 and user_marks>=0:
    if user_marks>90 and user_marks <=100:
        print('Grade-A')
    elif user_marks>80 and user_marks<=90:
        print('Grade-B')
    elif user_marks>70 and user_marks<=80:
        print('Grade-C')
    else:
        print('Grade-F')
else:
    print('Invalid marks')