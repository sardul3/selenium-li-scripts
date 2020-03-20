from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import keys

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
print("You are in: ", driver.title);

likes = 0
y = 1000
for timer in range(0,50):
     driver.execute_script("window.scrollTo(0, "+str(y)+")")
     y += 1000
     time.sleep(1)
like_btn = driver.find_elements_by_css_selector("button.react-button__trigger");
print("Number of posts available: ", len(like_btn))
for btn in like_btn:
    try:
        res = btn.click()
        print("Like sent count: ", likes)
        likes = likes + 1
    except:
        print("Exception occured")

#flag = True
#likes = 0
#while flag:
#    driver.execute_script("window.scrollTo(0, 2000)")
#
#    like_btn = driver.find_elements_by_css_selector("button.react-button__trigger");
#    print("Number of posts available: ", len(like_btn))
#    for btn in like_btn:
#        try:
#            res = btn.click()
#            print("Like sent count: ", likes)
#            likes = likes + 1
#        except:
#            print("Exception occured")
#        finally:
#            if(likes>=1000):
#                flag = False
#
    


