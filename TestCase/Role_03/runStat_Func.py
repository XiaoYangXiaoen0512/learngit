from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
import time
import datetime


def runstat():
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
    # 登录
    # driver.find_element(AppiumBy.ID, 'edUser').send_keys('111')
    # driver.find_element(AppiumBy.ID, 'edPassword').send_keys('111')
    # time.sleep(2)
    # code = 'new UiSelector().text("登录").className("android.widget.TextView")'
    # driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
    # 进入云View页面
    driver.find_element(By.ID, 'navigation_home').click()
    time.sleep(2)
    # 进入电梯列表页面
    code = 'new UiSelector().text("电梯列表").className("android.widget.TextView")'
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
    time.sleep(1)
    # 筛选电梯，点击电梯卡片进入设备查看页面
    code = 'new UiSelector().text("选择梯号").className("android.widget.TextView")'
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
    time.sleep(1)
    a = '2A-1'
    driver.find_element(AppiumBy.ID, 'search_src_text').send_keys(a)
    time.sleep(1)
    driver.find_element(AppiumBy.ID, 'search_ele_item_title_name').click()
    time.sleep(1)
    # 进入运行统计页面
    code = 'new UiSelector().text("运行统计").className("android.widget.TextView")'
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
    time.sleep(1)
    # 筛选测试
    code = 'new UiSelector().text("运行次数").className("android.widget.TextView")'
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
    time.sleep(1)
    code = 'new UiSelector().text("运行时间").className("android.widget.TextView")'
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
    time.sleep(1)
    code = 'new UiSelector().text("运行时间").className("android.widget.TextView")'
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
    time.sleep(1)
    code = 'new UiSelector().text("运行距离").className("android.widget.TextView")'
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
    time.sleep(1)
    code = 'new UiSelector().text("运行距离").className("android.widget.TextView")'
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
    time.sleep(1)
    code = 'new UiSelector().text("各楼层开关门次数").className("android.widget.TextView")'
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
    time.sleep(1)
    # 年月切换测试
    code = 'new UiSelector().text("日").className("android.widget.TextView")'
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
    time.sleep(1)
    code = 'new UiSelector().text("月").className("android.widget.TextView")'
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
    time.sleep(1)
    code = 'new UiSelector().text("年").className("android.widget.TextView")'
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
    time.sleep(1)
    # 次数查看
    driver.find_element(AppiumBy.ID, 'btn_everyFloorOpenCloseCountDetails').click()
    time.sleep(1)
    a = driver.find_element(AppiumBy.ID, 'txtOne').text
    if a == '各楼层停靠次数':
        alsettext3 = '年月切换测试成功'
    else:
        alsettext3 = '年月切换测试失败'
    if '成功' in alsettext3:
        alsettext = '测试通过'
    else:
        alsettext = '测试失败'
    driver.quit()
    return alsettext
if __name__ == '__main__':
    a = runstat()
    print(a)