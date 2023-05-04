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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from helpers import handling_popup, pass_onboarding_push_bottombanner, setup_teardown

def test_zigzag_alpha(setup_teardown):
    driver = setup_teardown
    print("testcase1 실행")
    sleep(2)
    el5 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="검색")
    print("검색어 입력필드 탭")
    el5.click()
    sleep(2)
    el6 = driver.find_element(
        by=AppiumBy.ID, value="com.croquis.zigzag.alpha:id/etSearchKeyword")
    print("검색어 입력 후 검색")
    el6.send_keys("원피스")
    driver.press_keycode(AndroidKey.ENTER)
    sleep(3)
    print("검색 결과 페이지 노출")
    sleep(1)
    print("testcase1 종료")
