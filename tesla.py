from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from threading import *



class S(Thread):
    def run(self):
        count=0
        driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
        for i in range(0, 5):
            driver.get("https://google.com/")
            driver.maximize_window()
            x = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input')
            x.send_keys("How Tesla electric car beats Audi and Jaguar in efficiency test? Quora")
            x.send_keys(Keys.ENTER)
            y = driver.find_element_by_xpath('//*[@id="rso"]/div/div/div[1]/div/div/div[1]/a/h3')
            y.click()
            driver.execute_script("window.scrollTo(0, 500)")
            time.sleep(1)
            driver.execute_script("window.scrollTo(1000, 2000)")
            time.sleep(1)
            driver.execute_script("window.scrollTo(2500, 4000)")
            count = count + 1
            print(str(count)+"-first")
            time.sleep(3)


class SS(Thread):
    def run(self):
        count = 0
        driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
        for i in range(0, 50):
            driver.get("https://google.com/")
            driver.maximize_window()
            x = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input')
            x.send_keys("How Tesla electric car beats Audi and Jaguar in efficiency test? Quora")
            x.send_keys(Keys.ENTER)
            y = driver.find_element_by_xpath('//*[@id="rso"]/div/div/div[1]/div/div/div[1]/a/h3')
            y.click()
            driver.execute_script("window.scrollTo(0, 500)")
            time.sleep(1)
            driver.execute_script("window.scrollTo(1000, 2000)")
            time.sleep(1)
            driver.execute_script("window.scrollTo(2500, 4000)")
            count = count + 1
            print(str(count)+"-second")
            time.sleep(3)
t1=S()
t2=SS()

t1.start()
t2.start()

t1.join(t2)
driver=webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
time.sleep(10)

