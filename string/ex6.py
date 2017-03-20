def append(str1):
    lgth = len(str1)
    if (lgth >=3):
        if (str1[-3:] == 'ing'):
            return str1[:lgth-3] + 'ly'
        else:
            return str1 + 'ing'
    else:
        return str1

print(append("w3"))
print(append("w3ing"))
print(append("w3ly"))


