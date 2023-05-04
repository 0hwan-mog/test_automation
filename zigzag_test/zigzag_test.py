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

# 앱 최초실행시 알림 팝업 처리 함수


def handling_popup(driver):
    try:
        # 팝업 확인 버튼을 찾아 클릭
        confirm_button = driver.find_element(
            by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_deny_button")
        confirm_button.click()
        print("알림 설정 팝업 닫기 버튼 탭")
        sleep(2)
    except NoSuchElementException:
        # 확인 버튼이 없으면 팝업이 없다고 가정하고 그냥 넘어감
        pass


def pass_onboarding_push_bottombanner(driver):
    try:
        # 온보딩 페이지 처리
        confirm_button = driver.find_element(
            by=AppiumBy.ACCESSIBILITY_ID, value="선택완료/다음으로")
        confirm_button.click()
        print("온보딩 페이지 선택완료 버튼 탭")
        sleep(2)
    except NoSuchElementException:
        # 선택완료 버튼이 없으면 온보딩페이지 노출되지 않았다고가정하고 그냥 넘어감
        pass

    try:
        # 푸시 알림 수신 팝업 처리
        confirm_button = driver.find_element(
            by=AppiumBy.ACCESSIBILITY_ID, value="안 받을래요/앱 푸시 알람 허용하지 않음")
        confirm_button.click()
        print("푸시 알림 허용하지 않음 버튼 탭")
        sleep(2)
    except NoSuchElementException:
        # 버튼이 없으면 팝업이 없다고 가정하고 그냥 넘어감
        pass
    try:
        # 이벤트 토스트 닫기 처리
        sleep(1)
        el1 = driver.find_element(
            by=AppiumBy.ID, value="com.croquis.zigzag.alpha:id/close")
        print("이벤트 토스트 닫기 처리")
        el1.click()
        sleep(1)
    except NoSuchElementException:
        pass
    try:
        sleep(3)
        el4 = driver.find_element(
            by=AppiumBy.ID, value="com.croquis.zigzag.alpha:id/btJoinEventBannerClose")
        print("하단 배너 x버튼 탭")
        el4.click()
        sleep(1)
    except NoSuchElementException:
        pass


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
    handling_popup(driver)
    pass_onboarding_push_bottombanner(driver)
    # 테스트 함수에서 사용할 값을 픽스쳐함수에서 반환한다
    yield driver
    # 테스트 함수 실행 후 아래 코드가 실행되며 인스턴스를 정리한다.
    driver.quit()
    print("tearDown")


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
