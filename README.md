# image2latex_mathpix
mathpix api를 사용하여 screenshot을 찍고 latex 문법으로 변형해주는 프로그램입니다.

먼저 https://mathpix.com/ 에 가입 후 

My account에서 Get API Keys에 들어가서 Accept 클릭

다음 화면에서 결제 카드를 입력 1000회 이상 이용 시 부터 1회당 0.004 달러 결제됨.

![캡ddd처](https://user-images.githubusercontent.com/53217819/91630925-a1042080-ea10-11ea-9dfb-5d07f791b349.PNG)

카드 입력 후 API ID와 API KEY를 확인

![캡dsdsdsd처](https://user-images.githubusercontent.com/53217819/91630926-a2354d80-ea10-11ea-86b9-4e21a836368c.PNG)

make_api.exe 파일을 실행하고 확인한 API_ID와 API_KEY를 입력 remain_count는 남은 횟수 입력(기본 1000)

![make_api](https://user-images.githubusercontent.com/53217819/91631030-330c2900-ea11-11ea-8008-4b3bd4beb75b.png)

im2latex.exe를 실행 후 변환하고자 하는 수식 부분을 클릭하고 Enter입력

Mathpix 서버와 통신 후 결과값이 클립보드에 copy됨.

![ezgif com-video-to-gif (1)](https://user-images.githubusercontent.com/53217819/91631335-c6465e00-ea13-11ea-8064-2265b87db3fb.gif)
