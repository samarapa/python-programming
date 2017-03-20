def find_replace(str1):
    snot = str1.find('not')
    spoor = str1.find('poor')
    if snot < spoor:
        str1 = str1.replace(str1[snot:(spoor + 4)],'good')
    return str1

print(find_replace('The lyrics is not that poor!'))
print(find_replace('The lyrics is not that!'))