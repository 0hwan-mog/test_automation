from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from datetime import datetime
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
import pytest

@pytest.fixture(scope='function', autouse=True)
def setup_teardown():
    capabilities = {
                'platformName': 'Android',
                'platformVersion': '13.0',
                'deviceName': 'emulator-5554',
                'appPackage': 'com.croquis.zigzag.alpha',
                'appActivity': 'com.croquis.zigzag.presentation.ui.splash.SplashActivity',
                'automationName': 'UiAutomator2',
                'noReset': True
            }

    driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', capabilities)
    sleep(3)

    #테스트 함수에서 사용할 값을 픽스쳐함수에서 반환한다
    yield driver
    #테스트 함수 실행 후 아래 코드가 실행되며 인스턴스를 정리한다.
    driver.quit()
    print("tearDown")

def test_zigzag_alpha():
    print("testcase1 실행")
    sleep(3)
    print("testcase1 종료")