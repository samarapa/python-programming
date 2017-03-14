def appendIs(s):
    if (len(s) >= 2 and s[:2] =="Is"):
        return s
    else:
        return "Is" + s


print(appendIs("Kumar"))
print(appendIs("IsSenthil"))
print(appendIs("Is"))
