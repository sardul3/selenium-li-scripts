from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import keys
import time

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.implicitly_wait(10)

driver.get("https://www.linkedin.com/login")
print("You are in: ",driver.title)

login_user = driver.find_element_by_name("session_key")
login_user.clear()
login_user.send_keys(keys.li_email)

login_pw = driver.find_element_by_name("session_password")
login_pw.clear()
login_pw.send_keys(keys.li_pw)

login_pw.send_keys(Keys.RETURN)
print("You are in: ", driver.title)

driver.get("https://www.linkedin.com/mynetwork/invitation-manager/sent/");
print("You are in: ", driver.title)

numbers = driver.find_elements_by_class_name("artdeco-pagination__indicator");
print(len(numbers))
start = len(numbers)
i = 0
for number in numbers:
    i = i + 1
    if i == start:
        number.click()
        withdraws = driver.find_elements_by_class_name("invitation-card__action-btn")
        print(len(withdraws))

        for withdraw in withdraws:
            time.sleep(3)
            btn = driver.find_element_by_class_name("invitation-card__action-btn")
            btn.click()
            
            confirm = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")))

            print("Removed one stale connection request")
            N = 3
            actions = ActionChains(driver)
            for _ in range(N):
                actions = actions.send_keys(Keys.TAB)
            actions.send_keys(Keys.ENTER)
            actions.perform()
            time.sleep(2)
   
 
