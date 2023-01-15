import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Browser:
    def __init__(self, url, email, password, users):
        self.url = url
        self.email = email
        self.password = password
        self.browser = None
        self.users = users
        Browser.initialize_chrome(self)

    def initialize_chrome(self):
        try:
            self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        except:
            print("Please install Chrome or ChromeDriver")

    def connect_to_url(self):
        return self.browser.get(self.url)

    def auth(self):
        for data in [(self.email, 'email'), (self.password, 'password')]:
            field = self.browser.find_element(By.XPATH, f"//input[@type='{data[1]}']")
            field.send_keys(data[0])
            field.send_keys(Keys.ENTER)
            time.sleep(4)

    def add_users(self):
        start_loc = '//*[@id="yDmH0d"]/div[5]/div/div[2]/span/c-wiz/div/span/div/c-wiz/div[1]/span/div/'
        addresses = ('div[1]/div[1]/div/div/div/div[1]/div/div[1]/input',
                     'div[1]/div[2]/div/div/div/div[1]/div/div[1]/input',
                     'div[2]/div[1]/div[1]/div/div/div[1]/div/div[1]/input',
                     'div[3]/div[1]/div/div/div[1]/div/div[1]/input',
                     'div[3]/div[2]/div/div/div[1]/div/div[1]/input')
        form_btn = ('//*[@id="yDmH0d"]/div[5]/div/div[2]/span/c-wiz/div/span/div/c-wiz/div[2]/div[2]',
            '//*[@id="yDmH0d"]/div[5]/div/div[2]/span/div/span/div/div[2]/div[1]/div[3]/div/span/span',
            '//*[@id="yDmH0d"]/div[6]/div/div[2]/span/div/div[2]/div[2]/span/span',
            '//*[@id="yDmH0d"]/div[5]/div/div[2]/span/div/span/div/div[4]/div[1]/div/span/span')
        for data in self.users:
            for i in range(0, len(addresses)):
                current_field = self.browser.find_element(By.XPATH, f"{start_loc}{addresses[i]}")
                current_field.send_keys(data[i])

            for i in range(0, len(form_btn)):
                self.browser.find_element(By.XPATH, form_btn[i]).click()
                time.sleep(2)