#task 1

import os
 
path = "lab6\dir-and-files"
dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
 
print(dir_list)


#task 2

import os

print('Exist:', os.access('lab6\dir-and-files', os.F_OK))
print('Readable:', os.access('lab6\dir-and-files', os.R_OK))
print('Writable:', os.access('lab6\dir-and-files', os.W_OK))
print('Executable:', os.access('lab6\dir-and-files', os.X_OK))



#task 3

import os

path = r"lab6\dir-and-files"

print(os.path.exists(path))
print(os.path.basename(path))
print(os.path.dirname(path))



#task 4

def lines(fname):
        with open(fname) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1
print("Number of lines:",lines("sample.txt"))


#task 5

items = ["I", "am", "sigma"]
file = open('sample.txt','w')
for item in items:
	file.write(item+"\n")
file.close()


#task 6

import string

import os

if not os.path.exists("letters"):
   os.makedirs("letters")
   
for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)


#task 7

with open("sample.txt") as f:
    with open("A.txt", "w") as f1:
        for line in f:
            f1.write(line)


#task 8

import os
if os.path.exists("deleted.txt"):
  os.remove("deleted.txt")
else:
  print("The file does not exist")