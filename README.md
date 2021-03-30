# 2021년 1학기 장기현장실습 (21.03.02 ~ 21.06.30)
## 기업: [💾셀로코㈜](https://selocoinc.wixsite.com/seloco)
### 참여: [🤗김기훈](https://github.com/daedu0813), [🤔최기환](https://github.com/kihwan1125/Resume)

## 오리엔테이션 (02.26)
### 전임 인턴 마지막 세미나 참여 및 인수인계
* 주차유도시스템 aParkings-ID(InDoor)
  - NVIDIA Jetson Nano 기반
  - Object Detection: YOLO(You Only Look Once)
  - 초음파 센서, 카메라 모듈, IoT 복합센서 이용
    - 자동차 인지 가능 (어두우면 인식률 낮음)
    - 전용 안드로이드 앱 개발 (진척도는 낮음, 통신은 TCP/IP)
* 사무실 출입 관제 시스템 aDoors
  - NVIDIA Jetson Nano 기반
  - Object Detection: Haar Cascades
  - 초음파 센서, 카메라 모듈 이용
     - Flask 웹 프레임 워크로 프론트엔드 설정 환경 개발
     - 수동으로 얼굴 저장 후 물체 감지 알고리즘으로 출입 시 카메라 모듈로 해당 사무실의 관계자 여부 확인

## 1주차 (03.03 ~ 03.05)
### 셀로코 개발 USN(Ubiquitous Sensor Network) MyUSN Station 기초 이해
* 03.04 1차 세미나 발표 - 제작/발표: 김기훈 *[PPT](https://github.com/daedu0813/Seloco_Intern/raw/main/documents/week01/USN%20%EC%8B%9C%EC%8A%A4%ED%85%9C%20%EA%B8%B0%EC%B4%88%EC%8B%A4%EC%8A%B5%20%EB%B0%9C%ED%91%9C%20-%20%EA%B9%80%EA%B8%B0%ED%9B%88.pptx) *[PPT(최기환 제작)](https://github.com/daedu0813/Seloco_Intern/raw/main/documents/week01/USN%EB%B0%9C%ED%91%9C(%EC%B5%9C%EA%B8%B0%ED%99%98%2C%202021.03.04).pptx)
  - 유비쿼터스 센서 네트워크, SENSOS 교육 및 개발 환경
  - 피드백
    - SENSOS 센서의 동작 원리, 실습 코드 분석

## 2주차 (03.08 ~ 03.12)
* 03.09 2차 세미나 발표 - 제작/발표: 최기환 *[PPT](https://github.com/daedu0813/Seloco_Intern/raw/main/documents/week02/5~10%EC%9E%A5%20%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C.%EA%B9%80%EA%B8%B0%ED%9B%88%2C%20%EC%B5%9C%EA%B8%B0%ED%99%98.pptx)
  - USN SENSOS 시스템 기초 실습
  - 피드백
    - SenTerm 실습, 18주간 계획짜기
    - 주차 유도 시스템, 주차 예약 시스템 개발 투입 예정 (시간 남으면 안드로이드 앱 개발) 
### Jetson Nano 개발 환경 기초 및 실습
* 03.10 Ubuntu OS 설치, 카메라 구동, 라이브러리 설치
* 03.11
  - 아두이노 이용 초음파 센서 구동 확인
  - Jetson Nano GPIO 공부
    - 초음파 센서 구동 실패
  - SenTerm 실습
    - 옵션 보드/센서를 제외한 모든 기능 확인
* 3차 세미나 - 제작: 최기환 / 발표: 김기훈 *[PPT](https://github.com/daedu0813/Seloco_Intern/raw/main/documents/week02/2%EC%A3%BC%EC%B0%A8%20Jetson%20Nano%2C%20Senterm%20%EC%8B%A4%EC%8A%B5%20%EB%B0%9C%ED%91%9C.pptx)
  - 피드백
    - 3주차까지 Jetson Nano + 초음파/도플러 센서 + 물체 감지 
* 03.12
  - Jetson Nano 이용 초음파 센서 (SR04) 구동 성공
### SELCAM (VB로 개발) ➡ Python 개발 환경 설정
  - UDP 소켓 통신
  - 여러개의 SenTerm 감지
  - OpenCV 등 오픈소스 이용 예정
  - YOLOv3 Object Detection 이용 예정

## 3주차 (03.15 ~ 03.19)
### Jetson Nano + 초음파/도플러 센서 + 물체 감지 (SenTerm 연결)
* 03.15
  - Jetson Nano + 도플러 센서(HW-M10) 구동 성공
  - HC-SR04 초음파 센서 파이썬 코드로 재 코딩 중
    - 초음파 센서와 도플러 센서를 같이 사용하기 위해
  - SELCAM➡Python 이식 진행 중
    - 소켓통신 이해와 VB코드의 이해가 중요
* 03.16 ~ 03.18
  - 차량계수 시스템 원리 파악
  - 원격 수질 측정시스템 DW-Q200 구성 블럭도 제작
* 03.19
  - ATmega8 기초지식 공부
  - 실습 키트와 책 구매
  
## 4주차(03.22~03.26)
### ATmega8 + 차량계수 시스템 업무 시작
* 03.22
  - ATmega8 기초지식 공부
* 03.23
  - LM, SIC, LED 모듈에 AtmelStudio 6.2 버전을 이용해 elf파일 집어넣기
* 03.24
  - 차량계수 시스템 SBC 파트 기초 파악
  - LED, Switch, 7-Segment 예제를 통한 AtmelStudio 코드 및 ATmega8 모듈 회로 이해
* 03.25
  - 차량계수 시스템 세부내용 관련 미팅
  - CM, LM을 이용한 SIC, LED 제어 블럭도 제작
* 03.26
  - 차량계수 시스템 세부내용 관련 미팅
  - 블럭도 제작 발표
## 5주차(03.29~04.02)
 * 03.29
  - 차량계수 시스템 세부내용 관련 미팅
  - 차량계수 시스템 세부내용 발표자료 제작
  - 기존 차량계수 시스템 코드 공부
 * 03.30
  - 기존 차량계수 시스템 코드 공부
  - 차량계수 시스템 진행상황 미팅 발표
  - 
  
