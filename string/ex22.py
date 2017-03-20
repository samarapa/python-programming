def lexicographi_sort(s):
    #return sorted(s)
        return sorted(sorted(s), key=str.upper)




print(lexicographi_sort('w3resource'))
print(lexicographi_sort('quickbrown'))