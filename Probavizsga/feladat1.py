# 1. Feladat: Keressük a téglalap kerületét
# Készíts egy python applikációt (egy darab python file) ami selenium-ot használ.
# A program töltse be a téglalap kerülete app-ot az https://svtesztelovizsga.blob.core.windows.net/$web/proba-vizsga/teglalap_kerulet.html oldalról.
# Feladatod, hogy automatizáld selenium webdriverrel az alábbi funkcionalitásokat a téglalap kerülete appban:
# Az ellenőrzésekhez NEM kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos, hogy assert összehasonlításokat használj!

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

service = Service(executable_path=r'C:\Users\Szabi\Desktop\Újratervezés program\Automata szoftvertesztelő\selenium\chromedriver.exe')
options = Options()
options.add_experimental_option('detach', True)
browser = webdriver.Chrome(service=service, options=options)

URL = 'https://svtesztelovizsga.blob.core.windows.net/$web/proba-vizsga/teglalap_kerulet.html'
browser.get(URL)

browser.maximize_window()

#-----------------------------------------------------------------------------

'''Minden részfeladatban először kikeresem a szükséges mezők elérését, 
aztán elküldöm a beírandó értékeket, rákattintok a kalkuláció gombra,
majd pedig assertel megbizonyosodom róla, hogy tényleg a várt éréket kaptuk.'''

#-----------------------------------------------------------------------------

#1.részfeladat:
# Helyes kitöltés esete:
# a: 74
# b: 32
# Eredmény: 212

time.sleep(1)
a = browser.find_element(By. ID, 'a')
b = browser.find_element(By. ID, 'b')
submit_btn = browser.find_element(By. ID, 'submit')
result = browser.find_element(By.ID, 'result' )
time.sleep(1)

a.send_keys(74)
b.send_keys(32)

time.sleep(1)

submit_btn.click()

time.sleep(1)

print(result.text)
assert result.text == '212'

#------------------------------------------------------------------------------

#2. részfeladat:
# Nem számokkal történő kitöltés:
# a: kiskutya
# b: 32
# Eredmény: NaN

browser.refresh()
time.sleep(2)

time.sleep(1)
a = browser.find_element(By. ID, 'a')
b = browser.find_element(By. ID, 'b')
submit_btn = browser.find_element(By. ID, 'submit')
result = browser.find_element(By.ID, 'result' )
time.sleep(1)

a.send_keys('kiskutya')
b.send_keys(32)

time.sleep(1)

submit_btn.click()

time.sleep(1)

print(result.text)
assert result.text == 'NaN'

#------------------------------------------------------------------------------

#3. részfeladat:
# Üres kitöltés:
# a: <üres>
# b: <üres>
# Eredmény: NaN

browser.refresh()
time.sleep(2)

time.sleep(1)
a = browser.find_element(By. ID, 'a')
b = browser.find_element(By. ID, 'b')
submit_btn = browser.find_element(By. ID, 'submit')
result = browser.find_element(By.ID, 'result' )
time.sleep(1)

a.send_keys()
b.send_keys()

time.sleep(1)

submit_btn.click()

time.sleep(1)

print(result.text)
assert result.text == 'NaN'

browser.quit()