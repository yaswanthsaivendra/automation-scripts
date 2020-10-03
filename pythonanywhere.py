from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='F:\chromedriver_win32\chromedriver.exe')

driver.get('http://grroott.pythonanywhere.com/')

driver.maximize_window()

driver.find_element_by_xpath('//*[@id="id_username"]').click()
driver.find_element_by_xpath('//*[@id="id_username"]').send_keys("xxxxx")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="id_password"]').click()
driver.find_element_by_xpath('//*[@id="id_password"]').send_keys("xxxxx")
time.sleep(2)

driver.find_element_by_xpath('/html/body/main/div/div[1]/div/form/div/button').click()
time.sleep(2)


for i in range(1, 3):

    driver.find_element_by_xpath('//*[@id="navbarToggle"]/div[2]/a[1]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="id_title"]').click()
    driver.find_element_by_xpath('//*[@id="id_title"]').send_keys('Post by Bot')
    time.sleep(2)
    driver.find_element_by_xpath('/html/body').click()
    time.sleep(2)
    frame = driver.find_element(By.CLASS_NAME, 'cke_wysiwyg_frame')
    driver.switch_to.frame(frame)
    body = driver.find_element(By.TAG_NAME, 'body')
    body.send_keys('An Internet bot, web robot, robot or simply bot, is a software application that runs automated tasks over the Internet. Typically, bots perform tasks that are simple and repetitive, much faster than a person could.')
    time.sleep(2)
    driver.switch_to.default_content()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/main/div/div[1]/div/form/div/button').click()

    driver.find_element_by_xpath('/html/body/main/div/div[1]/article/div/div/div/a[2]').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/main/div/div[1]/div/form/div/button').click()
    time.sleep(10)
    print(str(i) + " - Success!")
driver.close()