from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from excel_data import get_student_number, get_new_student_number
import time


student_number = get_student_number(1000)
new_number = get_new_student_number()
dict_number = dict(zip(student_number, new_number))

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)
driver.get("https://mebbis.meb.gov.tr")


username = driver.find_element_by_id("txtKullaniciAd")
password = driver.find_element_by_id("txtSifre")

username.send_keys("")
password.send_keys("")

driver.find_element_by_id("btnGiris").click()
element = driver.find_element_by_id("rptProjeler_ctl01_rptKullanicilar_ctl00_LinkButton1")
driver.execute_script("arguments[0].click();", element)

time.sleep(3)
driver.window_handles
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[-1])

el = wait.until(lambda d: d.find_element_by_id("mdlOOO"))
driver.execute_script("arguments[0].click();", el)

newstudent_number = wait.until(lambda d: d.find_element_by_id("OGRMenu1_txtTCYeni"))
newstudent_number.send_keys(1)
driver.find_element_by_id("OGRMenu1_btnOgrenciAra").click()

for old_number, new_number in dict_number.items():
    print(old_number)
    print(new_number)
    old_student_number = wait.until(lambda d: d.find_element_by_id("OGRMenu1_txtTC"))
    old_student_number.send_keys(old_number)
    driver.find_element_by_id("OGRMenu1_btnAra").click()
    new_student_number = wait.until(lambda d: d.find_element_by_id("txtOkulNo"))
    new_student_number.clear()
    new_student_number.send_keys(new_number)
    driver.find_element_by_id("OOMToolbarActive1_kaydet_b").click()

    time.sleep(3)

