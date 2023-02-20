from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
import time
from selenium.common import NoSuchElementException

def devview():
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
    a_con = driver.find_element(AppiumBy.ID, 'single_ele_status_archives_content_productContract').text
    time.sleep(1)
    # 进入保养工单页面
    code = 'new UiSelector().text("保养工单").className("android.widget.TextView")'
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
    time.sleep(1)
    # 切换电梯
    driver.find_element(AppiumBy.ID, 'text_single_ele_name').click()
    time.sleep(1)
    b = '2A-2'
    driver.find_element(AppiumBy.ID, 'search_src_text').send_keys(b)
    time.sleep(1)
    driver.find_element(AppiumBy.ID, 'search_ele_item_title_name').click()
    time.sleep(1)
    code = 'new UiSelector().text("状态监控").className("android.widget.TextView")'
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
    time.sleep(1)
    b_con = driver.find_element(AppiumBy.ID, 'single_ele_status_archives_content_productContract').text
    if a_con != b_con:
        alsettext = '测试通过'
    else:
        alsettext = '测试失败'
    driver.quit()
    return alsettext
def devviewtest():
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
    a = '837848994'
    driver.find_element(AppiumBy.ID, 'search_src_text').send_keys(a)
    try:
        code = 'new UiSelector().text("{}").className("android.widget.TextView")'.format(a)
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code)
    except NoSuchElementException:
        alsettext1 = '测试通过'
    else:
        alsettext1 = '测试失败'
    a = '2A-1'
    driver.find_element(AppiumBy.ID, 'search_src_text').send_keys(a)
    code = 'new UiSelector().text("{}").className("android.widget.TextView")'.format(a)
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
    code = 'new UiSelector().text("{}").className("android.widget.TextView")'.format(a)
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
    a = '893903891'
    driver.find_element(AppiumBy.ID, 'search_src_text').send_keys(a)
    try:
        code = 'new UiSelector().text("{}").className("android.widget.TextView")'.format(a)
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code)
    except NoSuchElementException:
        alsettext2 = '测试通过'
    else:
        alsettext2 = '测试失败'
    alsetText = [alsettext1, alsettext2]
    driver.quit()
    return alsetText
if __name__ == '__main__':
    # alsetText = devview()
    alsetText = devviewtest()
    print(alsetText)