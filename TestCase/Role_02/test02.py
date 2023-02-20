from selenium import webdriver
import time
import BasicInf.README
import BasicInf.ReadExecl
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


def accoutApp():
    s = Service('/usr/local/bin/chromedriver')
    driver = webdriver.Chrome(service=s)
    # 打开系统
    driver.implicitly_wait(10)
    driver.get('https://supp-mnt.smec-cn.com/app/298029362131763201/app/custom-page/apaas-custom-index?appId=300011223712268288&title=%E9%A6%96%E9%A1%B5&currentMenu=307921751541547008&url=apaas-custom-index&t=1660293345017')
    driver.maximize_window()
    driver.implicitly_wait(10)
    # 登录
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/form/div[1]/div/div[1]/input').send_keys('15690866454')
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div/div[2]/form/div[2]/div/div/button').click()
    time.sleep(30)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div/div/div/div[1]/div[2]/div[1]/div[2]/ul/div/label[9]/li/div/div/div').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div/div/div/div[1]/div[2]/div[1]/div[2]/ul/div/label[9]/li/ul/label/div/label[2]/li/div/div').click()
    # 获取数据
    accoutapplydata = BasicInf.ReadExecl.readExcel()
    for i in accoutapplydata:
        driver.find_element(By.XPATH,
                            '//*[@id="app"]/div[1]/div/div/div/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/div/div[2]/div/div[1]/form/div/div[7]/div/div/div/div/div/input').send_keys(i)
        driver.find_element(By.XPATH,
                            '//*[@id="app"]/div[1]/div/div/div/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/div/div[2]/div/div[1]/form/div/div[8]/div/div/div/div/div/input').send_keys('三方保养合同')
        driver.find_element(By.XPATH,
                            '//*[@id="app"]/div[1]/div/div/div/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/div/div[2]/div/div[4]/button[2]').click()
        time.sleep(5)
        number = driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div[1]/div/div/div/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/div/div[3]/div/div/div[2]/div/div[1]/div[2]/div[3]/table/tfoot/tr/td[2]/div/span/div/div[2]/div').text
        print(number)
        BasicInf.ReadExecl.writeExcel(i, number)
        driver.find_element(By.XPATH,
                            '//*[@id="app"]/div[1]/div/div/div/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/div/div[2]/div/div[1]/form/div/div[7]/div/div/div/div/div/input').clear()
        driver.find_element(By.XPATH,
                            '//*[@id="app"]/div[1]/div/div/div/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/div/div[2]/div/div[1]/form/div/div[8]/div/div/div/div/div/input').clear()
    driver.quit()
if __name__ == "__main__":
    accoutApp()

