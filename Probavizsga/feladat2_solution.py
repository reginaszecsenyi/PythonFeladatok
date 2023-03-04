'''
Feladat:
* Helytelen kitöltés esete:
    * email: teszt@
    * Az alábbi hibaüzenet jelenik meg: Kérjük, adja meg a „@” utáni részt is. A(z) „teszt@” cím nem teljes.

* Üres:
    * email: <üres>
    * Az alábbi hibaüzenet jelenik meg: Kérjük, töltse ki ezt a mezőt.

* Helyes kitöltés:
    * email: teszt@elek.hu
    * Nincs validációs hibazüzenet
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

browser.get('https://svtesztelovizsga.blob.core.windows.net/$web/proba-vizsga/email_validation.html')

# # Beviteli mező és gomb webelementek változóba mentése
email_field = browser.find_element(By.ID, 'email')
submit_button = browser.find_element(By.ID, 'submit')

# # # Nem Dry változat
# # TC1
# email_field.clear()
# email_field.send_keys('teszt@')
# submit_button.click()
# error_message = browser.find_element(By.CLASS_NAME, "validation-error").text
# print(error_message)
# assert error_message == 'Kérjük, adja meg a „@” utáni részt is. A(z) „teszt@” cím nem teljes.'
# time.sleep(2)

# # Beviteli adat megadása és gomb megnyomása függvény
def validation(email_inp):
    email_field.clear()
    email_field.send_keys(email_inp)
    submit_button.click()

# # Tesztadatok
test_data_emails = ['teszt@', '', 'teszt@elek.hu']
exp_err_messages = ['Kérjük, adja meg a „@” utáni részt is. A(z) „teszt@” cím nem teljes.',
                    'Kérjük, töltse ki ezt a mezőt.', '']


# # Tesztesetek lefuttatása a megírt függvénnyel, majd külön ellenőrzés
# TC1
validation(test_data_emails[0])
assert browser.find_element(By.CLASS_NAME, "validation-error").text == exp_err_messages[0]
time.sleep(1)

# TC2
validation(test_data_emails[1])
assert browser.find_element(By.CLASS_NAME, "validation-error").text == exp_err_messages[1]
time.sleep(1)

# TC3
validation(test_data_emails[2])
assert len(browser.find_elements(By.CLASS_NAME, "validation-error")) == 0
assert browser.find_element(By.TAG_NAME, 'form').get_attribute('class') == exp_err_messages[2]

# # Böngésző bezárása
browser.quit()