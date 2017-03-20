import glob
import os

files=glob.glob("C:\\Senthil\\*.txt")
files.sort(key=os.path.getmtime)
print("\n".join(files))