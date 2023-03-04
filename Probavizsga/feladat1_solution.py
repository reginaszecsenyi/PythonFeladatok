'''
Feladat:
* Helyes kitöltés esete:
    * a: 74
    * b: 32
    * Eredmény: 212

* Nem számokkal történő kitöltés:
    * a: kiskutya
    * b: 32
    * Eredmény: NaN

* Üres kitöltés:
    * a: <üres>
    * b: <üres>
    * Eredmény: NaN
'''
# # importok
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time
# # alap beállítások
# PATH = "S:\oktatási anyagok\chromedriver.exe"
# s = Service(executable_path=PATH)
s = Service(executable_path=ChromeDriverManager().install())
o = Options()
o.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=s, options=o)

URL = 'https://svtesztelovizsga.blob.core.windows.net/$web/proba-vizsga/teglalap_kerulet.html'
browser.get(URL)

# # Beviteli mezők és gomb webelementek változóba mentése
a_side = browser.find_element(By.ID, 'a')
b_side = browser.find_element(By.ID, 'b')
calc_button = browser.find_element(By.ID, 'submit')

# # # Nem DRY változat
# TC1
# a_side.send_keys(74)
# b_side.send_keys(32)
# calc_button.click()
#
# result = browser.find_element(By.ID, 'result').text
# assert result == "212"
# time.sleep(2)
#
# # TC2
# a_side.clear()
# a_side.send_keys('kiskutya')
# b_side.clear()
# b_side.send_keys(32)
# calc_button.click()
#
# result = browser.find_element(By.ID, 'result').text
# assert result == "NaN"
# time.sleep(2)
#
# # TC3
# a_side.clear()
# a_side.send_keys('')
# b_side.clear()
# b_side.send_keys('')
# calc_button.click()
#
# result = browser.find_element(By.ID, 'result').text
# assert result == "NaN"
# time.sleep(2)

# # Beviteli adatok megadása és gomb megnyomása függvény, ellenőrzéssel
def check(a_inp, b_inp, exp_res):
    a_side.clear()
    a_side.send_keys(a_inp)
    b_side.clear()
    b_side.send_keys(b_inp)
    calc_button.click()
    assert exp_res == browser.find_element(By.ID, 'result').text
    time.sleep(2)

# # Tesztesetek lefuttatása a megírt függvénnyel
# TC1
check(74, 32, '212')

# TC2
check('kiskutya', 32, 'NaN')

# TC3
check('', '', 'NaN')

# # Böngésző bezárása
browser.quit()
