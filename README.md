코드 작성 환경 : Mac OS Monterey /Python 3.9.6 / 안드로이드 에뮬레이터(OS13)

1. Python 3.9.6 버전을 설치합니다. (설치 가이드: [링크](https://www.python.org/downloads/))
2. 터미널에서 `pip3 install -r requirements.txt` 명령어를 입력하여 의존성 패키지를 설치합니다.
3. 터미널에서 'appium' 커맨드를 통해 appium 서버를 시작합니다. 
4. 각 테스트 파일에 있는 capabilities의 값 중 platformVersion과 deviceName은 각자 사용하는 테스트 기기에 맞게 설정해주세요(현재 코드는 안드로이드 에뮬레이터가 실행되고 있을때를 기준으로 작성되었습니다.)
5. 새로운 터미널 창을 열어 테스트 파일을 실행합니다. 
6. youtube_test_pytest.py 파일 외의 파일은 해당 파일이 있는 디렉토리로 이동한 뒤 "python3 {파일이름}" 커맨드를 통해 실행합니다.
7. youtube_test_pytest.py 파일은 해당 파일이 있는 디렉토리로 이동한 뒤 "pytest youtube_test_pytest.py" 커맨드를 통해 실행합니다.
