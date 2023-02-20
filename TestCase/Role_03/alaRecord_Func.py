from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
import time
import datetime
import calendar
from selenium.common import NoSuchElementException

def alarecord():
    global a_ym, atime
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
    # # 进入报警记录页面
    driver.find_element(By.ID, 'navigation_home').click()
    time.sleep(2)
    code = 'new UiSelector().text("报警记录").className("android.widget.TextView")'
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
    time.sleep(2)
    # 筛选时间
    today = datetime.date.today()
    this_month = today.replace(month=today.month)
    last_month = today.replace(month=today.month - 1)
    this_month_end = datetime.datetime(last_month.year, last_month.month,
                                       calendar.monthrange(last_month.year, last_month.month)[1])
    this_month_end = this_month_end.strftime("%Y%m%d")
    last_month = last_month.strftime("%Y%m")
    try:
        driver.find_element(AppiumBy.ID, 'overview_daily_errors_item_content_time')
    except NoSuchElementException:
        # 筛选上月记录
        driver.find_element(AppiumBy.ID, 'alarm_date_picker_start').click()
        time.sleep(1)
        driver.swipe(start_x=500, start_y=2008, end_x=500, end_y=2216, duration=800)
        time.sleep(1)
        code = 'new UiSelector().text("1").className("android.widget.TextView")'
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
        code = 'new UiSelector().text("{}").className("android.widget.TextView")'.format(this_month_end[6:])
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
        code = 'new UiSelector().text("确定").className("android.widget.TextView")'
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
        datatime = 1
    else:
        # 筛选本月记录
        atime = driver.find_element(AppiumBy.ID, 'overview_daily_errors_item_content_time').text
        driver.find_element(AppiumBy.ID, 'alarm_date_picker_start').click()
        time.sleep(1)
        code = 'new UiSelector().text("{}").className("android.widget.TextView")'.format(str(int(atime[8:10])))
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
        datatime = 0
    try:
        driver.find_element(AppiumBy.ID, 'overview_daily_errors_item_content_time')
    except NoSuchElementException:
        a = '1'
        last_month = '2'
    else:
        a = driver.find_element(AppiumBy.ID, 'overview_daily_errors_item_content_time').text
        a = a[:10]
        a_ym = a[:4] + a[5:7]
    print(a, a_ym,  last_month)
    while datatime == 1:
        if (a_ym == last_month) and (1 < int(a[8:10]) < int(this_month_end[6:])):
            text4 = '日期筛选成功'
            break
        else:
            text4 = '日期筛选失败'
            break
    else:
        if (a_ym == this_month) and (a[8:10] == atime[8:10]):
            text4 = '日期筛选成功'
        else:
            text4 = '日期筛选失败'
    # 筛选类型
    code = 'new UiSelector().text("全部").className("android.widget.TextView")'
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
    time.sleep(1)
    code = 'new UiSelector().text("工单").className("android.widget.TextView")'
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
    time.sleep(1)
    a1 = driver.find_element(AppiumBy.ID, 'overview_daily_errors_item_title_name').text
    time.sleep(1)
    code = 'new UiSelector().text("工单").className("android.widget.TextView")'
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
    time.sleep(1)
    code = 'new UiSelector().text("事件").className("android.widget.TextView")'
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
    time.sleep(1)
    code = 'new UiSelector().text("选择梯号").className("android.widget.TextView")'
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
    time.sleep(1)
    driver.find_element(AppiumBy.ID, 'search_src_text').send_keys(a1)
    time.sleep(1)
    driver.find_element(AppiumBy.ID, 'search_ele_item_title_name').click()
    time.sleep(1)
    try:
        driver.find_element(AppiumBy.ID, 'overview_daily_errors_item_title_name')
    except NoSuchElementException:
        text2 = '类型筛选成功'
    else:
        text2 = '类型筛选失败'
    code = 'new UiSelector().text("事件").className("android.widget.TextView")'
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
    time.sleep(1)
    code = 'new UiSelector().text("全部").className("android.widget.TextView")'
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
    time.sleep(1)
    driver.find_element(AppiumBy.ID, 'text_single_ele_name_xx').click()
    time.sleep(1)
    # 筛选梯号
    code = 'new UiSelector().text("选择梯号").className("android.widget.TextView")'
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
    time.sleep(1)
    driver.find_element(AppiumBy.ID, 'search_src_text').send_keys(a1)
    code = 'new UiSelector().text("2A-2").className("android.widget.TextView")'
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
    time.sleep(1)
    b = driver.find_element(AppiumBy.ID, 'overview_daily_errors_item_title_name').text
    driver.find_element(AppiumBy.ID, 'text_single_ele_name_xx').click()
    print(a1, b)
    if a1 == b:
        text3 = '梯号筛选成功'
    else:
        text3 = '梯号筛选失败'
    time.sleep(1)
    print(text2, text3, text4)
    if ('成功' in text2) and ('成功' in text3) and ('成功' in text4):
        alsetText = '测试通过'
    else:
        alsetText = '测试未通过'
    driver.quit()
    return alsetText
def alarecordtest2():
    global alsetText
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
    # 进入报警记录页面
    code = 'new UiSelector().text("报警记录").className("android.widget.TextView")'
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
    time.sleep(2)
    # 搜索错误数据
    code = 'new UiSelector().text("选择梯号").className("android.widget.TextView")'
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code).click()
    time.sleep(1)
    a = '738784874'
    driver.find_element(AppiumBy.ID, 'search_src_text').send_keys(a)
    try:
        code = 'new UiSelector().text("{}").className("android.widget.TextView")'.format(a)
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code)
    except NoSuchElementException:
        alsetText = '测试通过'
    else:
        alsetText = '测试失败'
    driver.quit()
    return alsetText
if __name__ == '__main__':
    alset = alarecord()
    # alset1 = alarecordtest2()
    print(alset)