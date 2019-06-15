from selenium import webdriver
import time
import pyperclip


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
class PhotoApi:
    CHROME_DRIVER = 'C:\chromedriver.exe'
    REFRESH_QUOTA = 1100

    def __init__(self):
        self.driver = self.initialize_driver()
        self.quota = 0

    def initialize_driver(self):
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(self.CHROME_DRIVER, options=options)
        driver.get("https://labs.everypixel.com/api/demo")
        return driver

    def get_response(self, photo_url):
        if self.quota == self.REFRESH_QUOTA:
            self.driver.refresh()
            time.sleep(5)
            self.quota = 0
        self.quota = self.quota + 1
        pyperclip.copy(photo_url)
        self.driver.find_element_by_class_name("estest_upload__input").send_keys('\ue009', 'v')
        time.sleep(3)
        try:
            response = self.driver.find_element_by_xpath('//*[@id="demo-container"]/div/div[2]/div[3]/div/ul').text
        except:
            return []
        return response.splitlines()

    def get_parsed_response(self, photo_url):
        response = self.get_response(photo_url)
        quantifier = response.__len__() / 2
        parsed_response = []
        for counter in range(0, response.__len__() - 1, 2):
            n_times = int(int(response[counter + 1][:-1]) / quantifier)
            parsed_response = parsed_response + [response[counter] for __ in range(n_times)]
        return parsed_response
