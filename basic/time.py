
days = int(raw_input("Enter the days :")) * 3600 * 24
hours = int(raw_input("Enter the hours :")) * 3600
minutes = int(raw_input("Enter the minutes :")) * 60
seconds = int(raw_input("Enter the seconds :"))

time=days+hours+minutes+seconds

print("Total Time : " + str(time))
