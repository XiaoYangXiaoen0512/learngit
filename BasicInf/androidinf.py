def AndroidInfo():
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '10',
        'deviceName': 'MJ',
        'appPackage': 'smec.com.inst_one_stop_app_android',
        'appActivity': '.mvp.activity.SplashActivity',
        'unicodeKeyboard': True,
        'resetKeyboard': True,
        'noReset': True,
        'newCommandTimeout': 6000,
        'automationName': 'UiAutomator2'
    }
    return desired_caps
