from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import variables


class Eokul():
    
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 10)
    
    def login(self):
        self.driver.get(variables.MEBBIS_URL)
        mebbis_username = self.driver.find_element_by_id("txtKullaniciAd").send_keys(variables.USERNAME)
        mebbis_password = self.driver.find_element_by_id("txtSifre").send_keys(variables.PASSWORD)
        self.driver.find_element_by_id("btnGiris").click()

        el = self.wait.until(lambda d: d.find_elements_by_id("ProfileInfoDiv"))
        if el:
            print("Giriş başarılı")
        else:
            print("başarısız")

app = Eokul()
app.login()