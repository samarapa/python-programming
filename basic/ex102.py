import subprocess

ret_tex=subprocess.check_output("dir",shell=True,universal_newlines=True)
print (ret_tex)