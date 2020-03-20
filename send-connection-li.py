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
print("You are in: ", driver.title)

connections_nav = driver.find_element_by_id("mynetwork-nav-item")
connections_nav.click()
print("You are in: ", driver.title)

y = 1000
for timer in range(0,50):
     driver.execute_script("window.scrollTo(0, "+str(y)+")")
     y += 1000
     time.sleep(1)
     if y>10000:
        connect_btn = driver.find_elements_by_css_selector("footer.mt2");
        print("Number of connections available: ", len(connect_btn))
        for btn in connect_btn:
            try:
                btn.click()
                print(btn.get_attribute('innerHTML'))
                print("Connection request sent")
            except:
                print("Exception occured")


        

#more_connections_btn = driver.find_element_by_xpath("/html/body/div[5]/div[3]/div/div/div/div/div/div/div/ul/li[4]/div/button/span")
#print(more_connections_btn)
#
#driver.execute_script("arguments[0].click();", more_connections_btn)
#
#connect_btn = driver.find_elements_by_xpath('//*[@id="ember*"]')
#print(connect_btn)

#connect_btn = driver.find_elements_by_css_selector("footer.mt2");
#print("Number of connections available: ", len(connect_btn))
#for btn in connect_btn:
#    try:
#        btn.click()
#        print(btn.get_attribute('innerHTML'))
#        print("Connection request sent")
#    except:
#        print("Exception occured")

    

