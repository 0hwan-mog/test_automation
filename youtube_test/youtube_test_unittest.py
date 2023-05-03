import unittest
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


# 공통으로 사용할 상위 클래스. setUp과 tearDown을 클래스마다 정의하지 않기 위해 사용
class BaseTestAppium(unittest.TestCase):
    # setUp 메서드는 unittest.TestCase에 정의되어있지만 비어있다. 메서드 오버라이딩을 통해 다시 정의한다.
    def setUp(self):
        capabilities = {
            'platformName': 'Android',
            'platformVersion': '13.0',
            'deviceName': 'emulator-5554',
            'appPackage': 'com.google.android.youtube',
            'appActivity': 'com.google.android.apps.youtube.app.WatchWhileActivity',
            'automationName': 'UiAutomator2',
            'noReset': True
        }

        self.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', capabilities)
        # 클래스 내에서 정의한 메서드는 클래스 내부에서 호출 가능하다.
        sleep(3)
        # 테스트 케이스에서 사용할 수 있는 오늘 날짜 데이터용 변수 생성
        today = datetime.now()
        self.today = "{0}월 {1}일".format(today.month, today.day)

    def tearDown(self):
        # 테스트 시나리오 종료할 때마다 앱 종료
        self.driver.press_keycode(AndroidKey.BACK)
        self.driver.quit()
    # 접근성 설정 토스트 및 팝업 노출시 처리를 위한 함수 정의

    def handle_popup(self):
        try:
            # 팝업 확인 버튼을 찾아 클릭
            confirm_button = self.driver.find_element(
                by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[2]")

            confirm_button.click()
            print("접근성 설정 팝업 닫기 버튼 탭")

            sleep(2)
        except NoSuchElementException:
            # 확인 버튼이 없으면 팝업이 없다고 가정하고 그냥 넘어감
            pass
        try:
            # 토스트 닫기 버튼 찾아 클릭
            confirm_button2 = self.driver.find_element(
                by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.GridLayout/android.view.ViewGroup/android.widget.Button[1]")
            print("접근성 설정 토스트 닫기 버튼 탭")
            confirm_button2.click()
            sleep(2)
        except NoSuchElementException:
            # 확인 버튼이 없으면 팝업이 없다고 가정하고 그냥 넘어감
            pass

# youtube 테스트 클래스
class Testsuite1(BaseTestAppium):
    # unittest.main()이 실행되면 test_로 시작하는 메서드를 테스트 케이스로 인식한다.
    def test_search_and_play_video1(self):
        print("테스트 케이스 1번 실행중")
        self.handle_popup()
        el2 = self.driver.find_element(
            by=AppiumBy.ACCESSIBILITY_ID, value="검색")
        print("검색 버튼 탭")
        el2.click()
        el3 = self.driver.find_element(
            by=AppiumBy.ID, value="com.google.android.youtube:id/search_edit_text")
        print("검색어 입력 후 검색")
        el3.send_keys("{0} 오늘의 뉴스".format(self.today))
        sleep(3)
        self.driver.press_keycode(AndroidKey.ENTER)

        sleep(2)
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(
        self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(500, 600)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        print("5초간 재생")
        sleep(5)
        print("테스트 케이스 1번 실행 종료")

    def test_search_and_play_video2(self):
        print("테스트 케이스 2번 실행중")
        self.handle_popup()
        el2 = self.driver.find_element(
            by=AppiumBy.ACCESSIBILITY_ID, value="검색")
        el2.click()
        el3 = self.driver.find_element(
            by=AppiumBy.ID, value="com.google.android.youtube:id/search_edit_text")
        el3.send_keys("{0} 뉴스 속보".format(self.today))
        sleep(3)
        self.driver.press_keycode(AndroidKey.ENTER)
        sleep(2)
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(
            self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(500, 600)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        sleep(5)
        print("테스트 케이스 2번 실행 종료")




if __name__ == '__main__':
    unittest.main()
    # unittest.main()이 실행되면 테스트가 정의된 클래스를 찾아 인스턴스를 자동으로 생성한다.
    # 테스트 케이스 실행 전 setUp 메서드를 실행한다.
    # test_* 메서드를 찾아 테스트 케이스로 인식한다.
