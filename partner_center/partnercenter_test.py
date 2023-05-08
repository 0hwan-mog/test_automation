from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def changing_first_order(input_number):
    for i in range(0, input_number):
        # 첫번째 상품 선택
        first_order = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      "#MainFrame > div.BjciI0DwH9nqgG3nq4qb > div.PqoW0UJNFISUjXDn9nGX.false > div.react-in-mithril > div > div > div:nth-child(3) > div.IuQkXH8WhWwfXxZYXfA7 > div.v90TAbI9_qqLWKbM5Bes > div.W33T7liyyVLq6KNZolFE > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > label > span")))
        first_order.click()

        #택배사 입력
        delivery_company = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                           "#MainFrame > div.BjciI0DwH9nqgG3nq4qb > div.PqoW0UJNFISUjXDn9nGX.false > div.react-in-mithril > div > div > div:nth-child(3) > div.IuQkXH8WhWwfXxZYXfA7 > div.v90TAbI9_qqLWKbM5Bes > div.W33T7liyyVLq6KNZolFE > div > table > tbody > tr:nth-child(1) > td:nth-child(8) > select > option:nth-child(54)")))
        delivery_company.click()


        #송장번호 입력
        invoice_number = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                         "#MainFrame > div.BjciI0DwH9nqgG3nq4qb > div.PqoW0UJNFISUjXDn9nGX.false > div.react-in-mithril > div > div > div:nth-child(3) > div.IuQkXH8WhWwfXxZYXfA7 > div.v90TAbI9_qqLWKbM5Bes > div.W33T7liyyVLq6KNZolFE > div > table > tbody > tr:nth-child(1) > td:nth-child(9) > input")))
        invoice_number.send_keys("123")

        # 주문번호 복사
        first_order_number = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                             "#MainFrame > div.BjciI0DwH9nqgG3nq4qb > div.PqoW0UJNFISUjXDn9nGX.false > div.react-in-mithril > div > div > div:nth-child(3) > div.IuQkXH8WhWwfXxZYXfA7 > div.v90TAbI9_qqLWKbM5Bes > div.W33T7liyyVLq6KNZolFE > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > div > a"))).text

        # 배송중 처리
        change_to_shipping = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                             "#MainFrame > div.BjciI0DwH9nqgG3nq4qb > div.PqoW0UJNFISUjXDn9nGX.false > div.react-in-mithril > div > div > div:nth-child(3) > div.IuQkXH8WhWwfXxZYXfA7 > div.v90TAbI9_qqLWKbM5Bes > div:nth-child(1) > div:nth-child(1) > div.v1X79mJumnJXC9NnmMpo > button:nth-child(3) > div")))
        change_to_shipping.click()

        confirm = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                  "body > div:nth-child(16) > div > div > div > div.l4hwaeGnXUpN3IQf4w79 > button.vFG06QbNQRqLtuFJfjUu.primary.flex")))
        confirm.click()
        sleep(1)

        confirm = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "body > div:nth-child(16) > div > div > div > div.l4hwaeGnXUpN3IQf4w79 > button")))
        confirm.click()
        print("주문번호 ", first_order_number, "을(를) 배송중 처리했습니다.")


# 파트너센터 로그인 정보 입력
partnercenter_id = input("파트너센터 테스트계정을 입력하세요 : ")
partnercenter_password = input("테스트계정의 비밀번호를 입력하세요 : ")

# 구매자명 입력
client_name = input("구매자명을 입력하세요 : ")

# 배송중 처리할 주문건 수 입력
number_of_order = int(input("몇건의 주문건을 배송중 처리할까요?(숫자 입력) "))

# 크롬 브라우저 실행후 씨리얼핏 알파 로그인페이지 접속
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://shop.alpha.zigzag.kr/#!/login")

# 로그인 페이지에서 테스트 관리자 계정으로 로그인
id = driver.find_element(By.CSS_SELECTOR,
                         "#app > div > main > div > section > form > div.css-1lvmktx.e1yzhszp5 > input")
