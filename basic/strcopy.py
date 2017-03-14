def strcopy(s,n):
    result = ""
    if (len(s) >= 2):
        substr = s[:2]
    else:
        substr = s
    for i in range(n):
        result += substr

    return result

print(strcopy("abcd",10))
print(strcopy("a",5))
        
            
        
