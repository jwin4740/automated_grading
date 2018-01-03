import time
import os
import re
from getpass import getpass
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class Make_repos():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_names(self):
        name_list = []
        res = open("studentsGithub.txt", "r")
        content = res.readlines()
        for entry in content:
            n = entry.split(" ")
            student_dict = {
                "name": n[0],
                "username": n[1].strip()
            }
            name_list.append(student_dict)
        return name_list

    def link(self, user):
        url = "https://github.com/" + user + "?tab=repositories"
        return url

    def login(self):
        self.driver.get("https://github.com/login")
        user = "jwin4740"
        passwd = "47bughouse"
        formone = self.driver.find_element_by_xpath('// *[ @ id = "login_field"]')
        formone.send_keys(user)
        formpass = self.driver.find_element_by_xpath('// *[ @ id = "password"]')
        formpass.send_keys(passwd)

        menu = self.driver.find_element(By.XPATH, '//*[@id="login"]/form/div[4]/input[3]')
        actions = ActionChains(self.driver)
        actions.move_to_element(menu)
        actions.click(menu)
        actions.perform()
        time.sleep(2)

    def grab_creds(self):
        return self.driver.execute_script('''
        var arr = [];
        for (let i = 0; i < 9; i++){
            var k = document.getElementsByClassName("d-inline-block mb-1")[i].getElementsByTagName("a")[0].href;
            arr.push(k);
        }
        return arr;
        ''')

    def clone_into_dir(self, student, repos):
        path = os.getcwd() + "/mystudents/" + student["name"]
        for repo in repos:
            gitCmd = "git clone " + repo + ".git"
            output = subprocess.Popen(gitCmd, cwd=path, shell=True, stdout=subprocess.PIPE).communicate()[0]
            print output
            print "--------------------------------------------------"

    def get_repos(self):
        my_students = self.get_names()
        print my_students

        self.login()
        for x in my_students:
            self.driver.get(self.link(x["username"]))
            time.sleep(2)
            repos = self.grab_creds()
            self.clone_into_dir(x, repos)


Make_repos().get_repos()
