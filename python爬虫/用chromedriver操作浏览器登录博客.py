# 本地Chrome浏览器设置方法
from selenium import  webdriver
import time
url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php?checkemail=registered'

driver = webdriver.Chrome() 
driver.get(url) 
time.sleep(2)

username=driver.find_element_by_id("user_login")
username.send_keys("tjt")
password=driver.find_element_by_id("user_pass")
password.send_keys("jtj456.-+")
button1=driver.find_element_by_id("wp-submit")
button1.click()

driver.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/')
time.sleep(2)
title=driver.find_element_by_id("post-13").find_element_by_class_name("entry-title")
title.click()

driver.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_01/')
time.sleep(2)
comment=driver.find_element_by_id("comment")
comment.send_keys("seleniumhahahah")
button2=driver.find_element_by_class_name("submit")
button2.click()

driver.close()

