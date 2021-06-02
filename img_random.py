import sys
import os
import random
from PIL import Image
import subprocess
import shutil
import random
from fuzzywuzzy import fuzz, process

# PureRef LOCATION
user_path = os.environ['USERPROFILE']

image_quantity = input("How many images will you open?? 🔢:  ")

if not len(sys.argv) > 1:
    basedir = os.getcwd()
    print("🤷🏽 We DON'T have basedir, using current dir ➡", basedir)
elif sys.argv[1] == ".":
    basedir = os.getcwd()
    print("👇🏽 Got it! Using current dir ➡", basedir)
else:
    basedir = sys.argv[1]
    print("🙌 We have path! Added to var! ➡", basedir)

files_list = []
for root, dirs, files in os.walk(basedir):
    for file in files:
        if file.endswith(".jpeg") or file.endswith(".png") or file.endswith(".mp4") or file.endswith(".jfif") or file.endswith(".jpg") or file.endswith(".gif"):
            files_list.append(os.path.join(root, file))

# print 20 random images
files_chosen = random.sample(files_list, int(image_quantity))
 
print("file LIST 📃 ", files_chosen)  # prints the random filename
#image_var = files_chosen[0]
print("type of FILES_CHOSEN OUTSIDE LOOP:", type(files_chosen))
for item in files_chosen:
    print("type of FILES_CHOSEN IIIIINSIDE LOOP:", type(files_chosen))
    item = "\"" + item + "\""
    print("grabbing img...", item)
    #command = 'Start-Process'+' '+item
    #print("command!!💻", command)
    subprocess.run(os.system(item))

print("finished!💥")
raise SystemExit
