# 2. Feladat: Email mező
# Készíts egy python applikációt (egy darab python file) ami selenium-ot használ.
# A program töltse be a email mező app-ot az https://svtesztelovizsga.blob.core.windows.net/$web/proba-vizsga/email_validation.html oldalról.
# Feladatod, hogy automatizáld selenium webdriverrel az email mező app tesztelését.
# A cél az email validáció tesztelése:

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

URL = 'https://svtesztelovizsga.blob.core.windows.net/$web/proba-vizsga/email_validation.html'
browser.get(URL)

browser.maximize_window()

#--------------------------------------------------------------------------------------------------
# 1. részfeladat

# Helytelen kitöltés esete:
# email: teszt@
# Az alábbi hibaüzenet jelenik meg:
# magyar: Kérjük, adja meg a „@” utáni részt is. A(z) „teszt@” cím nem teljes.
# angol: Please enter a part following '@'. 'teszt@' is incomplete.

email = browser.find_element(By.ID, 'email')
email.send_keys('teszt@')

time.sleep(1)

submit_btn = browser.find_element(By.ID, 'submit')
submit_btn.click()

time.sleep(1)

error_msg = browser.find_element(By.XPATH, '//div[@class="validation-error"]')
assert error_msg.text == 'Kérjük, adja meg a „@” utáni részt is. A(z) „teszt@” cím nem teljes.' or error_msg.text == "Please enter a part following '@'. 'teszt@' is incomplete."

#--------------------------------------------------------------------------------------------------
# 2. részfeladat

# Üres:
# email: <üres>
# Az alábbi hibaüzenet jelenik meg:
# magyar: Kérjük, töltse ki ezt a mezőt.
# angol: Please fill out this field. (angol beállítások esetén)

browser.refresh()
time.sleep(1)

email = browser.find_element(By.ID, 'email')
email.send_keys()

time.sleep(1)

submit_btn = browser.find_element(By.ID, 'submit')
submit_btn.click()

time.sleep(1)

error_msg = browser.find_element(By.XPATH, '//div[@class="validation-error"]')
assert error_msg.text == 'Kérjük, töltse ki ezt a mezőt.' or error_msg.text == 'Please fill out this field.'


#--------------------------------------------------------------------------------------------------
# 3. részfeladat

# Helyes kitöltés:
# email: teszt@elek.hu
# Nincs validációs hibazüzenet

browser.refresh()
time.sleep(1)

email = browser.find_element(By.ID, 'email')
email.send_keys('teszt@elek.hu')

time.sleep(1)

submit_btn = browser.find_element(By.ID, 'submit')
submit_btn.click()

time.sleep(1)

assert len(browser.find_elements(By.XPATH, '//div[@class="validation-error"]')) == 0

# try:
#     error_msg = browser.find_element(By.XPATH, '//div[@class="validation-error"]')
# except NoSuchElementException:
#     print("Element does not exist")


#----------------------------------------------------------------------------------------------------

browser.quit()