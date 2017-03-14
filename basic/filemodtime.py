import os.path,time

print("Created time:  %s" %time.ctime(os.path.getctime("C:/Senthil/spark.txt")))
print("Last Modifited time:  %s" %time.ctime(os.path.getmtime("C:/Senthil/spark.txt")))
