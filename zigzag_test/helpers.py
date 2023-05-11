from time import sleep
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pytest
import os
import subprocess
from appium import webdriver

# 앱 최초실행시 알림 팝업 처리 함수
def handling_popup(driver):
    try:
        sleep(1)
        print("알림 허용 팝업 노출 여부 확인중")
        # 팝업 확인 버튼을 찾아 클릭
        confirm_button = driver.find_element(
            by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_deny_button")
        confirm_button.click()
        print("알림 설정 팝업 닫기 버튼 탭")
        sleep(1)
    except NoSuchElementException:
        # 확인 버튼이 없으면 팝업이 없다고 가정하고 그냥 넘어감
        pass

# 앱 실행 후 표시되는 온보딩 페이지, 푸시 알림 수신동의 팝업, 토스트 및 배너 처리 함수
def pass_onboarding_push_bottombanner(driver):
    try:
        print("온보딩 페이지 노출 여부 확인중")
        # 온보딩 페이지 처리
        complate_button = WebDriverWait(driver,2).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.croquis.zigzag.alpha:id/tvSelectionComplete")))
        complate_button.click()
        print("온보딩 페이지 선택완료 버튼 탭")
        sleep(1)
    except TimeoutException:
        pass

    
    try:
        print("푸시알림 수신 동의 토스트 노출 여부 확인중")
        sleep(1.5)
        # 푸시 알림 수신 팝업 처리
        confirm_button = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="안 받을래요/앱 푸시 알람 허용하지 않음")
        confirm_button.click()
        print("푸시 알림 허용하지 않음 버튼 탭")
        sleep(2)
    except NoSuchElementException:
        pass

    try:
        print("이벤트 토스트 노출 여부 확인중")
        # 이벤트 토스트 닫기 처리
        el1 = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.croquis.zigzag.alpha:id/close")))
        print("이벤트 토스트 닫기 처리")
        el1.click()
        sleep(1)
    except TimeoutException:
        pass

    # try:
    #     print("회원가입 유도 배너 노출 여부 확인중")
    #     el4 = WebDriverWait(driver, 5).until(
    #         EC.presence_of_element_located((AppiumBy.ID, "com.croquis.zigzag.alpha:id/btJoinEventBannerClose")))
    #     print("하단 배너 x버튼 탭")
    #     el4.click()
    #     sleep(1)
    # except TimeoutException:
    #     pass

@pytest.fixture(scope='function', autouse=True)
def setup_teardown():
    print("테스트 시작전 초기화")
    # apk 설치 경로를 apk_path에 저장
    apk_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'zigzag_alpha.apk')
   # 앱이 설치되어 있는지 확인
    installed_packages = subprocess.check_output(
        ['adb', 'shell', 'pm', 'list', 'packages']).decode('utf-8')
    app_installed = 'package:com.croquis.zigzag.alpha' in installed_packages

    if not app_installed:
        print("테스트 기기에 지그재그 알파 앱이 설치되어있지 않아 설치합니다.")
        # 앱이 설치되어 있지 않으면 설치합니다.
        subprocess.run(['adb', 'install', apk_path])
       

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
    handling_popup(driver)
    sleep(1)
    pass_onboarding_push_bottombanner(driver)
    # 테스트 함수에서 사용할 값을 픽스쳐함수에서 반환한다
    yield driver
    # 테스트 함수 실행 후 아래 코드가 실행되며 인스턴스를 정리한다.
    driver.quit()
    print("tearDown")
