# 3. Feladat: Pénzfeldobás
# Készíts egy python applikációt (egy darab python file) ami selenium-ot használ.
#
# A program töltse be a pénzfeldobás app-ot az https://svtesztelovizsga.blob.core.windows.net/$web/proba-vizsga/penzfeldobas.html oldalról.
#
# Feladatod, hogy automatizáld selenium webdriverrel a pénzfeldobás app tesztelését.
#
# Az alkalmazás akkor működik helyesen ha 100 gombnyomásból legalább 30 fej. Ezt kell ellenőrizned.
#
# Az ellenőrzésekhez NEM kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos, hogy assert összehasonlításokat használj!


import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

service = Service(executable_path=r'C:\Users\Szabi\Desktop\Újratervezés program\Automata szoftvertesztelő\selenium\chromedriver.exe')
options = Options()
options.add_experimental_option('detach', True)
browser = webdriver.Chrome(service=service, options=options)

URL = 'https://svtesztelovizsga.blob.core.windows.net/$web/proba-vizsga/penzfeldobas.html'
browser.get(URL)

browser.maximize_window()

#Feladatod, hogy automatizáld selenium webdriverrel a pénzfeldobás app tesztelését.
#Az alkalmazás akkor működik helyesen ha 100 gombnyomásból legalább 30 fej. Ezt kell ellenőrizned.

throw_btn = browser.find_element(By.ID, 'submit')

for x in range(100):
    throw_btn.click()

results = browser.find_element(By.ID, "results")
print(results.text)

print(results.text.count('fej'))
# if results.text.count('fej') >= 30:
#     print('Az alkalmazás helyesen működik')
# else:
#     print('Az alkalmazás nem működik helyesen')

assert results.text.count('fej') >= 30

browser.quit()