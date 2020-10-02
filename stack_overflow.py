def myfunc():
    from selenium import webdriver
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.common.by import By
    import time
    import os
    import twitter

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

    #driver = webdriver.Chrome(executable_path='F:\chromedriver_win32\chromedriver.exe')

    #Stackoverflow

    driver.get('https://stackoverflow.com/')

    driver.maximize_window()

    driver.find_element_by_xpath('/html/body/header/div/ol[2]/li[2]/a[1]').click()

    driver.find_element_by_xpath('//*[@id="email"]').click()
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(os.environ.get('USERNAME'))
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="password"]').click()
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(os.environ.get('PASSWORD'))
    time.sleep(2)

    driver.find_element_by_xpath('//*[@id="submit-button"]').click()
    time.sleep(2)

    driver.get('https://stackoverflow.com/users/11321166/gokul-nath')

    result = driver.find_element_by_xpath('//*[@id="top-cards"]/aside[2]/div/div/div[2]/div[2]/div/div[1]/span').text
    print(result)
    time.sleep(5)

    driver.close()

    # Twitter  API
    
    api = twitter.Api(consumer_key=os.environ.get('CONSUMER_KEY'),
                      consumer_secret=os.environ.get('CONSUMER_SECRET'),
                      access_token_key=os.environ.get('ACCESS_TOKEN_KEY'),
                      access_token_secret=os.environ.get('ACCESS_TOKEN_SECRET'))

    msg_detail = api.PostDirectMessage(screen_name=os.environ.get('SCREEN_NAME'), text="Today: "+str(result), return_json=True)

    print(msg_detail)

from time import gmtime, strftime

if strftime("%H:%M", gmtime()) == '02:30':
    myfunc()
elif strftime("%H:%M", gmtime()) == '02:31':
    myfunc()
elif strftime("%H:%M", gmtime()) == '02:32':
    myfunc()
else:
    print("Not an scheduled run")


