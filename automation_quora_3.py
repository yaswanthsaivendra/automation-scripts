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
        for i in range(0,10):
            try:
                driver.get("https://duckduckgo.com/")
                driver.maximize_window()
                time.sleep(1)
                driver.get("https://www.quora.com/unanswered/What-can-I-know-learn-from-textsheet-com")

            except NoSuchElementException:
                print("Element not found")
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
            # driver.execute_script("window.scrollTo(1000, 1500)")
            # time.sleep(2)
            # driver.execute_script("window.scrollTo(2000, 2500)")
            # time.sleep(2)
            # driver.execute_script("window.scrollTo(2000, 2500)")
            # time.sleep(2)
            # driver.execute_script("window.scrollTo(3000, 3500)")
            # time.sleep(2)
            # driver.execute_script("window.scrollTo(4000, 4500)")
            count = count + 1
            print(str(count) + '-first')
            if count1 > 3:
                print("Check internet connection")
                exit()
            time.sleep(1)
            #driver.close()

class SS(Thread):
    def run(self):
        count = 0
        count1=0
        driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
        for i in range(0, 10):
            try:
                driver.get("https://duckduckgo.com/")
                driver.maximize_window()
                time.sleep(1)
                driver.get("https://www.quora.com/unanswered/What-can-I-know-learn-from-textsheet-com")

            except NoSuchElementException:
                print("Element not found")
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
            # driver.execute_script("window.scrollTo(1000, 1500)")
            # time.sleep(2)
            # driver.execute_script("window.scrollTo(2000, 2500)")
            # time.sleep(2)
            # driver.execute_script("window.scrollTo(2000, 2500)")
            # time.sleep(2)
            # driver.execute_script("window.scrollTo(3000, 3500)")
            # time.sleep(2)
            # driver.execute_script("window.scrollTo(4000, 4500)")
            count = count + 1
            print(str(count) + '-second')
            if count1 > 3:
                print("Check internet connection")
                exit()
            time.sleep(1)

class SSS(Thread):
    def run(self):
        count = 0
        count1=0
        driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
        for i in range(0, 10):

            try:
                driver.get("https://duckduckgo.com/")
                driver.maximize_window()
                time.sleep(1)
                driver.get("https://www.quora.com/unanswered/What-can-I-know-learn-from-textsheet-com")

            except NoSuchElementException:
                print("Element not found")
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
            # driver.execute_script("window.scrollTo(1000, 1500)")
            # time.sleep(2)
            # driver.execute_script("window.scrollTo(2000, 2500)")
            # time.sleep(2)
            # driver.execute_script("window.scrollTo(2000, 2500)")
            # time.sleep(2)
            # driver.execute_script("window.scrollTo(3000, 3500)")
            # time.sleep(2)
            # driver.execute_script("window.scrollTo(4000, 4500)")
            count = count + 1
            print(str(count) + '-third')
            if count1 > 3:
                print("Check internet connection")
                exit()
            time.sleep(1)
t1=S()
t2=SS()
t3=SSS()

t1.start()
t2.start()
t3.start()

