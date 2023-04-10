
x = int(input("Please Enter 1st NO:"))
y = int(input("Please Enter 2nd NO:"))
sum = x + y
print('Your sum is', sum)
rem = sum % 2
if rem == 0:
    print("Even")
elif rem != 0 :
    print("Odd")
else :
    print("Wrong input")

