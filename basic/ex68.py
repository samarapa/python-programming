
number = int(raw_input("Enter the digit"))
sum=0
while number !=0:
    x = number%10
    y = number/10
    sum +=x
    number = y
print("Sum of Digits : %s", sum)