def str_op(str1):


    if (len(str1) >= 2):
        str_1st = str1[:2]
        str_last = str1[-2:]
        return str_1st + str_last
    else:
        return ''

print(str_op("w3resource"))
print(str_op("w3"))
print(str_op("w"))