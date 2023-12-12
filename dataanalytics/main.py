def contact():
    print("Contact details of the school\n Delhi Public School\n Bangalore Karnataka\n")


for i in range(2):
    user_inp =input("Name of the student: ")    
    maths = int(input("enter marks for Mathematics "))
    science = int(input("enter marks for Science "))
    print(f"Marks of {user_inp}")
    print(f"Marks for mathematics {maths}")
    print(f"Marks for Science {science}")
    contact()