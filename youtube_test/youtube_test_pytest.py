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

def handle_popup(driver):
        try:
            # 팝업 확인 버튼을 찾아 클릭
            confirm_button = driver.find_element(
                by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[2]")

            confirm_button.click()
            print("접근성 설정 팝업 닫기 버튼 탭")

            sleep(2)
        except NoSuchElementException:
            # 확인 버튼이 없으면 팝업이 없다고 가정하고 그냥 넘어감
            pass
        try:
            # 토스트 닫기 버튼 찾아 클릭
            confirm_button2 = driver.find_element(
                by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.GridLayout/android.view.ViewGroup/android.widget.Button[1]")
            print("접근성 설정 토스트 닫기 버튼 탭")
            confirm_button2.click()
            sleep(2)
        except NoSuchElementException:
            # 확인 버튼이 없으면 팝업이 없다고 가정하고 그냥 넘어감
            pass
#픽스쳐를 통해 테스트 전후 처리를 수행한다. scope 옵션을 function으로 설정하였기 때문에 각 테스트 함수의 실행전/후 픽스쳐가 실행된다.
@pytest.fixture(scope='function', autouse=True)
def setup_teardown():
    capabilities = {
            'platformName': 'Android',
            'platformVersion': '13.0',
            'deviceName': 'emulator-5554',
            'appPackage': 'com.google.android.youtube',
            'appActivity': 'com.google.android.apps.youtube.app.WatchWhileActivity',
            'automationName': 'UiAutomator2',
            'noReset': True
        }

    driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', capabilities)
    sleep(3)
    handle_popup(driver)  # 팝업 처리를 호출합니다.

    today_info = datetime.now()
    today = "{0}월 {1}일".format(today_info.month, today_info.day)
    print("setUp")
    #테스트 함수에서 사용할 값을 픽스쳐함수에서 반환한다
    yield driver,today

    driver.press_keycode(AndroidKey.BACK)
    sleep(2)
    driver.quit()
    print("tearDown")

#공통된 동작을 함수로 작성해두고, 테스트 함수에서는 검색어만 변경하여 사용함으로써 테스트 코드를 효율적으로 작성한다.
def search_and_play_video(driver, today, search_keyword):
        search_button = driver.find_element(
            by=AppiumBy.ACCESSIBILITY_ID, value="검색")
        print("검색 버튼 탭")
        search_button.click()
        input_field = driver.find_element(
            by=AppiumBy.ID, value="com.google.android.youtube:id/search_edit_text")
        print("검색어 입력 후 검색")
        input_field.send_keys("{0} {1}".format(today,search_keyword))
        sleep(3)
        driver.press_keycode(AndroidKey.ENTER)

        sleep(2)
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(500, 600)
        print("첫 번째 영상 클릭")
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        print("5초간 재생")
        sleep(5)
        print("테스트 케이스 1번 실행 종료")

def test_search_and_play_video1(setup_teardown):
    driver,today = setup_teardown 
    # 이때 setup_teardown 뒤에 괄호를 추가하면 오류가 발생할 수 있다. 
    # 테스트 함수에서 픽스쳐를 사용할 때는 괄호 없이 픽스쳐의 이름만 인자로 전달하고, pytest가 픽스쳐를 관리하도록 하는 것이 좋다
    print("테스트 케이스 1번 실행중")
    search_and_play_video(driver,today,"오늘의 뉴스")
    print("테스트 케이스 1번 실행중")

def test_search_and_play_video2(setup_teardown):
    driver,today = setup_teardown
    print("테스트 케이스 2번 실행중")
    search_and_play_video(driver,today,"오늘의 속보")
    print("테스트 케이스 2번 실행중")
