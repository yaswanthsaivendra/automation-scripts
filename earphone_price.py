import twitter
from selenium import webdriver
import time
import requests
import config as conf
import os

body = ''


class Price_List:
    def get_flipkart_price(self):
        """
        This function takes the Flipkart url from config and get's the price of each product
        :return: None
        """
        global body
        try:
            for item in conf.flipkart_product_map.keys():
                req_body = requests.get(conf.flipkart_product_map[item]).text
                start = req_body.index('_16Jk6d')
                try:
                    rate = int(str(req_body[start + 10]) + str(req_body[start + 12:start + 15]))
                    print(item, rate)
                    if rate <= 1110:
                        body += '{} : {}\n{}\n'.format(item, str(rate), conf.flipkart_product_map[item])
                except:
                    pass
        except Exception as e:
            print(str(e))

    def get_amazon_price(self):
        """
        This function takes the Amazon url from config and get's the price of each product
        :return: None
        """
        global body
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)

        # driver = webdriver.Chrome(executable_path='E:\chromedriver_win32\chromedriver.exe')
        for item in conf.Amazon_product_map.keys():
            driver.get(conf.Amazon_product_map[item])
            driver.maximize_window()
            time.sleep(5)
            print(item)
            try:
                try:
                    amount = driver.find_element_by_xpath('//*[@id="priceblock_ourprice"]').text
                except:
                    amount = driver.find_element_by_xpath('// *[ @ id = "priceblock_dealprice"]').text
                try:
                    rate = int(str(amount[2]) + str(amount[4:7]))
                    print(item, rate)
                    if rate <= 1110:
                        body += '{} : {}\n{}\n'.format(item, str(rate), conf.Amazon_product_map[item])
                except:
                    pass

            except Exception as e:
                print(str(e))
        driver.close()

    def send_twitter_message(self):
        """
        THis function send the prices as the message to other twitter accounts
        :return: None
        """
        try:
            api = twitter.Api(consumer_key=os.environ.get('CONSUMER_KEY'),
                              consumer_secret=os.environ.get('CONSUMER_SECRET'),
                              access_token_key=os.environ.get('ACCESS_TOKEN_KEY'),
                              access_token_secret=os.environ.get('ACCESS_TOKEN_SECRET'))

            global body
            msg_detail = api.PostDirectMessage(screen_name='BharathanJarvis', text=body, return_json=True)
            # msg_detail = api.PostDirectMessage(screen_name='Gokulmechengg', text=body, return_json=True)
            print("Message sent!")
        except Exception as e:
            print(str(e))


price_obj = Price_List()
price_obj.get_flipkart_price()
price_obj.get_amazon_price()
if body != '':
    price_obj.send_twitter_message()
else:
    print("No data to send message")
