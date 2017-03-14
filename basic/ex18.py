
def sumvalues(n1,n2,n3):
    sum = n1+n2+n3
    if n1==n2==n3:
        sum = sum * 3
    return sum

print(sumvalues(1,2,3))
print(sumvalues(2,2,2))
