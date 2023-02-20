from appium import webdriver
from selenium.webdriver.common.by import By
import time
from appium.webdriver.extensions.android.nativekey import AndroidKey
import emailpost
import datetime
desired_caps = {
  'platformName': 'Android',
  'platformVersion': '12',
  'deviceName': 'Miowii',
  'appPackage': 'smec.com.inst_one_stop_app_android',
  'appActivity': '.mvp.activity.SplashActivity',
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
driver.find_element(By.ID, 'et_user').clear()
driver.find_element(By.ID, 'et_user').send_keys('f560026')
time.sleep(2)
driver.find_element(By.ID, 'ey_pwd').clear()
driver.find_element(By.ID, 'ey_pwd').send_keys('Lj303030')
driver.find_element(By.ID, 'but_log').click()
time.sleep(5)
# 进入催款函管理模块
driver.find_element(By.ID, 'guanli').click()
# driver.find_element(By.ID, 'img_sty').click()
driver.tap([(800, 1100)], 300)
time.sleep(10)
# 搜索安装合同号
driver.find_element(By.ID, 'et_view').click()
driver.find_element(By.ID, 'et_view').send_keys('14AZ-9679')
driver.press_keycode(AndroidKey.ENTER)
time.sleep(10)
# 上传催款函
driver.tap([(50, 450)], 300)
driver.find_element(By.ID, 'but_upload').click()
time.sleep(3)
driver.find_element(By.ID, 'up_tv').click()
time.sleep(2)
driver.tap([(500, 900)], 300)
driver.tap([(890, 140)], 300)
driver.implicitly_wait(10)
driver.find_element(By.ID, 'but').click()
driver.find_element(By.ID, 'btnSubmit').click()
time.sleep(10)
# 验证催款函
# driver.find_element(By.ID, 'et_view').send_keys('14AZ-9679')
# driver.press_keycode(AndroidKey.ENTER)
# time.sleep(10)
driver.swipe(start_x=510, start_y=428, end_x=0, end_y=428, duration=300)
driver.implicitly_wait(10)
cuikuanhan = driver.find_element(By.ID, 'smec.com.inst_one_stop_app_android:id/collectionCreationDate').text
print(cuikuanhan)
nowtime = datetime.datetime.now()
b = nowtime.strftime("%Y%m%d")
if cuikuanhan == b:
  print('上传成功')
  emailpost.email_send()
  driver.quit()
else:
  print('上传失败')