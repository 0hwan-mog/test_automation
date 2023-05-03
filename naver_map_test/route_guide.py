from playwright.sync_api import Playwright, sync_playwright, expect
from time import sleep
from PIL import Image


def find_route(playwright: Playwright, browser, context) -> None:
    starting_point = input("출발지를 입력하세요 : ")
    destination = input("도착지를 입력하세요 : ")
    mobilities = ['대중교통', '자동차', '도보', '자전거']

    while True:
        print("경로 종류")
        for i, option in enumerate(mobilities):
            print(f'{i + 1}. {option}')

        mobility = input('어떤 경로를 원하시나요? 번호 입력 : ')
        if mobility.isdigit() and 1 <= int(mobility) <= len(mobilities):
            break
        else:
            print('잘못된 번호를 입력하였습니다. 다시 입력하세요.')

    selected_option = mobilities[int(mobility) - 1]

    page = context.new_page()
    page.goto("https://map.naver.com/v5/directions/-/-/-/transit?c=15,0,0,2,dh")

    if selected_option == '대중교통':
        print(f'{selected_option}로 이동하는 경로를 검색합니다.')

    elif selected_option == '자동차':
        print(f'{selected_option}로 이동하는 경로를 검색합니다.')
        page.get_by_role("tab", name="자동차").click()

    elif selected_option == '도보':
        print(f'{selected_option}로 이동하는 경로를 검색합니다.')
        page.get_by_role("tab", name="도보").click()
    else:
        print(f'{selected_option}로 이동하는 경로를 검색합니다.')
        page.get_by_role("tab", name="자전거").click()
        # 경로 탐색에 수초가 걸리므로 멈추지 않고 진행중임을 확인하기 위한 장치로서 진행률 표시를 하드코딩
        print("5%", end='\r')
    page.get_by_label("출발지를 입력하세요").click()
    page.get_by_label("출발지를 입력하세요").fill(starting_point)
    page.get_by_label("출발지를 입력하세요").press("Enter")
    sleep(0.5)
    page.get_by_label("도착지 입력").click()
    page.get_by_label("도착지를 입력하세요").fill(destination)
    page.get_by_label("도착지를 입력하세요").press("Enter")
    sleep(0.5)
    page.get_by_role("button", name="길찾기").click()
    print("20%", end='\r')
    sleep(1)
    print("45%", end='\r')
    sleep(1)
    page.locator(".step_bottom_area").first.click()
    sleep(0.3)
    page.locator(".step_bottom_area").first.click()
    print("60%", end='\r')
    sleep(1)
    print("89%", end='\r')
    # 검색된 경로 이미지 캡쳐후 저장
    page.screenshot(path="route_screenshot.png", full_page=True)
    context.tracing.stop(path="trace_route_guide.zip")
    print("100%", end='\r')
    # ---------------------
    print("경로를 확인하세요")
    # 경로 검색 결과를 보여줌
    Image.open("route_screenshot.png").show()

    # 이 블록에서 Playwright 객체를 생성하고, 위에 정의한 함수를 실행
    # 함수를 이어서 추가할 수 있음
with sync_playwright() as playwright:
    # 테스트 시나리오 추가를 위해 테스트 초기 설정(browser, context)은 공통 영역으로 분리
    # headless 브라우저로 실행하는것을 기본으로 설정. 실행과정 확인 필요시 False로 변경.
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context(viewport={"width": 1920, "height": 1550})
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    # 위에 정의한 경로 검색 함수 실행
    find_route(playwright, browser, context)
    # 테스트 종료 후 리소스 정리
    context.close()
    browser.close()