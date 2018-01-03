import os

res = open("studentsGithub.txt", "r")
content = res.readlines()
curr_dir = os.getcwd() + "/mystudents/"
for entry in content:
    tempList = entry.split(" ")
    folder = tempList[0]
    os.mkdir(curr_dir + folder)
