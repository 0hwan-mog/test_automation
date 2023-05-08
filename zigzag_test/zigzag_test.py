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
from helpers import setup_teardown

def test_zigzag_alpha(setup_teardown):
    driver = setup_teardown
    print("testcase1 실행")
    sleep(2)
    el5 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="검색")
    print("상단 통합 검색 버튼 탭")
    el5.click()
    sleep(2)
    el6 = driver.find_element(
        by=AppiumBy.ID, value="com.croquis.zigzag.alpha:id/etSearchKeyword")
    print("검색어 입력 후 검색")
    el6.send_keys("원피스")
    driver.press_keycode(AndroidKey.ENTER)
    sleep(1)
    print("검색 결과 페이지 노출")
    sleep(1)
    #비슷한 상품 검색 기능 알림 토스트 처리
    try:
        toast = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button")))
        print("비슷한 상품 검색 기능 팝업 닫기")
        toast.click()
    except TimeoutException: 
        pass
    first_product = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.ImageView")))
    print("검색결과 목록중 첫번째 상품 탭")
    first_product.click()
    my_product = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[5]/android.view.View/android.view.View[2]/android.widget.Image")))
    print("찜 버튼 탭")
    my_product.click()
    sleep(2)
    print("testcase1 종료")
