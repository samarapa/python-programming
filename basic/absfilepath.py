import os
def absfilepath(path):
    return os.path.abspath(path)

print("Absoulate Path: " + absfilepath("spark.txt"))
