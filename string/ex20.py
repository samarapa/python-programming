def str_mul_4(str1):
    if (len(str1)%4 == 0):
        return str1[::-1]
    else:
        return str1

print(str_mul_4("Python23"))
