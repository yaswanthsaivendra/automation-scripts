
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
import time
from threading import *



count = 0
count1=0
driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
for i in range(0, 5):
    try:
        driver.get("https://www.google.com/")
        driver.maximize_window()
        x = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input')
        x.send_keys('What is the difference between “ls” command and “ls -lart” command in Linux?')
        x.send_keys(Keys.ENTER)
        time.sleep(1)
        y = driver.find_element_by_xpath('//*[@id="rso"]/div/div/div[1]/div/div/div[1]/a/h3')
        y.click()
    except NoSuchElementException:
        print ("Element not found")
        time.sleep(1000)
        count1=count1+1

    except NoSuchWindowException:
        driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
        print("skipped")
        pass
    except WebDriverException:
        driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
        print("skipped")
        pass
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(2)
    driver.execute_script("window.scrollTo(500, 1000)")
    time.sleep(2)
    driver.execute_script("window.scrollTo(1000, 1500)")
    time.sleep(2)
    driver.execute_script("window.scrollTo(1500, 2000)")
    count = count + 1
    print(str(count)+'-third')
    if count1>3:
        print("Check internet connection")
        exit()
    time.sleep(2)
    #driver.close()
