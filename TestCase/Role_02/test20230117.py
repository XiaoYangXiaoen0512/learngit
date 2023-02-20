from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common import NoSuchElementException


# driver = self.driver
s = Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=s)
# 打开系统
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
                   Object.defineProperty(navigator, 'webdriver', {
                     get: () => undefined
                   })
                 """
})
driver.implicitly_wait(20)
driver.get('https://supp.smec-cn.com/supp-mnt/app/')
driver.maximize_window()
driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/form/div[1]/div/div/input').send_keys('15690866454')
driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/form/div[2]/div/div/button').click()
time.sleep(15)
driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/form/div[3]/div/button').click()
driver.find_element(By.XPATH, '//ul/div/label[8]/li/div/div').click()
driver.find_element(By.XPATH, '//div/div[2]/div/div[2]/div/div[3]/div[2]/div/div').click()
time.sleep(8)
i = 1
y = 0
while i < 11:
    try:
        if i == 4:
            i = i + 1
        time.sleep(6)
        print(i)
        code = '//table/tbody/tr[{}]/td/div/div/span'.format(i)
        print(code)
        # driver.find_element(By.XPATH, code).click()
        element = driver.find_element(By.XPATH, code)
        driver.execute_script("arguments[0].click();", element)
        time.sleep(6)
        driver.find_element(By.XPATH, '//div/div[3]/div/button[2]').click()
        i = i + 1
        time.sleep(10)
        if i == 10:
            driver.find_element(By.XPATH, '//div/div[3]/div/div/div[2]/div/div[2]/div[2]/button[2]').click()
            i = 1
            y = y + 1
        if y == 32:
            break
    except NoSuchElementException:
        break

