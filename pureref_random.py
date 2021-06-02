import sys
import os
import random
from PIL import Image
import subprocess
import random
from fuzzywuzzy import fuzz, process

# PureRef LOCATION
user_path = os.environ['USERPROFILE']

image_quantity = input("How many images will you add?? 🔢:  ")

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
file_chosen = random.sample(files_list, int(image_quantity))
# print("file CHOSEN ❗❗", file_chosen)
A = []
for x in file_chosen:
    A.append("\"" + x + "\"")
image_list = " ".join(A)
# Get program files path from env var
program_files = os.environ['PROGRAMFILES']
pureref_path = os.path.join(program_files, 'PureRef\\PureRef.exe')
command = pureref_path + ' - load ' + image_list
# print("command!!💻", command)
subprocess.Popen(command)

raise SystemExit
