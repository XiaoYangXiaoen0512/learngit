from appium import webdriver
import time
from appium.webdriver.common.appiumby import AppiumBy


def appquit():
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
    driver.find_element(AppiumBy.ID, '').click()
    time.sleep(1)
    code = 'new UiSelector().text("退出登录").className("android.widget.TextView")'
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
    time.sleep(1)
    driver.find_element(AppiumBy.ID, '').click()
    driver.quit()