def insert_sting_middle(str1, s1):
    return (str1[:2] + s1 + str1[2:])

print(insert_sting_middle('[[]]', 'Python'))
print(insert_sting_middle('{{}}', 'PHP'))
print(insert_sting_middle('<<>>', 'HTML'))  