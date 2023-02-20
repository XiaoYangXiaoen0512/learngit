from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
import time
import random
def apply():
    desired_caps = {
        'platformName': 'iOS',
        'platformVersion': '15.5',
        'deviceName': 'iPhone X',
        'appPackage': 'com.example.smeceleapp',
        'appActivity': '.LoginActivity',
        'udid': ''
    }

    # 连接Appium Server，初始化自动化环境
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    # 设置缺省等待时间
    driver.implicitly_wait(10)
    # 登录
    driver.find_element(AppiumBy.ID, 'edUser').send_keys('17752821932')
    driver.find_element(AppiumBy.ID, 'edPassword').send_keys('111')
    time.sleep(2)
    code = 'new UiSelector().text("登录").className("android.widget.TextView")'
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
    # 进入云服务页面页面
    driver.find_element(By.ID, 'navigation_service').click()
    time.sleep(2)
    # 进入保养工单页面
    code = 'new UiSelector().text("保养工单").className("android.widget.TextView")'
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
    time.sleep(2)
    # 点击日历组件左右滑动
    alsetText1 = driver.find_element(AppiumBy.ID, 'calendar_title').text
    a = random.randint(12, 24)
    print(a)
    i = 0
    while i < a:
        driver.find_element(AppiumBy.ID, 'btn_down').click()
        time.sleep(1)
        i = i + 1
    alsetText2 = driver.find_element(AppiumBy.ID, 'calendar_title').text
    # driver.find_element(AppiumBy.ID, 'btn_up').click()
    y = int(a / 12)
    m = a % 12
    b = int(alsetText1[3]) + y
    c = int(alsetText1[5]) + m
    if c > 12:
        jia = int(c / 12)
        c = c % 12
        b = b + jia
    print(y, m, b, c)
    alsetText1 = alsetText1[0:3] + str(b) + alsetText1[4] + str(c) + alsetText1[6:]
    time.sleep(1)
    if alsetText2 == alsetText1:
        alsetText = '测试通过'
    else:
        alsetText = '测试失败'
    driver.quit()
    return alsetText
if __name__ == '__main__':
    a = apply()
    print(a)

