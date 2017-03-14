import platform
import os
import multiprocessing

print(os.name)
print(platform.system())
print(platform.release())

print(multiprocessing.cpu_count())
