import collections
def rep_count():
    str1='thequickbrownfoxjumpsoverthelazydog'
    d = collections.defaultdict(int)

    for c in str1:
        d[c] +=1

    for s in sorted(d, key=d.get,reverse=True):
        if (d[s] > 1):
            print("{} : {}".format(s,d[s]))


rep_count()