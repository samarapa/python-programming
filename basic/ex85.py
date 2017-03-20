import os



path=(raw_input("Enter the path : "))

if (os.path.isdir(path)):
    print "Its a directory"
elif (os.path.isfile(path)):
    print "Its is file"