from selenium import webdriver
import time
import PageInf
import openpyxl
import unittest
import BasicInf.README
import BasicInf.ReadExecl
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PageInf.Admin_Func import adminfunc
from selenium.webdriver.chrome.service import Service
class AccoutApply(unittest.TestCase):
    # def setUp(self):
    #     s = Service('/usr/local/bin/chromedriver')
    #     self.driver = webdriver.Chrome(service=s)
    #     self.driver.get(BasicInf.README.u())
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(10)
    def accoutApp(self):
        s = Service(BasicInf.README.wd())
        self.driver = webdriver.Chrome(service=s)
        driver = self.driver
        #打开系统
        driver.get(BasicInf.README.u())
        driver.maximize_window()
        driver.implicitly_wait(10)
        #登录
        data = BasicInf.ReadExecl.readExcel()
        time.sleep(2)
        driver.find_element(By.XPATH, BasicInf.README.ac()).send_keys(data[0])
        time.sleep(2)
        driver.find_element(By.XPATH, BasicInf.README.pw()).send_keys(data[1])
        time.sleep(1)
        driver.find_element(By.XPATH, BasicInf.README.sm()).click()
        time.sleep(3)
        #进入账号申请页面
        driver.find_element(By.XPATH,PageInf.Admin_Func.adminfunc().adminFunc()).click()
        driver.find_element(By.XPATH,PageInf.Admin_Func.accout().Accout()).click()
        time.sleep(2)
        driver.find_element(By.XPATH,PageInf.Admin_Func.accout().addButton()).click()
        driver.implicitly_wait(10)
        driver.find_element(By.CSS_SELECTOR,PageInf.Admin_Func.accout().buildButton()).click()
        time.sleep(1)
        driver.find_element(By.XPATH,'//*[@class="vxe-table--main-wrapper"]/div[2]/table/tbody/tr/td[2]/div/div/span').click()
        driver.find_element(By.XPATH,PageInf.Admin_Func.accout().nameInput()).send_keys(data[2])
        time.sleep(2)
        driver.find_element(By.XPATH,'//*[@class="vxe-table--main-wrapper"]/div[2]/table/tbody/tr/td[3]/div/div/span').click()
        driver.find_element(By.XPATH,PageInf.Admin_Func.accout().accoutInput()).send_keys(data[3])
        time.sleep(2)
        driver.find_element(By.XPATH,'//*[@class="vxe-table--main-wrapper"]/div[2]/table/tbody/tr/td[5]/div/div/div/div/div/div/div/div/div/div[2]').click()
        # driver.find_element(By.CSS_SELECTOR,'/html/body/div[8]/div/div[2]/div/div[1]/div/div').click()
        # driver.find_element(By.CSS_SELECTOR,PageInf.Admin_Func.accout().departSelect()).send_keys("江苏海菱机电设备工程有限公司").send_keys(Keys.ENTER)
        # time.sleep(2)
        driver.find_element(By.XPATH,'/html/body/div[8]/div/div[2]/div/div[2]/div/div/div/div[1]/div[1]/div').click()
        driver.find_element(By.XPATH,PageInf.Admin_Func.accout().confirmButton()).click()
        time.sleep(2)
        driver.find_element(By.XPATH,PageInf.Admin_Func.accout().submitButton()).click()
        time.sleep(10)
    def tearDown(self):
        s = Service(BasicInf.README.wd())
        self.driver = webdriver.Chrome(service=s)
        self.driver.quit()
class Check:
    def checkTest(self):
        s = Service(BasicInf.README.wd())
        self.driver = webdriver.Chrome(service=s)
        driver = self.driver
        # 打开系统
        driver.get(BasicInf.README.u())
        driver.maximize_window()
        driver.implicitly_wait(10)
        # 登录
        driver.find_element(By.XPATH, BasicInf.README.ac()).send_keys('17752823456')
        driver.find_element(By.XPATH, BasicInf.README.pw()).send_keys('welcome1')
        time.sleep(1)
        driver.find_element(By.XPATH, BasicInf.README.sm()).click()
        time.sleep(3)
        a = driver.current_url
        if a == BasicInf.README.u():
            print('登录失败')
        else:
            print('登录成功')
if __name__ == "__main__":
    AccoutApply().accoutApp()
    time.sleep(3)
    AccoutApply().tearDown()
    time.sleep(2)
    Check().checkTest()