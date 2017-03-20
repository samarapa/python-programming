def upppercase(str1):
    u = 0
    if len(str1) > 4 :
        for l in str1[:4]:
            if l.upper() == l:
                u +=1
        if u >= 2:
            return str1.upper()
        else:
            return str1


print(upppercase("string"))
print(upppercase("sABtring"))
print(upppercase("AAAAAAAAAAAAkljfdslkfjlksdjfalkjdslkjflksdjflksd"))


