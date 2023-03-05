'''
Feladat:
Az alkalmazás akkor működik helyesen ha 100 gombnyomásból legalább 30 fej. Ezt kell ellenőrizned.
'''
# # importok
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time

# PATH = "S:\oktatási anyagok\chromedriver.exe"
# s = Service(executable_path=PATH)
# # alap beállítások
s = Service(executable_path=ChromeDriverManager().install())
o = Options()
o.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=s, options=o)

URL = 'https://svtesztelovizsga.blob.core.windows.net/$web/proba-vizsga/penzfeldobas.html'
browser.get(URL)

# 1. verzió
pf_gomb = browser.find_element(By.ID, 'submit')
fej_szamlalo = 0

for i in range(100):
    pf_gomb.click()
    if browser.find_element(By.ID, 'lastResult').text == 'fej':
        fej_szamlalo += 1

assert fej_szamlalo >= 30
print(fej_szamlalo)

# # 2. verzió-------------------------------------------------------------
pf_gomb = browser.find_element(By.ID, 'submit')
fej_szamlalo = 0

tesztelendo_dobas_szam = 100
for i in range(tesztelendo_dobas_szam):
    pf_gomb.click()

dobasok = browser.find_elements(By.TAG_NAME, 'li')

for dobas in dobasok:
    if dobas.text == 'fej':
        fej_szamlalo += 1

assert fej_szamlalo >= 30
print(fej_szamlalo)

# # 3. verzió--------------------------------------------------------------------------
# try:
#     minimum = 30
#     pf_gomb = browser.find_element(By.ID, 'submit')
#     fej_lista = []
#
#     for i in range(100):
#         pf_gomb.click()
#         if browser.find_element(By.ID, 'lastResult').text == 'fej':
#             fej_lista.append('fej')
#
#     assert len(fej_lista) >= minimum
#     print(len(fej_lista))
#
# except AssertionError:
#     print(f'A fejek száma csak: {len(fej_lista)}, ez nem éri el a {minimum} minimum értéket.')

# # Böngésző bezárása
browser.quit()