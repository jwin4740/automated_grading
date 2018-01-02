import os

res = open("studentsGithub.txt", "r")
content = res.readlines()
curr_dir = os.getcwd() + "/"
for entry in content:
    folder = entry.split(" ")[0]
    os.mkdir(curr_dir + folder)
    
