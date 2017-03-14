def countlist(lst):
    count =0
    for l in lst:
        if l == 4:
            count += 1
    return count



print(countlist([1, 4, 6, 7, 4]))
print(countlist([1, 4, 6, 7, 4,4,4,4,4,4,4,4,4])) 
