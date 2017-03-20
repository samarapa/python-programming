def strip_chars(str,chars):
    return "".join(c for c in str if c not in chars)

print(strip_chars("Process finished with exit code 0",'ic'))