import time
import pandas as pd
import openpyxl
from selenium.webdriver.common.by import By


class Users:
    def __init__(self, path_excel):
        self.excel = path_excel

    def read_users(self):
        data = pd.read_excel(self.excel)
        return zip(data['Forename'], data['Surname'], data['Primary email'], data['Secondary email'], data['Phone number'])