id.clear()
id.send_keys(partnercenter_id)

password = driver.find_element(By.CSS_SELECTOR,
                               "#app > div > main > div > section > form > div.css-1bmzcds.e1yzhszp5 > input[type=password]")
password.clear()
password.send_keys(partnercenter_password)
password.send_keys(Keys.RETURN)

# 쇼핑몰 목록에서 씨리얼핏 클릭
crealfit = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
    (By.PARTIAL_LINK_TEXT, "씨리얼힛")))
crealfit.click()

# 상품준비/배송 관리 탭 이동
preparing_page = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                 "#MainFrame > div.BjciI0DwH9nqgG3nq4qb > div.LdpHuutKeZBD0Zv33FBQ.false > ul.lo5J1r0wqaPRncdeDdug > li.f2TyJBK2uwv7KlKcJucW.DxstYBvlTQAE9ACUWhMQ > ul > li:nth-child(3) > span")))
preparing_page.click()

# #결제완료 목록 표시될때까지 대기
first_order = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      "#MainFrame > div.BjciI0DwH9nqgG3nq4qb > div.PqoW0UJNFISUjXDn9nGX.false > div.react-in-mithril > div > div > div:nth-child(3) > div.IuQkXH8WhWwfXxZYXfA7 > div.v90TAbI9_qqLWKbM5Bes > div.W33T7liyyVLq6KNZolFE > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > label > span")))

# 구매자명 입력
set_search_condition = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                       "#MainFrame > div.BjciI0DwH9nqgG3nq4qb > div.PqoW0UJNFISUjXDn9nGX.false > div.react-in-mithril > div > div > div:nth-child(2) > div.B46HCxUGYe2MMxeYwhrg > form > div:nth-child(2) > div > div > select > option:nth-child(2)")))

set_search_condition.click()

name_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                             "#MainFrame > div.BjciI0DwH9nqgG3nq4qb > div.PqoW0UJNFISUjXDn9nGX.false > div.react-in-mithril > div > div > div:nth-child(2) > div.B46HCxUGYe2MMxeYwhrg > form > div:nth-child(2) > div > div > input")))

name_field.send_keys(client_name)

# 조회기간 '1개월'로 변경
duration = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                           "#MainFrame > div.BjciI0DwH9nqgG3nq4qb > div.PqoW0UJNFISUjXDn9nGX.false > div.react-in-mithril > div > div > div:nth-child(2) > div.B46HCxUGYe2MMxeYwhrg > form > div:nth-child(3) > div > div > div > div > div > div:nth-child(1) > div > label:nth-child(3)")))
duration.click()

#검색 버튼 클릭
searching = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                            "#MainFrame > div.BjciI0DwH9nqgG3nq4qb > div.PqoW0UJNFISUjXDn9nGX.false > div.react-in-mithril > div > div > div:nth-child(2) > div.B46HCxUGYe2MMxeYwhrg > form > div.pypaPpeW9YidFC38ttL7 > button.vFG06QbNQRqLtuFJfjUu.primary.large.tall")))
searching.click()

searching = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                            "#MainFrame > div.BjciI0DwH9nqgG3nq4qb > div.PqoW0UJNFISUjXDn9nGX.false > div.react-in-mithril > div > div > div:nth-child(2) > div.B46HCxUGYe2MMxeYwhrg > form > div.pypaPpeW9YidFC38ttL7 > button.vFG06QbNQRqLtuFJfjUu.primary.large.tall")))
searching.click()

# 배송중 처리


try:
    changing_first_order(number_of_order)
    print("알파 씨리얼핏에", client_name, "님이 1개월 이내 생성한 결제완료 주문건들중 최신순으로", number_of_order, "건을 '배송중' 상태로 변경했습니다.")

except:
    print("오류가 발생했습니다.")

driver.quit()