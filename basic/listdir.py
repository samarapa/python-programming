from os import listdir
from os.path import isfile,join

file_list = [f for f in listdir("C:/Senthil") if isfile(join("C:/Senthil",f))]
print(file_list)
