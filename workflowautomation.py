from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import *
from threading import *



class S(Thread):
    def run(self):
        count=0
        count1=0
        driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
        for i in range(0,500):
            try:

                driver.get("https://duckduckgo.com/")
                driver.maximize_window()
                x=driver.find_element_by_xpath('//*[@id="search_form_input_homepage"]')
                x.send_keys("What is workflow automation? Can you list some of the tools?")
                x.send_keys(Keys.ENTER)
                y=driver.find_element_by_xpath('//*[@id="r1-0"]/div/h2/a[1]')
                y.click()
                count1 = 0
            except NoSuchElementException:
                print("Element not found")
                Keys.F5
                count1 = count1 + 1
                time.sleep(15)

            except NoSuchWindowException:
                driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
                print("skipped")
                pass
            except WebDriverException:
                driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
                print("skipped")
                pass
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, 500)")
            time.sleep(2)
            driver.execute_script("window.scrollTo(500, 1000)")
            time.sleep(2)
            driver.execute_script("window.scrollTo(1000, 1500)")
            time.sleep(2)
            driver.execute_script("window.scrollTo(2000, 2500)")
            time.sleep(2)
            driver.execute_script("window.scrollTo(2000, 2500)")
            count = count + 1
            print(str(count) + '-first')
            if count1 > 2:
                print("Check internet connection")
                #exit()
            time.sleep(1)
            #driver.close()

class SS(Thread):
    def run(self):
        count = 0
        count1=0
        driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
        for i in range(0, 500):
            try:

                driver.get("https://duckduckgo.com/")
                driver.maximize_window()
                x = driver.find_element_by_xpath('//*[@id="search_form_input_homepage"]')
                x.send_keys("What is workflow automation? Can you list some of the tools?")
                x.send_keys(Keys.ENTER)
                y = driver.find_element_by_xpath('//*[@id="r1-0"]/div/h2/a[1]')
                y.click()
                count1 = 0
            except NoSuchElementException:
                print("Element not found")
                count1 = count1 + 1
                Keys.F5
                time.sleep(15)


            except NoSuchWindowException:
                driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
                print("skipped")
                pass
            except WebDriverException:
                driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
                print("skipped")
                pass
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, 500)")
            time.sleep(2)
            driver.execute_script("window.scrollTo(500, 1000)")
            time.sleep(2)
            driver.execute_script("window.scrollTo(1000, 1500)")
            time.sleep(2)
            driver.execute_script("window.scrollTo(2000, 2500)")
            time.sleep(2)
            driver.execute_script("window.scrollTo(2000, 2500)")
            count = count + 1
            print(str(count) + '-second')
            if count1 > 2:
                print("Check internet connection")
                #exit()
            time.sleep(1)

class SSS(Thread):
    def run(self):
        count = 0
        count1=0
        driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
        for i in range(0, 2):

            try:

                driver.get("https://duckduckgo.com/")
                driver.maximize_window()
                x = driver.find_element_by_xpath('//*[@id="search_form_input_homepage"]')
                x.send_keys("What is workflow automation? Can you list some of the tools?")
                x.send_keys(Keys.ENTER)
                y = driver.find_element_by_xpath('//*[@id="r1-0"]/div/h2/a[1]')
                y.click()
                count1=0
            except NoSuchElementException:
                print("Element not found")
                Keys.F5
                count1 = count1 + 1
                time.sleep(15)

            except NoSuchWindowException:
                driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
                print("skipped")
                pass
            except WebDriverException:
                driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
                print("skipped")
                pass
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, 500)")
            time.sleep(2)
            driver.execute_script("window.scrollTo(500, 1000)")
            time.sleep(2)
            driver.execute_script("window.scrollTo(1000, 1500)")
            time.sleep(2)
            driver.execute_script("window.scrollTo(2000, 2500)")
            time.sleep(2)
            driver.execute_script("window.scrollTo(2000, 2500)")
            count = count + 1
            print(str(count) + '-third')
            if count1 > 2:
                print("Check internet connection")
                #exit()
            time.sleep(1)
t1=S()
t2=SS()
t3=SSS()

t1.start()
t2.start()
t3.start()

