# def contact():
#     print("Contact details of the school\n Delhi Public School\n Bangalore Karnataka\n")


# for i in range(2):
#     user_inp =input("Name of the student: ")    
#     maths = int(input("enter marks for Mathematics "))
#     science = int(input("enter marks for Science "))
#     print(f"Marks of {user_inp}")
#     print(f"Marks for mathematics {maths}")
#     print(f"Marks for Science {science}")
#     contact()

## eleceticity


def  electricity_bill(unit_used):
    if unit_used <= 500:
        print("Your bill is ", unit_used * 5)
    elif unit_used > 500 and unit_used <= 700:
        print("Your bill is ", unit_used * 10)
    elif unit_used > 700 and unit_used <= 1000:
        print("Your bill is ", unit_used * 15)  
    elif unit_used > 1000 :
        print("Your bill is ", unit_used * 20)   

for i in range(1):
    user_name = input("Enter the name : ")
    unit_used = int(input("Enter the unit used: "))
    electricity_bill(unit_used)