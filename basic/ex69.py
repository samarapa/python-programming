v1 = int(raw_input("Enter the first number"))
v2 = int(raw_input("Enter the Sec number"))
v3 = int(raw_input("Enter the 3rd number"))

r1 = min(v1,v2,v3)
r3 = max(v1,v2,v3)

r2=(v1+v2+v3) - r1 - r3

print ("Sorted List : " , r1,r2,r3)
