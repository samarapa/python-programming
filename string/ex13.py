def up(str1):
    return str1.upper()

def low(str1):
    return str1.lower()

def up_low(str1):

    return up(str1) + "  : " + low(str1)

print(up_low("Senthil"))