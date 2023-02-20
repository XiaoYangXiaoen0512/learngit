from appium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from appium.webdriver.common.appiumby import AppiumBy


def submittest(a, accout, b):
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '12',
        'deviceName': 'Miowii',
        'appPackage': 'com.example.smeceleapp',
        'appActivity': '.LoginActivity',
        'unicodeKeyboard': True,
        'resetKeyboard': True,
        'noReset': True,
        'newCommandTimeout': 6000,
        'automationName': 'UiAutomator2'
    }

    # 连接Appium Server，初始化自动化环境
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    # 设置缺省等待时间
    driver.implicitly_wait(10)
    # 勾选协议
    alsettext = []
    if a == '是':
        driver.find_element(By.ID, 'policy_checkbox').click()
    time.sleep(2)
    # 输入账号
    driver.find_element(By.ID, 'edUser').send_keys(accout)
    time.sleep(1)
    if b == '1' or b == '2':
        driver.open_notifications()
        time.sleep(1)
        try:
            driver.find_element(AppiumBy.ID, 'dismiss_view')
        except NoSuchElementException:
            driver.back()
        else:
            driver.find_element(AppiumBy.ID, 'dismiss_view').click()
    driver.find_element(AppiumBy.ID, 'll_pwd_btn').click()
    time.sleep(1)
    # 获取文本内容
    # xpath = "//*[contains(@text,'{}')]".format(expectedalert1)
    # print(xpath)
    alsettext.append(driver.find_element(By.XPATH, "//*[@class='android.widget.Toast']").text)
    print(alsettext)
    time.sleep(5)
    if b == '1':
        password = '1'
        driver.find_element(By.ID, 'edPassword').send_keys(password)
    elif b == '2':
        driver.open_notifications()
        time.sleep(1)
        a = "//*[contains(@text,'验证码')]"
        password = driver.find_element(AppiumBy.XPATH, a).text
        # b = password.index('码')
        # password = password[(b+2):(b+8)]
        print(password)
        password = password[12:15] + password[9:12]
        print(password)
        time.sleep(2)
        driver.back()
        driver.find_element(By.ID, 'edPassword').send_keys(password)
    # 返回提示信息
    code = 'new UiSelector().text("登录").className("android.widget.TextView")'
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
    time.sleep(1)
    # xpath = "//*[contains(@text,'{}')]".format(expectedalert2)
    alsettext.append(driver.find_element(By.XPATH, "//*[@class='android.widget.Toast']").text)
    time.sleep(20)
    driver.quit()
    return alsettext
def submit():
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '12',
        'deviceName': 'Miowii',
        'appPackage': 'com.example.smeceleapp',
        'appActivity': '.LoginActivity',
        'unicodeKeyboard': True,
        'resetKeyboard': True,
        'noReset': True,
        'newCommandTimeout': 6000,
        'automationName': 'UiAutomator2'
    }

    # 连接Appium Server，初始化自动化环境
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    # 设置缺省等待时间
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 'policy_checkbox').click()
    # 输入账号
    accout = '17752821932'
    driver.find_element(By.ID, 'edUser').send_keys(accout)
    driver.find_element(AppiumBy.ID, 'll_pwd_btn').click()
    time.sleep(3)
    driver.open_notifications()
    time.sleep(2)
    a = "//*[contains(@text,'验证码')]"
    password = driver.find_element(AppiumBy.XPATH, a).text
    b = password.index('码')
    password = password[(b+2):(b+8)]
    print(password)
    driver.back()
    driver.find_element(By.ID, 'edPassword').send_keys(password)
    code = 'new UiSelector().text("登录").className("android.widget.TextView")'
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
    time.sleep(3)
    driver.quit()
if __name__ == '__main__':
    # lsettext = submittest('否', '1775282', '0')
    # lsettext = submittest('是', '17752821932', '1')
    # lsettext = submittest('是', '122', '0')
    # print(lsettext[0], lsettext[1])
    submit()