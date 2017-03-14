def histogram(lst):
    for i in lst:
        output=''
        times = i
        while ( times > 0):
            output += '*'
            times = times -1
        print(output)


histogram([2,3,4,5])
