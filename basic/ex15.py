import math

def volumesphere(r):
    v= 4.0/3.0 * math.pi * r**3
    print("Volume of Sphere " + str(v))
    print(math.pi)   

r=float(raw_input("Enter the radius: "))

volumesphere(r)
