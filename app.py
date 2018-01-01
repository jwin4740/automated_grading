import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSc_q0CSp5Bpn7lfDAdoPCbBTW-OxWQVhC3gG5P9e6iE4FERjw/viewform")
print(driver.current_url)
student_name = driver.find_element(By.XPATH, '//form/div/div[2]/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/input')
student_class_code = driver.find_element(By.XPATH, '//form/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/input')
student_email = driver.find_element(By.XPATH, '//form/div/div[2]/div[2]/div[3]/div[2]/div/div[1]/div/div[1]/input')
student_github = driver.find_element(By.XPATH, '//form/div/div[2]/div[2]/div[4]/div[2]/div/div[1]/div/div[1]/input')
student_name.send_keys("hello world")
student_class_code.send_keys("code")
student_email.send_keys("myemail")
student_github.send_keys("gituser")

menu = driver.find_element(By.XPATH, '//form/div/div[2]/div[3]/div[1]/div/div')
actions = ActionChains(driver)
actions.move_to_element(menu)
actions.click(menu)
actions.perform()
time.sleep(2)
print(driver.current_url)


