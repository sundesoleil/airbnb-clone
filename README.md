# 에어비앤비 클론
[노마드코더 에어비앤비 클론코딩](https://nomadcoders.co/airbnb-clone, "nomadcoder link") 강의를 바탕으로 에어비앤비 사이트를 클론 코딩

# 개발 환경
Python, Django, tailwind css

# 주요 기능
* 게스트, 호스트 시스템
* 소셜(카카오톡, 깃허브) 연동 로그인 및 회원가입 
* 다이렉트 메시지
* 위시 리스트
* 예약
* 리뷰
* 검색
* 영어/한국어/스페인어 3가지 언어로 서비스 제공

# 구현 화면
1. 메인화면

![127 0 0 1_8000_ (1)](https://user-images.githubusercontent.com/72296755/116498133-fcf6b000-a8e3-11eb-8ad9-364ab0d735e1.png)

-> 상단바에 검색창, body 부분에 방 목록 표시

2. 회원가입 및 로그인
![image](https://user-images.githubusercontent.com/72296755/116498206-2dd6e500-a8e4-11eb-9358-5e3458beb89b.png)
![image](https://user-images.githubusercontent.com/72296755/116498262-4fd06780-a8e4-11eb-9cf0-54d0a2da5171.png)

-> 자체 회원가입/로그인 or 깃허브 or 카카오톡

3. 방 상세 페이지
![127 0 0 1_8000_rooms_471_](https://user-images.githubusercontent.com/72296755/116498386-9756f380-a8e4-11eb-9ce1-490d50699187.png)
-> amenities, facilities, house rules 등 룸 컨디션과 리뷰 목록 표시

4. 위시 리스트 저장
![wish](https://user-images.githubusercontent.com/72296755/116498830-aa1df800-a8e5-11eb-892e-b5883c341cc3.png)
-> 방 상세 페이지에서 save to favorites 클릭 

![wish2](https://user-images.githubusercontent.com/72296755/116498942-e6e9ef00-a8e5-11eb-8dc3-874a83f232d3.png)
-> 상단 오른쪽에 favorites에 1개가 추가됨과, 상세 페이지에서 remove from favorites로 바뀌었음을 확인할 수 있다.

5. 예약
![image](https://user-images.githubusercontent.com/72296755/116499018-1c8ed800-a8e6-11eb-93cd-81512b3607d8.png)
-> 달력에서 예약을 원하는 날짜를 선택하면 예약이 된다. 

![image](https://user-images.githubusercontent.com/72296755/116499090-434d0e80-a8e6-11eb-99d9-66a4e98a60de.png)
-> 예약한 방과 예약 상태가 뜨는 것을 확인할 수 있다.

6. 호스팅 시작하기
![image](https://user-images.githubusercontent.com/72296755/116499141-5fe94680-a8e6-11eb-8f1c-4f8d1d084512.png)
-> 상단바에 있는 start hosting 버튼을 클릭

![image](https://user-images.githubusercontent.com/72296755/116499160-6c6d9f00-a8e6-11eb-8800-5ecb41677efd.png)
-> stop hosting과 create room이 뜬 것으로 보아, 호스팅이 가능한 상태로 변했음을 확인할 수 있다.

![127 0 0 1_8000_rooms_create_ (2)](https://user-images.githubusercontent.com/72296755/116499501-44cb0680-a8e7-11eb-9492-4259737680a6.png)
-> create room을 클릭하면 방을 등록할 수 있다.

![127 0 0 1_8000_rooms_547_](https://user-images.githubusercontent.com/72296755/116500464-9bd1db00-a8e9-11eb-9a7d-f7312efd60ad.png)
-> 등록된 방을 확인할 수 있다.

7. 다이렉트 메시지
![image](https://user-images.githubusercontent.com/72296755/116500699-084cda00-a8ea-11eb-97bc-7a94b9797106.png)
![image](https://user-images.githubusercontent.com/72296755/116500711-113dab80-a8ea-11eb-8d4d-4aa707c63a3d.png)

8. 검색
![127 0 0 1_8000_rooms_search__csrfmiddlewaretoken=T8flk57HyWHz7ssWzhSdrXHUqgxrbDihOUgYNs7NaH5IdM0Z3Gnai3U0JFhX2sir city=Seoul country=KR room_type= price= guests= bedrooms= beds= baths=](https://user-images.githubusercontent.com/72296755/116500905-7c877d80-a8ea-11eb-926d-ffd4925de2e3.png)
-> 원하는 조건을 입력하면 바로 아래 Result에 결과가 뜬다.

9. 번역
![image](https://user-images.githubusercontent.com/72296755/116501048-d720d980-a8ea-11eb-97c5-89863bf42a5e.png)
->영어

![image](https://user-images.githubusercontent.com/72296755/116501002-bbb5ce80-a8ea-11eb-9b5d-0757ec49d4aa.png)
->한국어

![image](https://user-images.githubusercontent.com/72296755/116501028-ca03ea80-a8ea-11eb-9113-8859f8bafd7d.png)
->스페인어
