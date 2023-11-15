# errors detected during execution are called Exceptions.

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


## 1.
a=5
b=0
try:
    result=a/b
    
except ZeroDivisionError:
    result ="You can't divide by 0"
print(result)
# 2.

#Type your answer below.

a="Hello World!"
try:
    a + 10
except BaseException as e:
    msg="You can't add int to string"


print(msg)

# 3.

#Type your answer below.

lst=[5, 10, 20]

try:
    print(lst[5])
except IndexError:
    msg="You're out of list range"


print(msg)