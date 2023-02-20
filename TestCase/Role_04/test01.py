import self as self
from selenium import webdriver
import time
import BasicInf.ReadExecl
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common import NoSuchElementException


class getInformation():
    def __init__(self):
        s = Service('/usr/local/bin/chromedriver')
        self.driver = webdriver.Chrome(service=s)

    def accout(self):
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
        driver.implicitly_wait(10)
        driver.get('http://www.chinabidding.cc')
        driver.maximize_window()
        time.sleep(5)
        # 关闭弹窗
        # driver.switch_to.frame('layui-layer-iframe1')
        driver.find_element(By.XPATH, '//*[@id="layui-layer1"]/span[1]/a').click()
        # driver.switch_to.default_content()
        # 登录
        driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('u2974')
        driver.find_element(By.ID, 'userpwd').send_keys('smec3030')
        driver.find_element(By.XPATH, '//*[@id="login_frm1"]/span[3]/input').click()
        time.sleep(5)
        # 搜索
        driver.find_element(By.ID, 'keyword').send_keys('电梯')
        driver.find_element(By.ID, 'submit').click()
        i = 1
        while i:
            try:
                code = '//*[@id="center_box"]/div[2]/div[1]/div[2]/ul/li[{}]/span[1]'.format(i)
                tendertype = driver.find_element(By.XPATH, code).text
                print(tendertype)
                if tendertype == '[招标公告]':
                    alink = '//*[@id="center_box"]/div[2]/div[1]/div[2]/ul/li[{}]/a'.format(i)
                    tender = driver.find_element(By.XPATH, alink)
                    tenderlink = tender.get_attribute('href')
                    tendertext = tender.text
                    tender.click()
                    time.sleep(2)
                    for handle in driver.window_handles:
                        driver.switch_to.window(handle)
                        # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
                        if tendertext in driver.title:
                            # 如果是，那么这时候WebDriver对象就是对应的该窗口，正好，跳出循环，
                            break
                    contact = []
                    telephone = []
                    tenderarea = driver.find_element(By.XPATH, '//*[@id="center_box"]/div[2]/div[1]/span/a[1]').text
                    tenderarea = tenderarea[5:]
                    releasetime = driver.find_element(By.XPATH, '//*[@id="center_box"]/div[2]/div[1]/span/a[2]').text
                    releasetime = releasetime[5:]
                    try:
                        driver.find_elements(By.XPATH, '//*[@id="center_box"]/div[2]/div[1]/div[3]/div[1]/div/*')
                    except NoSuchElementException:
                        contact = ''
                        telephone = ''
                    else:
                        a = driver.find_elements(By.TAG_NAME, 'p')
                        for y in a:
                            text = y.text
                            if ("联系电话" in text) or ("联系方式" in text) or ("手机号码" in text):
                                telephone.append(text)
                            elif ("联系人" in text) or ("联系单位" in text):
                                contact.append(text)
                    contact = str(contact)
                    telephone = str(telephone)
                    driver.close()
                    print(tendertext, tenderarea, releasetime, tenderlink)
                    BasicInf.ReadExecl.writeExcel(tendertext, tenderarea, releasetime, tenderlink, contact, telephone)
                    i += 1
                    print(i)
                    for handle in driver.window_handles:
                        driver.switch_to.window(handle)
                        if '电梯招标信息，电梯采购信息_电梯项目信息' in driver.title:
                            break
                    time.sleep(2)
                else:
                    i += 1
                    print(i)
                    continue
            except NoSuchElementException:
                driver.find_element(By.XPATH, '//*[@id="center_box"]/div[2]/div[1]/div[2]/div/a[10]').click()
                i = 1
                print(i)

    def getinfor(self, a):
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
        driver.implicitly_wait(10)
        driver.get(a)
        driver.maximize_window()
        driver.find_element(By.XPATH, '//*[@id="layui-layer1"]/span[1]/a').click()
        # 登录
        driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('u2974')
        driver.find_element(By.ID, 'userpwd').send_keys('smec3030')
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="login_frm1"]/span[3]').click()
        time.sleep(1)
        driver.refresh()
        time.sleep(3)
        contact = []
        telephone = []
        tenderarea = driver.find_element(By.XPATH, '//*[@id="center_box"]/div[2]/div[1]/span/a[1]').text
        tenderarea = tenderarea[5:]
        releasetime = driver.find_element(By.XPATH, '//*[@id="center_box"]/div[2]/div[1]/span/a[2]').text
        releasetime = releasetime[5:]
        try:
            driver.find_elements(By.XPATH, '//*[@id="center_box"]/div[2]/div[1]/div[3]/div[1]/div/*')
        except NoSuchElementException:
            contact = ''
            telephone = ''
        else:
            a = driver.find_elements(By.TAG_NAME, 'p')
            for i in a:
                text = i.text
                if (("联系电话" in text) or ("联系方式" in text) or ("手机号码" in text)) and (len(text) < 30):
                    telephone.append(text)
                elif (("联系人" in text) or ("联系单位" in text)) and (len(text) < 30):
                    contact.append(text)
        # print(tenderarea, releasetime, contact, telephone)
        # BasicInf.ReadExecl.writeExcel(1, tenderarea, releasetime, 1, str(contact), str(telephone))
        driver.quit()
        return [tenderarea, releasetime, str(contact), str(telephone)]

if __name__ == "__main__":
    getInformation.accout(self)
