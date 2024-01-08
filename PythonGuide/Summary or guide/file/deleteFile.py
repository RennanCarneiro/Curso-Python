import os
import shutil

path = 'test.txt'

try:
    os.remove(path) #delete a file
    #os.rmdir(path) #delete a file or empty folder
    #shutil.rmtree(path) #delete files and or folders |dangerous pay attention|
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("That folder contains files")
else:
    print(path+ " deletion was succesful")