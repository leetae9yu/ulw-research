---
title: Pleos SDK 제공 정보 범위 조사
subtitle: 현대차그룹 차량용 앱 공모전
summary: Pleos Connect SDK가 공모전에서 제공하는 차량·내비·음성 데이터 범위와 졸음운전, 뒷좌석 아이, 동승자 엔터테인먼트 관련 현실 문제를 공개 자료로 정리했습니다.
created: 2026-10-23
updated: 2026-10-23
aliases: 2026-10-23-pleos-sdk
---
# 현대차그룹 차량용 앱 공모전: Pleos SDK 제공 정보 범위와 관련 현실 문제 조사

조사 기준일: 2026년 10월 23일. 공개 자료만 사용했습니다.

## 0. 요약

- 공모전 SDK는 Vehicle, NaviHelper, TextToSpeech, SpeechToText, FusedLocation 다섯 개입니다. 이 가운데 지금 신청 없이 바로 쓸 수 있는 것은 Vehicle State(차량 상태 조회)와 NaviHelper뿐입니다. TextToSpeech, SpeechToText, FusedLocation, Vehicle Control(차량 제어)은 "준비 중(Coming Soon)" 상태입니다(2.1절).
- 공개 ADAS·차량 데이터로 졸음이나 부주의를 직접 알 수 없습니다. 운전자 주의 경고(DRIVER_ATTENTION), 차선 유지(LKA), 전방 충돌(FCA) 같은 경고등 정보와 AAOS의 운전자 졸음·주의 분산·차선 이탈 상태는 모두 signature|privileged 권한이라 서드파티 앱이 받을 수 없습니다. 실내 카메라와 생체 신호 API도 없습니다(2.3절, 2.7절, 2.8절).
- 좌석별 탑승 여부(getCurrentSeatOccupancy), 좌석별 안전벨트, 도어·창문, 실내 온도, EV 배터리 잔량, 현재 주행 시간은 일반 권한으로 읽을 수 있고 에뮬레이터 Virtual Console에서 재현됩니다(2.3절).
- 차량 속도는 AAOS 표준 프로퍼티 PERF_VEHICLE_SPEED로 읽습니다. Vehicle SDK의 속도 리스너는 v2.3.2에서 삭제되었습니다. 기어는 AAOS GEAR_SELECTION으로 읽을 수 있고, Vehicle SDK 기어 API는 예제 코드에만 나와 제공 여부를 확인 못 했습니다(2.3절, 2.7절).
- NaviHelper는 위치, 목적지, 남은 거리·시간, 도착 시 예상 배터리, 충전 계획, 주의 구간, 제한 속도(1초 주기)를 주고 경로·경유지를 설정할 수 있지만, 휴게소·졸음쉼터 검색 API는 없습니다(2.4절).
- 주행 중에는 동영상·게임·브라우저 앱을 쓸 수 없고, 앱은 CarUxRestrictions에 맞춰 기능을 줄여야 합니다(2.9절).
- 현실 문제: 고속도로 사망자의 약 70%가 졸음·주시태만으로 집계되었고, 졸음운전 치사율은 전체 사고의 약 2배입니다(3.1절). 충전 앱의 "사용 가능" 표시가 실제와 다른 경험은 20.6%였습니다(3.3절). 뒷좌석 아이와의 상호작용은 휴대전화 상호작용의 12배 빈도로 관찰되었습니다(3.6절).
- 후보 판정(4장, 5장)은 세 후보 모두 "부분"입니다. 이 보고서는 아이디어를 고르지 않습니다.
  - 졸음운전 대응: 졸음 감지는 불가능합니다. 시간 기반 피로 위험 추정과 휴게소 경유지 안내는 가능합니다.
  - 뒷좌석 아이 케어: 주행 중 착좌·안전벨트·도어·온도 모니터링은 가능합니다. 영상·소리 확인과 하차 후 감지는 불가능합니다.
  - 동승자 엔터테인먼트: 주행 중 화면 콘텐츠는 불가능합니다. 위치·경로 기반 음성 콘텐츠는 음성 SDK가 준비 중입니다.

## 1. 조사 범위와 방법

- 조사 기준일은 2026년 10월 23일입니다. 공개 자료만 사용했고 Pleos Playground에 가입하거나 로그인하지 않았으며, 공모전 운영처나 어떤 사람에게도 문의하지 않았습니다.
- SDK 범위는 Pleos Playground 개발 문서(https://document.pleos.ai/docs/pleos-only/getting-started)와 공모전 개발 환경 안내(https://appdevchallenge.auto-hmg.io/guide/development)를 1차 자료로 삼았습니다. 문서 사이트의 개발자 가이드 412쪽을 내려받았고, 스크립트로 그려지는 API Reference는 문서 사이트가 배포하는 번들에서 1,866개 API 페이지 원문을 추출했습니다. 보고서에 적은 Pleos SDK와 AAOS의 API·상수 이름은 추출 원문과 자동 대조해 모두 원문에 있음을 확인했습니다. Android 표준 API인 CarPropertyManager.getPropertyList는 대조 대상에서 빠졌습니다.
- AAOS 표준 차량 프로퍼티의 권한은 Android 공식 레퍼런스(https://developer.android.com/reference/android/car/VehiclePropertyIds)를 2026년 10월 23일에 내려받은 본으로 확인했습니다. 로그인 상태나 접속 환경에 따라 이 주소가 Google 로그인 화면으로 이동할 수 있습니다.
- 현실 문제는 정부·공공기관 통계, 언론 보도, 연구 논문, 소비자 조사, 커뮤니티 글을 찾아 각 주장 옆에 출처를 붙였습니다. 열어 보지 못했거나 수치를 대조하지 못한 항목은 "확인 못 함"으로 적었습니다.
- 이 보고서는 아이디어를 고르지 않습니다. 근거와 판정만 정리합니다.
- 판정 기준: "가능"은 공모전에서 지금 쓸 수 있는 공개 API(사용 가능 상태 SDK 또는 normal·dangerous 권한의 AAOS 프로퍼티)로 필요한 데이터를 모두 얻는 경우입니다. "부분"은 일부 데이터만 얻거나 준비 중 SDK에 기대는 경우입니다. "불가"는 핵심 데이터가 signature|privileged 권한 뒤에 있거나 공개 API가 없는 경우입니다.

## 2. Pleos SDK별 제공 정보 범위

이 장의 API 이름은 Pleos Playground 공개 문서의 API Reference 표기를 그대로 옮겼습니다. API Reference 본문은 브라우저에서 스크립트로 그려지는 방식이어서, 공개 문서 사이트가 배포하는 문서 번들에서 1,866개 API 페이지 원문을 추출해 대조했습니다. 각 행의 URL은 사람이 열어 볼 수 있는 해당 API 페이지 주소입니다. 문서 기준 버전은 Vehicle SDK v2.3.2, NaviHelper v3.0.5, TextToSpeech v3.3.1, SpeechToText v3.3.1, FusedLocation SDK v1.1.3이며 릴리스일은 2026년 10월 19일입니다(https://document.pleos.ai/docs/pleos-only/release-note/sdk-261015).

### 2.1 SDK 목록과 공모전 사용 가능 상태

공모전이 안내하는 SDK는 Vehicle SDK, NaviHelper SDK, TextToSpeech SDK, SpeechToText SDK, FusedLocation SDK 다섯 개입니다(https://appdevchallenge.auto-hmg.io/faq, "어떤 SDK와 API를 쓸 수 있나요?"; https://appdevchallenge.auto-hmg.io/guide/development, "Pleos Connect SDK"). 공모전 FAQ는 "각 SDK의 현재 제공 상태와 사용 조건은 SDK 문서 페이지에서 확인"하라고 안내합니다. Playground 문서의 SDK 사용 신청 절차는 각 SDK의 상태를 다음과 같이 밝힙니다(https://document.pleos.ai/docs/pleos-only/create-my-project, "SDK 사용 신청").

| SDK | Playground 상태 | 의미 |
| --- | --- | --- |
| Vehicle State | 사용 가능(신청 없이 바로 사용) | 차량 상태 조회·구독 |
| NaviHelper SDK | 사용 가능(신청 없이 바로 사용) | 내장 내비게이션 연동 |
| Vehicle Control | 준비 중(Coming Soon, 신청 불가) | 차량 제어 |
| FusedLocation SDK | 준비 중(Coming Soon, 신청 불가) | 차량 위치 |
| TextToSpeech SDK | 준비 중(Coming Soon, 신청 불가) | 음성 합성 |
| SpeechToText SDK | 준비 중(Coming Soon, 신청 불가) | 음성 인식 |

Vehicle State와 Vehicle Control의 경계는 문서에 API 단위로 적혀 있지 않습니다. 퍼미션 체계가 조회용 CAR_* 와 제어용 CONTROL_CAR_* 로 나뉘어 있으므로(https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/Vehicle/vehicle-permission, "퍼미션 종류"), 이 보고서는 Vehicle State를 CAR_* 조회·구독 API로, Vehicle Control을 CONTROL_CAR_* 설정 API로 추정합니다. 이 대응은 추정이며 문서로 확인 못 함입니다.

에뮬레이터 개발은 신청 상태와 별개로 문서화되어 있습니다. TextToSpeech와 SpeechToText의 ON_DEVICE 모드는 앱 등록 없이 동작한다고 문서에 적혀 있습니다(https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/TextToSpeech/intro, "음성 합성 모드"; https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/SpeechToText/intro, "음성 인식 모드"). 준비 중 상태의 SDK가 에뮬레이터에서 실제로 호출되는지는 로그인과 실행이 필요해 확인 못 함입니다.

Pleos App Market 출시 단계에서는 App Market과 사전 협의해 승인받은 Vehicle SDK 퍼미션만 선언할 수 있습니다. 승인되지 않은 퍼미션을 선언한 앱은 심사를 통과할 수 없습니다(https://document.pleos.ai/docs/pleos-only/distribute/app-review-guide/review-functionality-performance-stability, "SDK·API 사용 심사"). 공모전 2차 PT는 에뮬레이터 구동 화면 시연을 인정합니다(https://appdevchallenge.auto-hmg.io/notice/c0a1a000-2026-4923-8000-000000000006, "2. 심사 및 시상·현장 시연 관련 유의사항").

### 2.2 공통 개발 환경

- 최소 Android API 28, Gradle 8.0 이상, Java 또는 Kotlin을 사용합니다. 에뮬레이터는 Pleos Connect Emulator 2.1.0이며 Android Studio SDK Manager에 업데이트 사이트를 추가해 Android API 34 시스템 이미지로 설치합니다(https://document.pleos.ai/docs/connect/guide/getting-started/application-development/setup-connect-sdk-emulator, "소프트웨어 개발 환경", "Emulator를 Android Studio에 추가하기").
- Pleos Connect Virtual Console은 에뮬레이터의 8088 포트를 포워딩한 뒤 PC 브라우저에서 차량 상태를 바꾸는 도구입니다(https://document.pleos.ai/docs/connect/guide/getting-started/application-development/use-vehicle-emulator, "Pleos Connect Virtual Console 실행 방법").
- Vehicle SDK 호출은 IPC이므로 capability·get·set 결과가 onComplete·onFailed 비동기 람다로 돌아옵니다. register* 함수는 리스너를 등록해 상태 변화를 구독합니다(https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/Vehicle/intro, "진입점과 도메인 구조").
- 갱신 주기: Vehicle SDK 문서는 Hz나 주기 값을 적지 않습니다. register* 리스너는 "property updates"를 받는다고만 적혀 있어, 고정 주기는 확인 못 함입니다. NaviHelper의 onCurrentRoadSpeedLimit만 "등록 후 매초 수신"으로 주기가 명시되어 있습니다(2.4절).
- 차량 모델마다 지원 API가 다르며 checkXXXCapabilities로 지원 여부를 확인해야 합니다(https://document.pleos.ai/docs/pleos-only/vehicle-app-planning-guide/api-compatibility-availability, "Pleos Connect SDK API 호환성").

### 2.3 Vehicle SDK

진입점은 Vehicle 클래스입니다. 이 클래스는 initialize(), release()와 다음 도메인 획득 함수 getBrake(), getCarInfo(), getDisplay(), getDoor(), getDrivingMode(), getEvBattery(), getFuel(), getHVAC(), getLight(), getOdometer(), getSafety(), getSeat(), getSideMirror(), getSteeringWheel(), getTire(), getToll(), getTurnSignal(), getWindow(), getWiper()를 제공합니다(https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/Vehicle/vehicle/ai.pleos.playground.vehicle/vehicle/entry). 아래 표의 보호 수준은 각 API 페이지의 "Permission: ... (protection level: ...)" 표기입니다. normal은 일반 앱이 선언만으로 받는 수준이고, signature|privileged는 플랫폼 서명이나 시스템 권한 앱만 받는 수준입니다.

| 도메인 | 주요 데이터(API 이름 그대로) | 읽기/쓰기 | 퍼미션(보호 수준) | Virtual Console 재현 | 출처 |
| --- | --- | --- | --- | --- | --- |
| Brake | getCurrentBrakePedalStatus(눌림 여부 Boolean), registerBrakePedalStatus | 읽기·구독 | CAR_DRIVE(normal) | Brake Pedal 0~100% | https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/Vehicle/vehicle/ai.pleos.playground.vehicle.api/brake/entry |
| CarInfo | getVINInfo(VIN 문자열), getCRNInfo(deprecated) | 읽기 | CAR_INFO(normal) | 없음 | https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/Vehicle/vehicle/ai.pleos.playground.vehicle.api/car-info/entry |
| Display | getCurrentTemperatureDisplayUnit, registerTemperatureDisplayUnit | 읽기·구독 | CAR_INFO(normal) | 없음 | https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/Vehicle/vehicle/ai.pleos.playground.vehicle.api/display/entry |
| Door | getCurrentDoorPosition, getDoorLockState, getCurrentGloveBoxLockState, register*; setDoorLock, setDoorPosition, setGloveBoxLock | 읽기·구독, 쓰기 | CAR_DOORS(normal), 쓰기 CONTROL_CAR_DOORS(normal) | Door Position, Door Lock, Trunk/Frunk, Glove Box | https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/Vehicle/vehicle/ai.pleos.playground.vehicle.api/door/entry |
| DrivingMode | getCurrentDrivingModeState(DrivingModeType), getCruiseControlState(CruiseControl), getCruiseControlTargetSpeed, register* | 읽기·구독 | CAR_DRIVE(normal) | Cruise Control State, Cruise Target Speed | https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/Vehicle/vehicle/ai.pleos.playground.vehicle.api/driving-mode/entry |
| EvBattery | getEvBatteryStateOfCharge(%), getCurrentEvEfficiency, getInstantaneousEvEfficiency, getCumulativeEvEfficiency, getSinceChargeEvEfficiency(km/kWh), getEvChargeSwitchState, getEvChargeCurrentDrawLimit, register*; setEvChargePercentLimit, setEvChargeCurrentDrawLimit, setEvChargePortOpen, setEvChargeSwitch | 읽기·구독, 쓰기 | CAR_ENERGY(normal), 쓰기 CONTROL_CAR_ENERGY(normal) | Battery SOC, Battery Energy, Capacity, Charge Limit, Charge Switch, Charge Port, Remaining Range | https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/Vehicle/vehicle/ai.pleos.playground.vehicle.api/ev-battery/entry |
| Fuel | getFuelPercent(%), getCurrentFuelEconomy, getInstantaneousFuelEconomy, getCumulativeFuelEconomy, getSinceChargeFuelEconomy(L/100km), register* | 읽기·구독 | CAR_ENERGY(normal) | 없음 | https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/Vehicle/vehicle/ai.pleos.playground.vehicle.api/fuel/entry |
| HVAC | getHvacTemperature, getHvacTemperatureCurrent(실내 온도 °C), getHvacPowerState, getHvacFanSpeed, getHvacFanDirection, getHvacAcState, getHvacAutoState, getHvacRecirculationState, getHvacDefrosterState, getHvacAirCleanerState 등, register*; setHvacTemperature, setHvacFanSpeed, setHvacAc, setHvacRecirculation, setHvacAirCleaner 등 13종 | 읽기·구독, 쓰기 | CAR_CLIMATE(normal), 쓰기 CONTROL_CAR_CLIMATE(normal) | Climate 도메인 11개 카드 | https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/Vehicle/vehicle/ai.pleos.playground.vehicle.api/h-v-a-c/entry |
| Light | 앰비언트(getAmbientLightBrightness, getAmbientLightBrightnessColor 등), 실내등·독서등·전조등·안개등·미등 상태와 스위치, register*; setAmbientLightBrightnessColor(32비트 ARGB), setReadingLightSwitch, setCabinLightSwitch 등 | 읽기·구독, 쓰기 | CAR_LIGHTS(normal), 쓰기 CONTROL_CAR_LIGHTS(normal) | Ambient, Cabin, Reading, Exterior, High Beam, Hazard, Stop | https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/Vehicle/vehicle/ai.pleos.playground.vehicle.api/light/entry |
| Odometer | getCurrentDistanceDriven, getTripCurrentDrivingTime(현재 주행 세션 분), getTripCurrentDrivingDistance, getTripCumulativeDrivingTime, getTripSinceRefillDrivingTime 등, register* | 읽기·구독 | CAR_DRIVE(normal) | Odometer | https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/Vehicle/vehicle/ai.pleos.playground.vehicle.api/odometer/entry |
| Safety | hasSeatBeltNotBuckledWarning, hasSeatAirbagEnabled, hasSeatAirbagBeenDeployed, getEngineOilLevelState, getBrakeFluidLevelState, getTransmissionOilLevelState, hasLowWasherFluidWarning, hasPowerDownWarningIndicator, register* | 읽기·구독 | CAR_SAFETY(normal) | 일부(Telltales 카드) | https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/Vehicle/vehicle/ai.pleos.playground.vehicle.api/safety/entry |
| Safety(경고등) | getTelltalesInfo, registerTelltales, checkTelltalesCapabilities | 읽기·구독 | PRIVATE_CAR_SAFETY(signature|privileged) | Telltales | https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/Vehicle/vehicle/ai.pleos.playground.vehicle.api/safety/get-telltales-info |
| Seat | getCurrentSeatOccupancy(좌석별 탑승 Boolean), registerSeatOccupancy, getCurrentSeatBeltBuckledState, registerSeatBeltBuckledState, 좌석 위치·각도(getCurrentSeatForeAftPosition 등), getHvacSeatTemperature, getHvacSeatVentilationState; moveSeat*(11종), selectSeatMemory, setHvacSeatTemperature, setHvacSeatVentilation | 읽기·구독, 쓰기 | CAR_SEATS(normal), 쓰기 CONTROL_CAR_SEATS(normal) | Seat Occupancy(운전석·동승석·뒷좌석 좌우), Seat Temperature | https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/Vehicle/vehicle/ai.pleos.playground.vehicle.api/seat/entry |
| SideMirror | getHvacSideMirrorHeatState, setHvacSideMirrorHeat | 읽기, 쓰기 | CAR_MIRRORS(normal), CONTROL_CAR_MIRRORS(normal) | 없음 | https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/Vehicle/vehicle/ai.pleos.playground.vehicle.api/side-mirror/entry |
| SteeringWheel | getCurrentSteeringWheelAngle(앞바퀴 조향각, 도), registerSteeringWheelAngle, getHvacSteeringWheelHeatState, setHvacSteeringWheelHeat | 읽기·구독, 쓰기 | CAR_DRIVE(normal), 열선 CAR_CLIMATE/CONTROL_CAR_CLIMATE(normal) | Steering Angle -540~540도, Steering Wheel Heat | https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/Vehicle/vehicle/ai.pleos.playground.vehicle.api/steering-wheel/entry |
| Tire | getLowTirePressure(저압 경고 임계값 kPa) | 읽기 | CAR_SAFETY(normal) | 없음 | https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/Vehicle/vehicle/ai.pleos.playground.vehicle.api/tire/entry |
| Toll | getCurrentEtcsVoiceGuidanceVolume, setEtcsVoiceGuidanceVolume | 읽기·구독, 쓰기 | CAR_TOLL(normal), CONTROL_CAR_TOLL(normal) | ETCS Power, ETCS Scenario | https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/Vehicle/vehicle/ai.pleos.playground.vehicle.api/toll/entry |
| TurnSignal | getCurrentTurnSignalState, registerTurnSignalState | 읽기·구독 | CAR_LIGHTS(normal) | Turn Signal State | https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/Vehicle/vehicle/ai.pleos.playground.vehicle.api/turn-signal/entry |
| Window | getCurrentWindowPosition, getCurrentWindowLockState, getCurrentWindowBlindPosition, getCurrentSmartGlassLevel, register*; setWindowPosition, setWindowLock, moveWindowBlind, setSmartGlassLevel | 읽기·구독, 쓰기 | CAR_WINDOWS(normal), CONTROL_CAR_WINDOWS(normal), setSmartGlassState만 signature|privileged | Window Position, Window Lock | https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/Vehicle/vehicle/ai.pleos.playground.vehicle.api/window/entry |
| Wiper | getCurrentWiperState, getCurrentWiperSwitch, registerWiperState, setWiperSwitch | 읽기·구독, 쓰기 | CAR_WINDOWS(normal), CONTROL_CAR_WINDOWS(normal) | Windshield Wiper Switch | https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/Vehicle/vehicle/ai.pleos.playground.vehicle.api/wiper/entry |

Virtual Console 열은 Virtual Console 사용 가이드의 카드 목록 기준입니다(https://document.pleos.ai/docs/pleos-only/app-test-guide/virtual-console-guide, "Emulation Controls 사용 방법"). 기어(P, R, N, D)는 Virtual Console에서 바꿀 수 있습니다. Vehicle 클래스 설명의 예제 코드에는 vehicle.getGear(), registerGearSelection, GearSelectionListener가 나오지만, 같은 페이지의 함수 목록과 API Reference의 도메인 페이지에는 Gear가 없습니다(https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/Vehicle/vehicle/ai.pleos.playground.vehicle/vehicle/entry). Vehicle SDK의 기어 API 제공 여부는 확인 못 함이며, 문서가 확실히 안내하는 경로는 AAOS 표준 프로퍼티 GEAR_SELECTION입니다(2.7절).

조향각 주의점: getCurrentSteeringWheelAngle의 값은 "front-wheel steering angle"입니다. 문서는 이 값이 "does not represent the rotation angle of the steering wheel"이라고 명시합니다(https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/Vehicle/vehicle/ai.pleos.playground.vehicle.api/steering-wheel/get-current-steering-wheel-angle). Virtual Console 카드는 같은 값을 "스티어링 휠 각도 -540~540도"로 설명해 표현이 다릅니다.

경고등(Telltale) 상세: TelltaleType은 경고등 종류를 나열한 열거형입니다. 여기에는 DRIVER_ATTENTION, FCA, LKA, LFA, LCA_LEFT, LCA_RIGHT, ICC, OVER_SPEED, SEAT_BELT, DOOR_OPEN, TPMS, CHILD_PRESENCE_DETECTION_OFF, LOW_EV_BATTERY, LOW_FUEL, ENGINE, MASTER_WARNING 등이 있고, TelltaleData는 type, state(OFF, ON, BLINK), color, priority, warningCount를 담습니다(https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/Vehicle/vehicle/ai.pleos.playground.vehicle.constant.telltale/telltale-type/entry 및 https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/Vehicle/vehicle/ai.pleos.playground.vehicle.api.model.telltale/telltale-data/entry). 그러나 이 데이터를 받는 getTelltalesInfo, registerTelltales는 PRIVATE_CAR_SAFETY(signature|privileged)를 요구합니다. getTelltalesInfo 페이지는 어노테이션에 CAR_SAFETY, 설명에 PRIVATE_CAR_SAFETY(signature|privileged)를 함께 적어 표기가 서로 다릅니다. registerTelltales와 checkTelltalesCapabilities는 어노테이션과 설명 모두 PRIVATE_CAR_SAFETY입니다. 따라서 운전자 주의 경고(DAW) 점등 여부는 열거형에는 있지만 서드파티 앱이 받을 수 없는 것으로 판단합니다.

삭제된 API: Vehicle SDK v2.3.2에서 VehicleSpeedListener와 onSpeedUpdated가 삭제되었습니다(https://document.pleos.ai/docs/pleos-only/release-note/sdk-261015, "Shutdown API").

### 2.4 NaviHelper SDK

NaviHelper는 Pleos Connect 내장 내비게이션과 연동하는 SDK입니다. 진입점은 NaviHelper(context)이며 initialize(), initialize(onConnected, onFailed), addListener(), removeListener(), release()를 제공합니다(https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/NaviHelper/navi-helper/ai.pleos.playground.navi.helper/navi-helper/entry). 내비게이션이 탑재된 차량에서만 전체 호환됩니다(https://document.pleos.ai/docs/pleos-only/vehicle-app-planning-guide/api-compatibility-availability). 공모전 상태는 "사용 가능"입니다(2.1절).

| 구분 | API 이름 그대로 | 퍼미션 | 출처 |
| --- | --- | --- | --- |
| 조회(결과는 리스너로 수신) | getCurrentLocationInfo, getDestinationInfo, getWaypointInfo, getRouteStateInfo, getTBTInfo, getBookmarkInfo, getRecentDestinationInfo, getChargerOperatorInfo, requestTrip | pleos.car.permission.NAVI_ROUTE | https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/NaviHelper/declaring-permissions |
| 경로 제어(쓰기) | requestRoute, requestRouteWithWaypoints, cancelRoute, requestReRoute, addWaypoint, removeWaypoint, changeRouteOption | pleos.car.permission.NAVI_ROUTE_SEARCH | 같은 페이지 |
| 화면 전환 | requestNavigationScreen(Foreground, FavoriteMain, AddHomeFavorite, AddWorkFavorite, NearbyChargingStations, Settings, MoveToCurrentLocationOnMap, OverviewRoute, SearchPlace, POIDetailPopup, RecentDestinations, RouteOptionList, EditRoute) | pleos.car.permission.NAVI_CUSTOM_MAP | https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/NaviHelper/navi-helper/ai.pleos.playground.navi.data/navigation-screen-request/entry |

NaviHelperEventListener는 다음 이벤트를 제공합니다. onCurrentLocationInfo, onCurrentRoadSpeedLimit(등록 후 매초 수신), onCameraAlert, onCautionPointInfo, onTBTInfo, onDrivingInfo, onTripInfo, onRouteStateInfo, onNavigationStatus, onRouteStarted, onRoutingCompleted, onReRouteEnded, onRouteCancelled, onRouteOptionChanged, onDestinationInfo, onDestinationChanged, onDestinationArrived, onWayPointInfo, onWaypointChanged, onWayPointArrived, onBookmarkInfo, onBookMarkChanged, onRecentDestinationInfo, onChargerOperatorInfo, onError(https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/NaviHelper/navi-helper/ai.pleos.playground.navi.helper.listener/navi-helper-event-listener/entry).

주요 데이터 필드는 다음과 같습니다(https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/NaviHelper/navi-helper/ai.pleos.playground.navi.data/entry).

- CurrentLocationInfo: latitude, longitude, heading, address, routeId, currentRouteIndex
- DestinationInfo: name, address, remainDistance, remainTime, tollFare, poiId
- TripInfo: distance(m), eta(초), estimatedSocAtDest(도착 시 예상 배터리 %), energyConsumption(Wh), summary(TripSummary: trafficConditions, routePoints)
- DrivingState: duration, distance, remainDestinationChargingValue, isChargingStation, isRecommendedChargingStation, maxChargingPower, targetSoc, chargerCount, chargingPlan(duration, startSoc, endSoc)
- CameraAlert: type, speedLimit, remainDistance, sectionAvrSpeed, isOverSpeed, isOverSectionAvrSpeed
- CautionPoint: type(SPEED_BUMP, SCHOOL_ZONE, ACCIDENT_PRONE_AREA, FOG_AREA, FALLING_ROCK_AREA, DOWNHILL_CAUTION_AREA, WILDLIFE_CROSSING 등), remainDistance
- RouteStateInfo.trafficStatus: TrafficCongestionSummary(totalCongestionDist, totalCongestionTime, totalCongestionAvrSpeed), TrafficCongestionInfo(avrSpeed, roadName 등), TrafficEventInfo(eventType: ACCIDENT, ROAD_DAMAGE, REPAIRING, EVENT, DISASTER)
- NavigationStatus: INACTIVE, INITIALIZING, FREE_DRIVE, ROUTE_DRIVE

NaviHelper에서 찾지 못한 것: 공개 API 목록에서 휴게소·졸음쉼터·주차장 같은 장소 유형 검색 API를 찾지 못했습니다. 경로 지점의 POI 유형은 NORMAL과 EV_CHARGING 두 가지뿐이고(https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/NaviHelper/navi-helper/ai.pleos.playground.navi.constants/route-point-poi-type/entry), requestRoute는 앱이 위도·경도·poiId를 직접 넘기는 방식입니다. 따라서 휴게소 안내를 하려면 앱이 휴게소 좌표를 별도 공개 데이터에서 가져와 경유지로 넣어야 합니다. 갱신 주기는 onCurrentRoadSpeedLimit의 1초만 명시되어 있고 나머지 이벤트 주기는 확인 못 함입니다.

### 2.5 TextToSpeech SDK와 SpeechToText SDK

| 항목 | TextToSpeech | SpeechToText |
| --- | --- | --- |
| 진입점·주요 API | ai.pleos.playground.tts.TextToSpeech; initialize, addEventListener, setLocale, setSpeakerType, setAudioZoneId, setAudioAttributes, registerApp, speak, stop, release | ai.pleos.playground.stt.SpeechToText; initialize, addListener, setLocale, registerApp, request, sendAudio, completeAudioSend, stop, release |
| 모드 | HYBRID(기본), SERVER, ON_DEVICE | HYBRID(기본), SERVER, ON_DEVICE |
| 퍼미션 | pleos.car.permission.TTS_SERVICE(https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/TextToSpeech/declaring-permissions) | pleos.car.permission.STT_SERVICE(https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/SpeechToText/declaring-permissions) |
| 서버 모드 조건 | Playground 프로젝트의 클라이언트 ID·시크릿으로 앱 등록 필요 | 같음 |
| 특징 | 화자 seoyoon, eunwoo, haeun, sanghyeok(한국어) 선택, 오디오 존 지정 | 결과는 텍스트만 반환하고 명령을 실행하지 않음. sendAudio는 앱이 가진 PCM을 ON_DEVICE 모드에서만 인식 |
| 공모전 상태 | 준비 중 | 준비 중 |
| 출처 | https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/TextToSpeech/intro, https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/TextToSpeech/text-to-speech/ai.pleos.playground.tts/text-to-speech/set-speaker-type | https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/SpeechToText/intro, https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/SpeechToText/sending-audio-data |

문서상 음성은 주행 중에도 허용되는 입력 방식입니다. 북미 정책은 주행 중 검색을 음성으로만 허용합니다(https://document.pleos.ai/docs/pleos-only/vehicle-app-planning-guide/driving-restiction-policy). 주의 분산 설계 원칙은 음성 입력과 프리셋을 우선하라고 안내합니다(https://document.pleos.ai/docs/pleos-only/vehicle-app-planning-guide/driver-distraction-guideline). 다만 두 SDK 모두 공모전 상태가 준비 중이라는 점이 제약입니다.

### 2.6 FusedLocation SDK

FusedLocation은 isSupported, initialize, getLastKnownLocation, registerFusedLocationCallback, unregisterFusedLocationCallback, showLocationAccessBlockedPopup, addProximityAlert, removeProximityAlert를 제공합니다. LocationData는 위도, 경도, 고도, 진행 방향, 신뢰도, 타임스탬프를 담습니다. 퍼미션은 pleos.car.permission.FUSED_LOCATION이며 차량 모델에 따라 지원 여부가 다릅니다(https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/FusedLocation/intro, "제공 기능", "위치 데이터", "권한 및 접근 제약"). 공모전 상태는 준비 중입니다. 위치가 필요하면 사용 가능 상태인 NaviHelper의 getCurrentLocationInfo, onCurrentLocationInfo로 대체할 수 있습니다(2.4절).

### 2.7 Gleo Interface와 AAOS 표준 Car API

Gleo Interface는 Gleo AI가 서드파티 앱을 음성 명령으로 호출하는 연동 규격이며, 별도 SDK는 아닙니다. 앱이 App Schema(JSON)에 function을 정의하면 LLM이 function call을 만듭니다. Gleo AI는 Gleo Action으로 앱을 호출하고 Callback으로 응답을 받습니다(https://document.pleos.ai/docs/pleos-only/app-integration-guide/guide/core-concepts). App Schema의 actionCalls는 최대 3개이고 호출 방식은 activity(startActivity) 또는 service(sendBroadcast)입니다(https://document.pleos.ai/docs/pleos-only/app-integration-guide/guide/app-capability, "2.1 Fields"). 즉 Gleo AI는 사용자가 말을 걸었을 때 앱을 부르는 구조이며, 앱이 Gleo AI에게 대화를 먼저 시작하게 하는 API는 문서에서 찾지 못했습니다. 공모전 FAQ와 개발 안내의 SDK 목록에는 Gleo Interface가 없습니다(https://appdevchallenge.auto-hmg.io/faq). App Schema 등록 절차와 공모전 사용 가능 여부는 확인 못 함입니다.

Pleos는 AAOS 표준 API에 같은 기능이 있으면 SDK에서 중복 제공하지 않고 표준 API 사용을 권장합니다. 문서는 속도, 기어 상태, 외기 온도, 연료 레벨을 AAOS Car API 대상 예시로 듭니다(https://document.pleos.ai/docs/pleos-only/vehicle-app-planning-guide/pleos-connect-sdk-api, "API 선택 기준"). 클러스터와 같은 속도는 CarPropertyManager로 PERF_VEHICLE_SPEED를 읽으라고 안내합니다(https://document.pleos.ai/docs/pleos-only/vehicle-app-developer-guide/vehicle-app-faq, "클러스터 속도 조회 방법").

| AAOS 프로퍼티 | 내용 | 필요 권한(보호 수준) | 서드파티 사용 |
| --- | --- | --- | --- |
| PERF_VEHICLE_SPEED | 차량 속도 m/s, CONTINUOUS | Car.PERMISSION_SPEED(dangerous) | 가능(런타임 권한) |
| GEAR_SELECTION | 선택 기어 | Car.PERMISSION_POWERTRAIN(normal) | 가능 |
| ENV_OUTSIDE_TEMPERATURE, NIGHT_MODE | 외기 온도, 야간 모드 | normal | 가능 |
| SEAT_OCCUPANCY | 좌석 점유 | Car.PERMISSION_READ_CAR_SEATS(dangerous) | 가능 |
| DRIVER_DROWSINESS_ATTENTION_STATE, DRIVER_DROWSINESS_ATTENTION_WARNING | KSS 기반 졸음·주의 상태와 경고 | Car.PERMISSION_READ_DRIVER_MONITORING_STATES(signature|privileged) | 불가 |
| DRIVER_DISTRACTION_STATE, DRIVER_DISTRACTION_WARNING | 주의 분산 상태와 경고 | 같음(signature|privileged) | 불가 |
| HANDS_ON_DETECTION_DRIVER_STATE | 핸들 파지 여부 | 같음(signature|privileged) | 불가 |
| LANE_DEPARTURE_WARNING_STATE, FORWARD_COLLISION_WARNING_STATE, BLIND_SPOT_WARNING_STATE | 차선 이탈·전방 충돌·후측방 경고 상태 | Car.PERMISSION_READ_ADAS_STATES(signature|privileged) | 불가 |

표의 출처는 https://developer.android.com/reference/android/car/VehiclePropertyIds 의 각 상수 항목입니다. 표준 정의가 있어도 차량이 해당 프로퍼티를 실제로 제공하는지는 모델마다 다르며 CarPropertyManager로 확인해야 합니다(https://document.pleos.ai/docs/pleos-only/vehicle-app-planning-guide/api-compatibility-availability, "AAOS Vehicle Property 가용성"). Pleos Connect 실차가 PERF_VEHICLE_SPEED 외의 프로퍼티를 어디까지 제공하는지는 확인 못 함입니다. Virtual Console 셋업 가이드는 "차량 속도" 변경을 할 수 있다고 소개하지만 사용 가이드의 카드 목록에는 속도 카드가 없어, 에뮬레이터에서 속도를 바꾸는 방법은 확인 못 함입니다(https://document.pleos.ai/docs/connect/guide/getting-started/application-development/use-vehicle-emulator 및 https://document.pleos.ai/docs/pleos-only/app-test-guide/virtual-console-guide).

### 2.8 공개 API로 얻을 수 없는 정보

| 정보 | 판정 | 근거 |
| --- | --- | --- |
| 실내 카메라 영상, 운전자 모니터링(DMS) 데이터 | 공개 문서에서 찾지 못함 | Vehicle SDK 19개 도메인과 다섯 SDK 어디에도 카메라·DMS API가 없습니다(https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/Vehicle/intro). AAOS의 운전자 상태 프로퍼티는 signature|privileged입니다(2.7절). 표준 Android 카메라 API로 실내 카메라에 접근할 수 있는지는 확인 못 함입니다. |
| 졸음·주의 분산 판정값, DAW 경고 | 서드파티 불가 | TelltaleType.DRIVER_ATTENTION은 PRIVATE_CAR_SAFETY(signature|privileged), DRIVER_DROWSINESS_ATTENTION_STATE는 READ_DRIVER_MONITORING_STATES(signature|privileged) |
| 차선 이탈·전방 충돌·후측방 경고(ADAS 경고) | 서드파티 불가 | LKA, FCA, LCA 경고등은 PRIVATE_CAR_SAFETY, AAOS ADAS 상태는 READ_ADAS_STATES(signature|privileged) |
| 크루즈 컨트롤 상태 | 가능 | getCruiseControlState(CAR_DRIVE, normal). 상태 값은 OTHER, ENABLED, ACTIVATED, USER_OVERRIDE, SUSPENDED, FORCED_DEACTIVATION_WARNING(https://document.pleos.ai/docs/pleos-only/release-note/sdk-261015) |
| 생체 신호(심박, 체온 등) | 공개 문서에서 찾지 못함 | 다섯 SDK의 공개 API 목록에서 생체 신호 API를 찾지 못했습니다(SDK 개요 https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/) |
| 좌석 점유(사람이 앉았는지) | 가능 | getCurrentSeatOccupancy, registerSeatOccupancy(CAR_SEATS, normal), 1~3열 좌우·가운데 SeatValue. 실차 센서가 어느 좌석에 있는지는 checkSeatOccupancyCapabilities로만 알 수 있어 차종별 범위는 확인 못 함 |
| 뒷좌석 아이 감지(Child Presence Detection) | 결과값 API를 찾지 못함 | TelltaleType에 CHILD_PRESENCE_DETECTION_OFF(기능 꺼짐 표시)만 있고 PRIVATE_CAR_SAFETY입니다. 감지 결과를 주는 API는 공개 문서에서 찾지 못했습니다. |
| 안전벨트 착용 | 가능 | getCurrentSeatBeltBuckledState(CAR_SEATS), hasSeatBeltNotBuckledWarning(CAR_SAFETY) |
| 차량 속도, 기어 | AAOS로 가능 | PERF_VEHICLE_SPEED(dangerous), GEAR_SELECTION(normal). Vehicle SDK 속도 리스너는 삭제됨. Vehicle SDK 기어 API는 예제 코드에만 나오며 제공 여부 확인 못 함 |
| 마이크 원음 녹음 | 확인 못 함 | STT는 텍스트만 반환합니다. 일반 Android AudioRecord 사용 가능 여부는 문서에 없습니다. |
| 휴게소·졸음쉼터 검색 | NaviHelper 공개 API에서 찾지 못함 | POI 유형은 NORMAL, EV_CHARGING뿐(2.4절) |
| 알림, 계정, 결제 SDK | 공모전 SDK 목록에서 찾지 못함 | SDK 개요의 모듈 목록은 다섯 SDK뿐입니다(https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/). 결제(Universal Wallet) 등은 Playground 제품 소개 페이지 제목으로만 존재하며 공모전 SDK가 아닙니다. 상세는 확인 못 함 |

### 2.9 주행 중 제한

- 앱이 Distraction Optimization(DO)을 선언하지 않으면 주차 중에만 쓸 수 있고 주행 중에는 쓸 수 없습니다(https://document.pleos.ai/docs/pleos-only/vehicle-app-planning-guide/driving-restiction-policy, "주행 상황에 따른 앱 사용 여부").
- 주행 규제 상태에서 키보드, 다이얼패드, 설정, 동영상, 대용량 텍스트가 제한됩니다. 문서는 북미, 유럽, "그외 지역" 세 표만 제공하며 한국을 따로 명시하지 않습니다. 한국이 "그외 지역"에 속한다는 것은 추정입니다. "그외 지역"은 주행 중 키보드·다이얼패드·검색·미디어 앱 로그인과 내비게이션 검색을 허용하고, 차량 설정, 동영상, QR 로그인, 대용량 텍스트를 막습니다. 북미는 검색을 음성으로만 허용합니다(같은 페이지, "주행 상황별 기능 제한"). 지역 코드는 product.sw.target_region 값 KOR로 구분합니다(https://document.pleos.ai/docs/pleos-only/vehicle-app-developer-guide/vehicle-app-faq, "지역 코드 확인").
- 앱은 AAOS CarUxRestrictionsManager의 onUxRestrictionsChanged로 제한 상태를 받아 반영해야 합니다(https://document.pleos.ai/docs/pleos-only/vehicle-app-developer-guide/driving-restriction-development-guide). 에뮬레이터에서는 adb shell cmd hmg_car_service --service drivingstate driving 으로 주행 규제를 켤 수 있습니다(https://document.pleos.ai/docs/pleos-only/vehicle-app-developer-guide/adb-command-reference-guide, "주행 규제 활성화/해제").
- 동영상, 게임, 브라우저 기능을 가진 미디어 앱은 운전 중 실행·사용할 수 없고, 운전이 시작되면 일시 중지하고 UI를 숨겨야 합니다(https://document.pleos.ai/docs/pleos-only/distribute/app-review-guide/review-driver-distraction-elements, "미디어 앱 설계").
- 앱 카테고리 중 Music/Audio, Maps/Navigation, Mobility Services는 주행 중 일부 기능이 제한적으로 허용될 수 있고, Kids 카테고리도 따로 있습니다(https://document.pleos.ai/docs/pleos-only/vehicle-app-planning-guide/app-category).
- 동승석 전용 화면이나 뒷좌석 화면을 위한 별도 규제나 API는 공개 문서에서 찾지 못했습니다(확인 못 함). Pleos Connect 플랫폼은 Connect-S, Connect-L, Connect-W 세 가지로 구분됩니다(https://document.pleos.ai/docs/pleos-only/vehicle-app-developer-guide/vehicle-app-faq, "실행 플랫폼 확인").

### 2.10 Playground의 다른 공개 API(차량 앱 밖)

Pleos Playground에는 차량용 앱 SDK 외에도 API 문서가 공개되어 있습니다. 공모전 개발 안내는 이 API들을 공모전 SDK로 안내하지 않습니다(https://appdevchallenge.auto-hmg.io/guide/development).

| API | 성격 | 제공 데이터 | 사용 조건 | 출처 |
| --- | --- | --- | --- | --- |
| Vehicle Data API | 현대·기아·제네시스 커넥티드 카의 텔레매틱스 데이터를 서버에서 조회하는 클라우드 REST API | 충전 상태(/batteries), 파워트레인(/powertrains), 위치·방향·속도(/locations), 시동·누적 거리·주차(/driving), 도어·트렁크·타이어 공기압·경고등·공조(/status), 냉동고(/freezer), 기초 데이터(/powertrains/data, /speed, /driving/data, /status/data) | Private User는 API 키 발급 후 본인 차량 조회. Business User는 차량 소유자의 데이터 공유 동의가 필요하고, 기초 데이터는 동의 후 24시간이 지나야 조회 가능 | https://document.pleos.ai/api-reference/vehicle-data-api/intro |
| Fleet API | Pleos Fleet 기반 차량·단말 관리 REST API와 Webhook | 차량·단말 등록과 조회, 차량 데이터 조회, Webhook 실시간 수신. 이상 이벤트, 예약, 운전자, 정비, 운행 이력은 "지원 예정" | Pleos Fleet 가입 필요(상세 확인 못 함) | https://document.pleos.ai/api-reference/fleet-api/intro |
| Pleos Platform SDK | 승인된 privileged 앱에 차량 기능을 System API로 제공하는 SDK | 문서상 권한·기능·호환성 표는 "문서화 진행 중" | Maven 계정을 회사별 담당자에게 받아야 함. 공모전 참가자용이 아님 | https://document.pleos.ai/api-reference/pleos-platform-sdk/intro, https://document.pleos.ai/api-reference/pleos-platform-sdk/get-started |

Vehicle Data API의 목록에는 운전자 상태, 졸음, 실내 카메라 항목이 없습니다. 이 API는 차량 밖의 서버나 휴대폰 앱이 쓰는 경로이며, 국내 차종 지원 범위와 API 키 발급 조건은 로그인 필요로 확인 못 함입니다.

## 3. 기능 영역별 현실 문제와 불편

이 장은 SDK가 다루는 영역별로 운전자와 동승자가 실제로 겪는 문제, 그리고 기존 해결책이 부족한 이유를 정리합니다. 기관 발표를 인용한 기사는 재인용임을 밝혔습니다.

### 3.1 운전 보조·안전: 졸음과 주의 분산

고속도로 졸음·주시태만

- 한국도로공사 자료를 인용한 보도에 따르면 최근 3년간 고속도로 교통사고 사망자의 약 70%가 졸음·주시태만(추정)으로 발생했습니다(환경일보 2024년 2월, https://www.hkbs.co.kr/news/articleView.html?idxno=743674). 졸음과 주시태만을 합친 분류이며 졸음 단독 수치가 아닙니다.
- 2020~2024년 고속도로 전체 사고 8,280건 중 4,848건(58.6%)이 졸음·주시태만 사고였고, 설·추석 연휴에는 167건 중 109건(65.3%)이었습니다(한국도로공사 발표 인용, 뉴스핌 2025년 10월 2일, https://newspim.com/news/view/20251002001172).
- 도로공사 대전충남본부는 졸음 취약 시간대로 오후 2~4시를 제시했습니다(파이낸셜뉴스 2024년 5월, https://www.fnnews.com/news/202405171614485473).

졸음운전 사고 통계

- 경찰청 집계로 2019~2023년 졸음운전 사고는 10,765건, 사망자는 316명이고 치사율(사고 100건당 사망자)은 2.9명으로 음주운전 1.5명의 약 2배였습니다. 고속도로 졸음운전 치사율은 8.3명입니다. 주간(06~18시) 사망자가 201명으로 야간 115명보다 많았습니다(정책브리핑 2024년 4월, https://www.korea.kr/news/policyNewsView.do?newsId=148927915).
- 한국도로교통공단 발표에 따르면 2021~2023년 졸음운전 치사율은 2.7명으로 전체 교통사고 1.4명보다 높고, 사고는 12~18시에 몰리는 경향을 보였습니다(오토타임즈 2025년 4월, https://v.daum.net/v/2ozBNte7yM).
- 경찰청 2020~2024년 분석에서 졸음운전 사망자 252명 중 14.3%가 8월에 발생했고, 8월 고속도로 졸음운전 치사율은 10.81명이었습니다(파이낸셜뉴스 2025년 7월 30일, https://www.fnnews.com/news/202507301202194822).

스마트폰·터치스크린 주의 분산

- 2024년 교통문화지수 조사에서 운전 중 스마트기기 미사용 준수율은 63.43%였습니다(국토교통부·한국교통안전공단 2025년 2월 보도자료 첨부, https://www.korea.kr/common/download.do?fileId=198040390&tblKey=GMN). 설문조사 지표입니다.
- AAA 재단·유타대학교 실험(2017년, 차량 30종, 운전자 120명)에서 내비게이션 설정 같은 과제를 할 때 운전자의 주의가 40초 넘게 분산되었습니다. 23종은 높거나 매우 높은 주의 요구도를 보였습니다(https://newsroom.aaa.com/2017/10/new-vehicle-infotainment-systems-create-increased-distractions-behind-wheel/). 음성 명령도 평가 대상이었으므로 음성이면 항상 안전하다는 결론은 나오지 않습니다.
- 스웨덴 Vi Bilägare 시험(2022년, 시속 110km)에서 네 가지 과제 완료 시간은 물리 버튼 중심의 2005년식 Volvo V70이 10.0초, 현대 Ioniq 5가 26.7초였습니다(https://www.vibilagare.se/english/physical-buttons-outperform-touchscreens-new-cars-test-finds).
- Euro NCAP은 2026년 평가에서 방향지시등, 와이퍼, 비상등, 경적, eCall의 직접 물리 조작을 요구합니다(https://www.euroncap.com/press-media/buttons-are-back-for-basic-functions-euro-ncap-confirms-in-testing/).

기존 대응 수단과 한계

- 현대차그룹 DAW는 차로 추종 능력 저하, 갑작스러운 조향 같은 운전 패턴을 분석해 휴식을 권합니다(2022년, https://www.hyundaimotorgroup.com/ko/story/CONT0000000000016227). 기아 2024년형 설명서는 피곤하지 않아도 경고할 수 있고 부주의 상태를 판단하지 못할 수도 있다고 명시합니다(https://ownersmanual.kia.com/full_webhelp/TAM/2024/ko_KR/topics/t00045.html).
- 제네시스 GV70(2025년형)의 운전자 모니터링 시스템은 실내 카메라로 얼굴 방향과 눈 개폐를 보지만, 편광 선글라스나 가림 같은 제한 조건이 있습니다(https://ownersmanual.genesis.com/full_webhelp/JK/2025/ko_KR/topic_qzj_r31_syb.html). GV60은 2025년 3월 개편 모델에 실내 카메라가 추가되었습니다(https://newsroom.genesis.com/download/b8b83f4d-b1eb-4ced-bbb4-19bb1a86d969/250306-first-everredesignofgenesisgv60makeskoreandebut.pdf).
- EU는 운전 패턴 기반 졸음 경고(DDAW)를 신규 형식 2022년 7월, 모든 신차 2024년 7월부터 의무화했습니다(https://data.consilium.europa.eu/doc/document/ST-8164-2021-INIT/en/pdf). 시각 주의 기반 주의 분산 경고(ADDW)는 신규 형식 2024년 7월, 모든 신차 2026년 7월부터 요구합니다(https://data.consilium.europa.eu/doc/document/ST-11895-2023-INIT/en/pdf).
- 카카오모빌리티 내비게이션 SDK는 2022년 12월 고속도로 안내에 졸음쉼터 정보를 추가했습니다(https://developers.kakaomobility.com/guide/android/release.html).
- 티맵은 2024년 7월 졸음운전 예방 캠페인으로 휴게 매장 할인 쿠폰을 제공했습니다(https://www.tmapmobility.com/story/pr/detail/148). 두 앱이 개인의 졸음 상태를 감지한다는 근거는 확인 못 함입니다.
- 졸음쉼터 도입 뒤 고속도로 졸음운전 사망자는 2010년 119명에서 2011~2022년 연평균 69명으로 약 42% 줄었습니다(한국도로공사 자료 인용, 파이낸셜뉴스 2023년 2월, https://www.fnnews.com/news/202302191206328663). 다른 요인을 통제한 효과는 아닙니다.
- IIHS 조사(2024년)에서 차로 이탈 경고·방지 기능이 켜진 차량은 87%였지만, 소리로 알리는 과속 경고는 14%만 켜져 있었습니다(https://www.iihs.org/news/detail/fewer-drivers-are-opting-out-of-lane-departure-prevention). 불편한 경고는 꺼진다는 근거입니다. 국내 DAW 해제율은 확인 못 함입니다.

휴식 알림과 음성 대화의 효과

- 미국 NHTSA 실험(2023년, 72명, 새벽 4시간 모의 주행)에서 졸음 알림과 차로 이탈 경고를 함께 준 조건은 차로 이탈을 줄였지만, 휴식 빈도와 시점은 경고 없는 조건과 차이가 없었습니다(DOT HS 813 438, https://rosap.ntl.bts.gov/view/dot/67404). 원문 PDF는 자동 접근이 차단되어 기관 저장소의 초록으로 확인했습니다.
- AAA 재단 연구(2023년)에서 운전자는 극도로 졸리다고 느낄 때도 휴식 기회의 75%를 지나쳤습니다(https://newsroom.aaa.com/2023/03/asleep-at-the-wheel-drivers-unaware-of-how-drowsy-they-really-are/).
- 휴식 뒤 수행 개선은 40분 안에 원래 수준으로 돌아왔다는 모의 주행 연구(2025년, 90명)가 있습니다(https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:40470890&format=json&resultType=core).
- 음성으로 응답하는 과제는 자기보고 졸음 점수를 유의하게 낮췄습니다. 2025년 29명 모의 주행 연구입니다(https://eprints.whiterose.ac.uk/id/eprint/233018/1/Manuscript%20revised.pdf).
- 반대로 대화가 피로로 늦어진 긴급 제동 반응을 회복하지 못했다는 연구(2017년)도 있습니다(https://stars.library.ucf.edu/scopus2015/5195/). 자연 대화형 AI의 실차 효과는 검증되지 않았습니다.

기존 해결책의 한계: 차량 내장 DAW와 실내 카메라는 오경고와 미감지 조건을 제조사 스스로 밝히고 있고, 경고가 실제 휴식으로 이어진다는 근거는 약합니다. 내비게이션 앱은 쉼터 정보를 보여 주지만 운전자 상태는 모릅니다. 공개 API로 Pleos 앱이 운전자 상태를 받을 수 없다는 점(2.8절)과, 휴식 유도 자체의 효과가 약하다는 연구 결과를 함께 고려해야 합니다.

### 3.2 내비게이션·경로·휴게소

- 신차 구입자 중 순정 인포테인먼트를 쓰는 비율은 국산차 73%, 수입차 54%였고, 폰 프로젝션 사용률은 각각 17%, 36%였습니다. 컨슈머인사이트 2023년 7월 조사(신차 구입자 2,368명)입니다(https://www.consumerinsight.co.kr/voc_view?PageNo=1&id=pr4_list&no=3483&schFlag=0).
- 지도 갱신 지연으로 더 긴 경로를 안내한 사례가 보도되었습니다. 2025년 1월 개통한 고속도로 구간을 순정 내비게이션이 인식하지 못해, 같은 경로에서 티맵보다 12km, 22분 긴 경로를 안내했습니다(IT조선 2025년 3월, https://it.chosun.com/news/articleView.html?idxno=2023092136245). 개별 취재 사례이며 전체 오류율은 아닙니다.
- 폰 연결 장치도 연결 불가, 화면 끊김, 터치 불능 같은 오류 수정 공지를 반복합니다(카링킷 국내 업데이트 공지 2024~2025년, https://carlinkit.co.kr/updates/).
- 한국도로공사는 휴게소 명칭·위치·노선·방향을 공공데이터 API로 제공합니다(https://www.data.go.kr/data/15076770/openapi.do). 휴게소별 이용객·교통량은 연 단위 파일 자료(207행)입니다(https://www.data.go.kr/data/15118977/fileData.do). 두 공공데이터에는 실시간 잔여 주차면 정보가 없습니다. 다른 경로로 실시간 주차면 API가 있는지는 확인 못 함입니다.

기존 해결책의 한계: 폰 프로젝션은 순정 지도 갱신 문제를 피하지만 연결 오류를 새로 만듭니다. 위의 두 휴게소 공공데이터는 위치와 연간 통계 위주여서 "도착 시점에 쉴 자리가 있는지"를 알려 주지 못합니다. Pleos NaviHelper도 휴게소 검색 API가 없으므로(2.4절), 휴게소 안내는 공공데이터 좌표를 앱이 경유지로 넣는 방식이 됩니다.

### 3.3 전기차 충전

- EV Infra 사용자 1,532명 조사에서(조사 연도는 기사 본문에서 확인 못 함) 가장 큰 불편은 잦은 고장 30.1%, 충전 매너 부족 26.1%였습니다. "사용 가능" 표시를 보고 갔는데 다른 차가 충전 중이던 경험은 20.6%, 결제 오류는 6.9%였습니다(https://www.thedrive.co.kr/news/newsview.php?ncode=1065569876290312).
- 한국전기차사용자협회가 2023년 3~6월 환경부 급속충전기 7,812기를 점검한 결과, 충전 불가·폐쇄 비중은 2022년 13.2%에서 2023년 7.7%로 낮아졌습니다. 기사는 환경부 집계 고장률 1% 미만과 현장 점검 약 7%의 차이를 지적합니다(https://www.electimes.com/news/articleView.html?idxno=324471).
- 국무조정실·환경부 합동 점검(2025년 4~6월)에서 무공해차 통합누리집은 충전시설 21,283기의 상태를 정확히 표시하지 못했습니다(연합뉴스 2025년 9월 17일, https://www.yna.co.kr/view/AKR20250917032700001).
- 2023년 EV이음 협약으로 86개 사업자의 회원카드를 쓸 수 있는 사업자가 늘었지만, 사업자별 회원 요금 차이는 남아 있습니다(https://www.electimes.com/news/articleView.html?idxno=325975).
- 아이오닉 5 2WD 롱레인지 20인치의 환경부 인증 주행거리는 상온 405km, 저온 354km로 약 12.6% 줄었습니다(연합뉴스 2023년 1월, https://www.yna.co.kr/view/AKR20230126074300003). 이 값은 한 사양의 인증값이며 모든 전기차의 감소율은 아닙니다.

기존 해결책의 한계: 충전 앱의 "사용 가능" 표시가 도착 후 충전을 보장하지 못합니다(20.6%, 21,283기 상태 오류). 카드 호환이 늘어도 요금은 사업자마다 다릅니다. Pleos 차량 앱은 실제 배터리 잔량(getEvBatteryStateOfCharge, https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/Vehicle/vehicle/ai.pleos.playground.vehicle.api/ev-battery/get-ev-battery-state-of-charge)과 내장 내비게이션의 도착 시 예상 잔량(TripInfo.estimatedSocAtDest), 경로상 충전 계획(DrivingState.chargingPlan)을 한 앱 안에서 읽을 수 있습니다(https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/NaviHelper/navi-helper/ai.pleos.playground.navi.data/entry). 폰 앱이 같은 정보를 얻는 다른 경로(예: 클라우드 Vehicle Data API, 2.10절)는 별도 동의와 가입이 필요합니다.

### 3.4 차량 음성 비서와 앱 생태계

- 현대차그룹은 Pleos Connect를 2026년 5월 국내 신형 그랜저에 처음 적용한다고 발표했습니다(2026년 4월 30일, https://www.hyundai.com/worldwide/en/newsroom/detail/0000001168). 현대차 공식 행사 안내는 더 뉴 그랜저와 디 올 뉴 아반떼에 Pleos Connect가 탑재되었다고 적습니다(https://www.hyundai.com/kr/ko/event/event-pleos-challenge-by-h-stylist-2026).
- 그랜저 시승 기사(2026년 5월 29일)는 음성 인식 실패, 동승석 발화를 운전석으로 인식한 오류, 한 번에 2~3개 기능을 요청할 때의 처리 미흡을 기록했습니다(https://www.kukinews.com/article/print/kuk202605290163). 기자 1명의 시승이며 오류율은 아닙니다.
- Gleo AI 개발자 인터뷰(2026년 9월 29일)는 경유지를 포함한 복잡한 목적지 설정을 주요 과제로 개발 중이고, 오래 주고받는 대화는 아직 기억하지 못한다고 밝혔습니다. 같은 인터뷰는 음성으로 쓸 수 있는 앱은 일부 프리로드 앱이며 서드파티 연동은 논의 중이라고 설명했습니다(https://www.hyundaimotorgroup.com/ko/story/42dot-gleo-ai-developer-present-and-future).
- 2024년 기아 카니발 개발자 인터뷰는 명령어 인식 시간이 0.4초이고 CPU 부하가 크면 약 1.5초까지 늘 수 있다고 설명했습니다(https://www.hyundaimotorgroup.com/ko/story/CONT0000000000143973).
- 미국 J.D. Power의 음성 인식 문제 조사는 원문 접근이 차단되어 수치를 확인 못 함입니다.

기존 해결책의 한계: 제조사는 복잡한 경유지 설정을 개발 과제로 두고 있고, 시승 기사는 복합 명령 처리의 미흡을 기록했습니다. 서드파티 앱의 음성 연동 규격은 Gleo Interface(App Schema, 함수 최대 3개)입니다(https://document.pleos.ai/docs/pleos-only/app-integration-guide/guide/app-capability). 공모전이 안내하는 SDK 목록에는 이 규격이 없습니다(https://appdevchallenge.auto-hmg.io/faq).

### 3.5 차량 상태·정비

- 한국소비자원 자료를 인용한 보도에 따르면 2022년~2025년 5월 자동차 정비 관련 피해구제 신청은 953건이고, 정비 불량이 699건(73.3%), 사전 고지 없는 수리비 청구가 173건(18.2%)이며, 합의는 352건(36.9%)이었습니다(동아일보 2025년 7월 18일, https://www.donga.com/news/Society/article/all/20250718/132027236/2).
- 현대해상 긴급출동 분석(2022년 3월~2024년 2월)에서 겨울철 출동의 58.1%가 배터리 충전 요청이었습니다. 전기차는 긴급 견인 29.6%, 타이어 펑크 수리 24.7%, 배터리 충전 24.1%였습니다(이데일리 2025년 2월 26일, https://www.edaily.co.kr/News/Read?mediaCodeNo=257&newsId=02755206642074456).
- 영국 자동차 소유자 2,000명 조사(2024년)에서 46%는 계기판 경고등의 절반도 식별하지 못했습니다(https://www.warrantywise.co.uk/blog/news/23-million-uk-drivers-in-the-dark-when-it-comes-to-identifying-dashboard-warning-lights/). 국내 경고등 이해율 조사는 확인 못 함입니다.

기존 해결책의 한계: 영국 조사에서는 운전자의 46%가 경고등의 절반도 식별하지 못했습니다. 국내 정비 분쟁에서는 합의가 36.9%에 그쳤습니다. Pleos 차량 앱은 엔진오일·브레이크액·워셔액 상태와 타이어 저압 임계값을 CAR_SAFETY(normal) 권한으로 읽을 수 있습니다(https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/Vehicle/vehicle/ai.pleos.playground.vehicle.api/safety/entry). 반면 경고등 전체 목록(getTelltalesInfo)은 PRIVATE_CAR_SAFETY(signature|privileged)여서 "켜진 경고등을 설명해 주는 앱"은 공개 API로 만들 수 없습니다(https://document.pleos.ai/docs/pleos-only/connect-sdk-pleos/Vehicle/vehicle/ai.pleos.playground.vehicle.api/safety/get-telltales-info).

### 3.6 뒷좌석 아이와 가족 이동

차내 방치

- 2018년 7월 17일 동두천에서 4세 아동이 어린이집 차량에 7시간 10분 동안 갇혀 숨졌습니다(서울신문·연합뉴스 2018년 9월 7일, https://www.seoul.co.kr/news/society/2018/09/07/20180907800066).
- 이 사고 뒤 어린이 통학버스 하차 확인장치가 2019년 4월 17일부터 의무가 되었습니다. 엔진 정지 후 3분 안에 차량 맨 뒤 버튼을 누르지 않으면 경고음과 비상점멸등이 작동합니다(https://www.ibabynews.com/news/articleView.html?idxno=73666 및 정부 브리핑 https://www.korea.kr/news/policyNewsView.do?newsId=148859879). 이 장치는 사람이 뒤까지 가게 만드는 절차이며 아이를 자동으로 감지하지 않습니다.
- 미국 Kids and Car Safety 집계로 2024년 차내 고온 사망 아동은 41명이고, 1990~2024년 누적은 최소 1,126명입니다(https://www.kidsandcars.org/hot-cars/2024-deaths).
- 같은 단체는 고온 차량 사망의 약 88%가 3세 이하라고 밝혔습니다(https://www.kidsandcars.org/news/hot-car-death-season-in-the-us-is-underway-what-can-be-done-to-save-children). NHTSA 원문은 접근이 차단되어 확인 못 함입니다. 국내 연도별 차내 방치 사망 통계도 확인 못 함입니다.
- Euro NCAP은 2023년 평가부터 아동 존재 감지(CPD)에 점수를 주기 시작했습니다(https://www.euroncap.com/press-media/lexus-puts-safety-up-front-in-all-new-electric-rz/). 2025년 이후 세부 배점은 확인 못 함입니다.

현대·기아 후석 승객 알림의 작동 방식

- 1차 알림은 뒷문을 열고 닫은 이력을 이용합니다. 시동을 끄고 운전석 문을 열면 뒷좌석 확인 메시지를 띄웁니다. 센서 사양은 1차 알림 뒤 문을 잠그면 약 10분 동안 실내 움직임을 감지하고, 감지하면 경적을 약 25초씩 최대 8회 울립니다(현대 2026년형 미국 설명서 https://ownersmanual.hyundai.com/full_webhelp/MX5aHEV/2026/en_US/id5afd08a9aae.html 및 기아 2023년형 한국어 설명서 https://ownersmanual.kia.com/full_webhelp/NQ5KH/2023/ko_KR/topics/t00421.html).
- 기아 설명서는 1차 알림이 없으면 2차 알림도 작동하지 않는다고 적습니다. 작은 움직임, 담요나 보조 좌석의 가림, 센서 오염은 미감지 원인이고, 바람, 벌레, 진동은 오경보 원인입니다(같은 기아 설명서). 현대 STARIA의 일부 시장 사양은 레이더 센서를 씁니다(https://www.hyundai.com/worldwide/en/newsroom/detail/0000000538).

카시트와 안전띠

- 2025년 유아용 카시트 착용률은 도시부도로 60.07%, 고속도로 66.25%였습니다. 고속도로 뒷좌석 안전띠 착용률은 69.65%였습니다(국토교통부·한국교통안전공단 교통문화실태조사 인용 보도 2026년 2월 1일, https://v.daum.net/v/20260201110121480). 다른 표본조사에서 2022년 뒷좌석 안전띠 착용률은 32.3%였습니다(https://www.fnnews.com/news/202309171101072946). 두 조사는 범위가 달라 직접 비교하지 않습니다.
- 2011~2015년 교통사고로 응급실을 찾은 6세 미만 3,240명 중 카시트 착용은 31%였고, 미착용군의 중상 위험은 2.2배, 머리 손상 위험은 2.1배로 보고되었습니다(질병관리본부 2016년 12월, https://www.korea.kr/briefing/policyBriefingView.do?newsId=148826033).

부모 운전자의 주의 분산

- 호주 Monash 대학 연구(2012년, 12가구 자연주행 영상)에서 운전자가 뒷좌석 아이와 상호작용한 빈도는 휴대전화 상호작용의 12배였습니다(https://research.monash.edu/en/publications/prevalence-of-mobile-phone-vs-child-related-driver-distraction-in/). 12배는 상호작용 빈도이며 충돌 위험을 뜻하지 않습니다. 관련 보도에 따르면 아이 관련 행동의 76.4%가 뒤돌아보거나 거울로 보는 행동이었고, 평균 16분 주행에서 3분 22초 동안 시선이 도로를 벗어났습니다(https://www.asianscientist.com/2013/10/in-the-lab/children-distracting-mobile-phones-2013/).
- 애프터마켓 아이 확인용 거울이 충돌 때 떨어지거나 깨져 다칠 수 있다는 카시트 안전 안내가 있습니다(https://www.vumc.org/injuryprevention/node/228). 이 주소가 보여 주는 본문의 작성 기관은 확인 못 함입니다. 뒷좌석 카메라 제품은 2015년에도 있었지만(Garmin babyCam, https://www.garmin.com/en-US/newsroom/press-release/automotive/2015-adding-multimedia-garmin-delivers-babycam-the-worlds-first-video-monitor-navigation-system/), 화면을 보는 시간이 남는다는 점은 이 보고서의 해석이며 측정된 값은 없습니다.

멀미와 지루함

- CDC는 멀미가 2~12세 아동에게 더 흔하고, 지평선 보기, 눈 감기, 음악 듣기를 비약물 대처법으로 제시합니다(https://wwwnc.cdc.gov/travel/page/motion-sickness). 한국 아동 유병률은 확인 못 함입니다.
- 영국 부모 2,000명 조사(2022년)에서 68%가 뒷좌석 짜증의 원인으로 지루함을 꼽았고, "거의 다 왔어요?"는 출발 32분 뒤에 나왔습니다(https://www.rte.ie/news/newslens/2022/0822/1317041-are-we-there-yet-formula-created-to-predict-tantrums/). 상업 후원 조사입니다.
- 2025년 추석 특별교통대책기간 예상 이동인원은 3,218만 명이고 승용차 비중은 84.5%였습니다(국토교통부 대책 게시, https://www.kric.go.kr/jsp/board/portal/sub01/railNewsDetail.jsp?p_id1=M01060101&p_id2=661585&p_id3=2025.09.29). 전국 평균 귀성 소요시간은 확인 못 함입니다.

기존 해결책의 한계: 하차 확인장치는 버튼 절차이고, 후석 승객 알림은 문 개폐 이력과 10분 감지라는 조건이 붙어 있습니다. 거울과 카메라는 운전자의 시선을 다시 화면으로 끌어옵니다. 차량 앱은 좌석별 점유(getCurrentSeatOccupancy), 안전벨트(getCurrentSeatBeltBuckledState), 도어(getCurrentDoorPosition), 도어 잠금, 실내 온도(getHvacTemperatureCurrent)를 normal 권한으로 읽을 수 있습니다(2.3절). 다만 차량 앱은 시동이 꺼진 뒤 계속 동작한다는 근거가 문서에 없어, 하차 후 방치 감지는 앱 단독으로 보장할 수 없습니다(확인 못 함).

### 3.7 동승자 엔터테인먼트

- BMW 7시리즈(2022년)는 31인치 뒷좌석 화면을 제공합니다(https://www.press.bmwgroup.com/usa/article/detail/T0382613EN_US/the-new-bmw-7-series). BMW 5시리즈의 AirConsole 게임은 스마트폰을 컨트롤러로 쓰며 정차 중에 함께 즐기는 방식입니다(2023년, https://www.press.bmwgroup.com/usa/article/detail/T0419599EN_US).
- Audi는 동승석 화면이 있는 차량에서 운전자에게 화면이 보이지 않게 하는 프라이버시 모드로 주행 중 게임을 제공합니다(2025년, https://www.audi-mediacenter.com/en/press-releases/gaming-fun-on-the-go-audi-integrates-airconsole-16729). Mercedes-Benz E-Class는 운전자 눈의 움직임을 카메라로 보고 동승석 화면 밝기를 낮춥니다(https://media.mbusa.com/news/the-new-e-class-dimensional-concept-and-interior-design).
- Tesla는 2021년 12월 중앙 화면의 주행 중 Passenger Play를 OTA로 비활성화했고, NHTSA는 조사를 종결했습니다(AP 보도 2023년 5월 30일, https://www.cbsnews.com/detroit/news/us-ends-probe-into-tesla-allowing-video-games-while-vehicles-are-moving-says-feature-was-disabled/).
- 국내에서는 현대 블루링크 스트리밍 요금제에 게임이 있고 ccNC 차량에 한정됩니다(https://www.hyundai.com/kr/ko/digital-customer-support/app/myhyundai/bluelink-registration). 기아 커넥트 스토어는 차량용 아케이드 게임 8종을 안내합니다(https://connectstore.kia.com/kr/info/product-usage-guide-incargame).
- 미국 성인 조사(2024년 발표)에서 뒷좌석 화면을 원한다는 응답은 58%였습니다. 이 값은 선호이며 실제 이용률이 아닙니다(https://wctvtv.marketminute.com/article/bizwire-2024-6-12-dts-reports-radio-remains-crucial-while-video-and-gaming-surge-in-vehicle). 한국 승객의 이용률은 확인 못 함입니다.
- 도로교통법 제49조 제1항 제11호는 운전 중 "운전자가 운전 중 볼 수 있는 위치에 영상이 표시되지 아니하도록" 하라고 정하고, 정지 중이거나 지리안내·교통정보·긴급상황·주변 확인 영상인 경우를 예외로 둡니다. 제11호의2는 운전 중 영상표시장치 조작을 금지합니다(https://www.law.go.kr/lsLawLinkInfo.do?chrClsCd=010202&lsJoLnkSeq=1000842761). 2026년 현행 조문과의 일치는 확인 못 함입니다.

기존 해결책의 한계: 해외 차량 게임은 정차 중 전용이거나 별도 동승석 화면과 시선 차단 장치를 전제합니다. Pleos 문서는 동영상, 게임, 브라우저 앱을 주행 중 실행할 수 없게 하라고 요구하고(2.9절), 동승석 전용 화면 API는 공개 문서에서 찾지 못했습니다. 따라서 주행 중 동승자 참여는 화면을 쓰지 않는 음성·오디오 방식이나 승객의 휴대폰을 쓰는 방식만 남습니다.

## 4. 교차표: 현실 문제 × 쓸 수 있는 데이터

판정 기준은 1장과 같습니다. "가능"은 지금 쓸 수 있는 공개 API로 필요한 데이터를 모두 얻는 경우, "부분"은 일부만 얻거나 준비 중 SDK·외부 데이터에 기대는 경우, "불가"는 핵심 데이터가 signature|privileged 권한 뒤에 있거나 공개 API가 없는 경우입니다. 이 표는 순위가 아니며 아이디어를 고르지 않습니다. API 출처는 2장의 해당 절에 있습니다.

| 번호 | 현실 문제(근거 절) | 필요한 데이터 | 공개 API(이름 그대로) | 판정 | 판정 이유 | 폰으로는 못 하는 이유 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 졸음·주의 저하 상태를 직접 알아내 경고(3.1) | 운전자 졸음·주의 상태, DAW 경고, 차선 이탈 경고 | TelltaleType.DRIVER_ATTENTION, LKA(PRIVATE_CAR_SAFETY), DRIVER_DROWSINESS_ATTENTION_STATE, LANE_DEPARTURE_WARNING_STATE | 불가 | 모두 signature|privileged 권한이며 실내 카메라 API도 없습니다(2.3, 2.7, 2.8절) | 해당 없음(차량 앱도 받지 못함) |
| 2 | 장시간 연속 주행의 피로 위험을 추정해 휴식 제안(3.1, 3.2) | 현재 주행 시간, 속도, 시각, 남은 거리·시간, 휴게소 좌표 | getTripCurrentDrivingTime(CAR_DRIVE), PERF_VEHICLE_SPEED(AAOS), DestinationInfo.remainTime, requestRouteWithWaypoints, 휴게소는 한국도로공사 공공데이터 | 부분 | 차량 데이터는 얻지만 졸음 판정이 아닌 시간 기반 추정입니다. 휴게소 검색 API가 없어 외부 데이터가 필요하고, 음성 출력 SDK(TTS)는 준비 중입니다 | 폰은 차량 세션의 실제 주행 시간과 차량 속도 신호를 직접 읽지 못하고, 내장 내비게이션 경로에 경유지를 넣지 못합니다 |
| 3 | 주행 중 뒷좌석 아이의 안전벨트 풀림·착좌 이상 확인(3.6) | 좌석별 점유, 좌석별 안전벨트, 속도, 도어 상태 | getCurrentSeatOccupancy, registerSeatOccupancy, getCurrentSeatBeltBuckledState, registerSeatBeltBuckledState(CAR_SEATS), getCurrentDoorPosition(CAR_DOORS), PERF_VEHICLE_SPEED | 가능 | 모두 normal 또는 dangerous 권한이며 Vehicle State 범위입니다. 에뮬레이터에 Seat Occupancy 카드가 있습니다. 실차 좌석 센서 위치는 차종별입니다 | 폰은 좌석 센서와 안전벨트 신호에 접근할 수 없습니다 |
| 4 | 하차 후 뒷좌석 아이 방치(3.6) | 시동 종료 시점, 뒷좌석 점유, 도어 개폐·잠금 | getCurrentSeatOccupancy, getCurrentDoorPosition, getDoorLockState, GEAR_SELECTION | 부분 | 데이터는 읽지만 시동이 꺼진 뒤 앱이 계속 동작하는지 문서로 확인 못 했고, 차량에 이미 후석 승객 알림이 있습니다. 아동 존재 감지 결과값 API는 없습니다 | 폰은 좌석 점유를 모릅니다. 다만 차량 앱도 시동 후 동작은 확인 못 함입니다 |
| 5 | EV 충전 불확실성과 도착 잔량 불안(3.3) | 현재 SOC, 도착 예상 SOC, 경로상 충전 계획, 효율, 공조 상태 | getEvBatteryStateOfCharge, getCurrentEvEfficiency(CAR_ENERGY), TripInfo.estimatedSocAtDest, DrivingState.chargingPlan, getChargerOperatorInfo, getHvacPowerState(CAR_CLIMATE), ENV_OUTSIDE_TEMPERATURE | 가능 | Vehicle State와 NaviHelper만으로 구성됩니다. 충전기 실시간 가용 정보는 외부 데이터가 필요합니다 | 폰 충전 앱은 실제 배터리 잔량과 내장 내비게이션의 도착 잔량 예측을 함께 보지 못합니다 |
| 6 | 위험 구간·제한 속도 사전 안내(3.1) | 경로상 주의 지점, 현재 도로 제한 속도, 차량 속도 | onCautionPointInfo(SCHOOL_ZONE, ACCIDENT_PRONE_AREA, FOG_AREA 등), onCurrentRoadSpeedLimit(1초 주기), onCameraAlert, PERF_VEHICLE_SPEED | 가능 | NaviHelper(사용 가능)와 AAOS 속도로 구성됩니다. 내장 내비게이션이 이미 안내하는 정보와 겹칠 수 있습니다 | 폰 내비게이션은 같은 안내를 하지만 차량 속도 신호와 순정 내비게이션 상태를 결합하지 못합니다 |
| 7 | 정비·소모품 상태를 몰라 생기는 고장과 분쟁(3.5) | 엔진오일·브레이크액·워셔액, 타이어, 누적 거리, 경고등 | getEngineOilLevelState, getBrakeFluidLevelState, hasLowWasherFluidWarning(CAR_SAFETY), getLowTirePressure, getCurrentDistanceDriven | 부분 | 오일·액체·누적 거리는 normal 권한입니다. 타이어는 저압 임계값만 있고 실제 공기압은 없으며, 경고등 전체 목록은 signature|privileged입니다 | 폰은 차량 액체 수준과 누적 거리를 직접 읽지 못합니다(클라우드 Vehicle Data API는 별도 동의 필요, 2.10절) |
| 8 | 아이가 탄 차의 실내 환경 관리(3.6) | 좌석 점유, 실내 온도, 공조·공기청정 제어, 앰비언트 조명 | getCurrentSeatOccupancy, getHvacTemperatureCurrent, setHvacTemperature, setHvacAirCleaner(CONTROL_CAR_CLIMATE), setAmbientLightBrightnessColor(CONTROL_CAR_LIGHTS) | 부분 | 읽기는 가능하지만 제어(set) API는 Vehicle Control로 추정되어 준비 중 상태입니다 | 폰은 공조와 조명을 제어하지 못합니다 |
| 9 | 장거리 이동에서 동승자 지루함(3.6, 3.7) | 현재 위치·주소, 경로, 남은 시간, 경유지, 음성 입출력 | getCurrentLocationInfo, onTripInfo, DestinationInfo.remainTime, onWayPointArrived, SpeechToText·TextToSpeech | 부분 | 위치와 경로는 사용 가능하지만 음성 입출력 SDK가 준비 중입니다. 주행 중 게임·동영상은 허용되지 않습니다(2.9절) | 폰은 내장 내비게이션의 경로와 남은 시간을 실시간으로 받지 못합니다 |
| 10 | 경고등 의미를 모르는 운전자(3.5) | 켜진 경고등 종류·색·상태 | getTelltalesInfo, registerTelltales | 불가 | PRIVATE_CAR_SAFETY(signature|privileged)입니다(2.3절) | 해당 없음 |

교차표에서 반복되는 사실은 세 가지입니다. 첫째, 운전자 상태와 ADAS 경고는 공개 API로 받을 수 없습니다. 둘째, 좌석 점유·안전벨트·도어·배터리·주행 시간 같은 차량 상태와 내장 내비게이션 데이터는 지금 쓸 수 있습니다. 셋째, 음성 입출력과 차량 제어는 준비 중이어서 공모전 일정 안에 쓸 수 있는지가 불확실합니다.

## 5. 후보 아이디어 3개의 실현 가능성

이 장은 세 후보를 같은 기준으로 판정합니다. 어느 후보를 고를지는 판단하지 않습니다.

### 5.1 졸음운전 대응(ADAS 감지 + Gleo AI 대화 + NaviHelper 휴게소 안내)

| 구성 요소 | 필요한 것 | 공개 API로 가능한가 | 근거 |
| --- | --- | --- | --- |
| 졸음·부주의 감지 | DAW 경고, 운전자 모니터링, 차선 이탈 경고 | 불가 | TelltaleType.DRIVER_ATTENTION과 LKA는 PRIVATE_CAR_SAFETY(signature|privileged), AAOS DRIVER_DROWSINESS_ATTENTION_STATE와 LANE_DEPARTURE_WARNING_STATE도 signature|privileged입니다. 실내 카메라 API는 없습니다(2.3, 2.7, 2.8절) |
| 졸음 위험 추정 | 연속 주행 시간, 속도, 시각, 조향 변화 | 부분 | getTripCurrentDrivingTime, PERF_VEHICLE_SPEED, registerSteeringWheelAngle은 읽을 수 있습니다. 조향각은 앞바퀴 각도이고 갱신 주기가 문서에 없어 졸음 판정 근거로 검증되지 않았습니다(2.3절) |
| Gleo AI 대화 | 앱이 먼저 운전자에게 말을 거는 대화형 AI | 불가 | Gleo Interface는 사용자가 말했을 때 Gleo AI가 앱 함수를 부르는 구조이며, 앱이 Gleo AI 대화를 시작하는 API는 찾지 못했습니다. 공모전 SDK 목록에도 없습니다(2.7절) |
| 앱 자체 음성 대화 | 음성 출력과 인식 | 부분 | TextToSpeech, SpeechToText가 있지만 공모전 상태는 준비 중입니다(2.1절, 2.5절) |
| 휴게소 안내 | 휴게소 위치와 경유지 설정 | 부분 | NaviHelper에 휴게소 검색은 없습니다. 한국도로공사 공공데이터 좌표를 requestRouteWithWaypoints나 addWaypoint로 넣는 방식은 가능합니다(2.4절, 3.2절) |

판정: 부분. 후보가 내건 "ADAS로 졸음 감지"는 불가입니다. "공개 ADAS·차량 데이터로 졸음·부주의를 실제로 알 수 있는가"에 대한 답은 "알 수 없다"입니다. 부분 판정은 공개 데이터로 구현할 수 있는 나머지 기능, 즉 주행 시간과 시각에 근거한 피로 위험 추정과 휴게소 경유지 안내를 가리킵니다. 차량에는 이미 운전자 주의 경고(DAW)가 있고, 휴식 알림이 실제 휴식으로 이어지지 않았다는 연구가 있습니다(3.1절).

### 5.2 뒷좌석 아이 케어

| 구성 요소 | 필요한 것 | 공개 API로 가능한가 | 근거 |
| --- | --- | --- | --- |
| 아이 탑승 여부 | 뒷좌석 좌석별 점유 | 가능 | getCurrentSeatOccupancy, registerSeatOccupancy(CAR_SEATS, normal). SeatValue에 ROW_2_LEFT 등 1~3열이 있고 에뮬레이터 Seat Occupancy 카드로 재현됩니다(2.3절). 실차 센서 좌석은 차종별 확인 필요 |
| 안전벨트 풀림 | 좌석별 버클 상태 | 가능 | getCurrentSeatBeltBuckledState, registerSeatBeltBuckledState(CAR_SEATS), hasSeatBeltNotBuckledWarning(CAR_SAFETY) |
| 도어·창문 | 뒷문 열림, 창문 위치·잠금 | 부분 | getCurrentDoorPosition, getCurrentWindowPosition, getCurrentWindowLockState는 읽기 가능. setWindowLock, setDoorLock은 제어 API로 준비 중 추정 |
| 실내 환경 | 실내 온도, 공조·공기청정 | 부분 | getHvacTemperatureCurrent, getHvacAirCleanerState는 읽기 가능. set* 제어는 준비 중 추정 |
| 아이 상태 확인 | 뒷좌석 카메라, 소리, 생체 신호 | 불가 | 카메라·생체 API가 없습니다(2.8절) |
| 하차 후 방치 감지 | 시동 종료 후 감지·알림 | 부분 | 데이터는 읽지만 시동 후 앱 동작은 확인 못 함이고, 아동 존재 감지 결과 API는 없습니다(2.8절, 3.6절) |

판정: 부분. 읽기 기능은 가능하고 제어·영상·하차 후 감지는 부분 또는 불가입니다. 주행 중 뒷좌석 착좌·안전벨트·도어·실내 온도를 모니터링하는 기능은 지금 공개 API로 만들 수 있고 에뮬레이터로 시연할 수 있습니다. 아이의 상태를 보거나 듣는 기능과 하차 후 방치 감지는 공개 API로 보장할 수 없습니다. 기존 후석 승객 알림과 하차 확인장치는 하차 시점을 다룹니다(3.6절). 차량이 주행 중 뒷좌석 안전벨트 경고를 이미 어디까지 제공하는지는 차종별로 다르며 이 조사에서 확인 못 했습니다.

### 5.3 동승자 참여형 엔터테인먼트

| 구성 요소 | 필요한 것 | 공개 API로 가능한가 | 근거 |
| --- | --- | --- | --- |
| 주행 중 화면 게임·영상 | 주행 중 실행 | 불가 | 미디어 앱(동영상, 게임, 브라우저)은 운전 중 실행·사용할 수 없습니다. 도로교통법 제49조는 운전자가 볼 수 있는 위치의 영상 표시를 금지합니다(2.9절, 3.7절) |
| 동승석 전용 화면 | 동승석 디스플레이 제어 | 불가 | 동승석 화면 API를 공개 문서에서 찾지 못했습니다(2.9절). 실차에 동승석 화면이 있는지는 확인 못 함 |
| 위치·경로 기반 콘텐츠 | 현재 위치, 주소, 경로, 남은 시간, 경유지 도착 | 가능 | getCurrentLocationInfo, onTripInfo, DestinationInfo, onWayPointArrived(NaviHelper, 사용 가능) |
| 음성 퀴즈·대화 | 음성 입출력 | 부분 | TextToSpeech, SpeechToText 준비 중. ON_DEVICE 모드는 앱 등록이 필요 없지만 공모전 사용 가능 여부는 확인 못 함 |
| 동승자 확인 | 좌석별 탑승 | 가능 | getCurrentSeatOccupancy는 동승석·뒷좌석 좌석별 점유 여부(Boolean)를 줍니다. 탑승자 수는 좌석별 값에서 앱이 계산해야 하며, 어느 좌석에 센서가 있는지는 차종별입니다 |
| 분위기 연출 | 앰비언트 조명 | 부분 | setAmbientLightBrightnessColor는 제어 API로 준비 중 추정 |
| 정차·충전 중 게임 | 주차 상태 확인 | 가능 | 심사 가이드는 "모든 미디어 앱은 정차 중에만 사용 가능"하다고 적고(https://document.pleos.ai/docs/pleos-only/distribute/app-review-guide/review-driver-distraction-elements), 주행 규제 정책은 Parking 상태에서 앱 사용을 허용합니다(https://document.pleos.ai/docs/pleos-only/vehicle-app-planning-guide/driving-restiction-policy). 주행 상태는 AAOS CarUxRestrictionsManager(Android 표준 API, Pleos SDK 아님)와 GEAR_SELECTION(normal)으로 확인합니다 |

판정: 부분. 주행 중 화면을 쓰는 엔터테인먼트는 정책과 법령으로 막혀 있습니다. 주행 중에는 위치·경로와 좌석 점유를 쓰는 오디오·음성 중심 참여만 가능하고, 음성 SDK가 준비 중이라는 점이 공모전 일정상 위험입니다. 정차·충전 중 화면 콘텐츠는 가능합니다.

### 5.4 세 후보 공통 위험

- 준비 중 SDK 의존: TextToSpeech, SpeechToText, FusedLocation, Vehicle Control은 공모전 접수 기간(2026년 10월 21일~11월 15일)과 2차 PT(12월 3~4일) 전에 "사용 가능"으로 바뀐다는 공지를 찾지 못했습니다(일정 https://appdevchallenge.auto-hmg.io/, 공지 목록 https://appdevchallenge.auto-hmg.io/notice).
- 심사와 출시는 다릅니다. 공모전은 에뮬레이터 시연을 인정하지만, App Market 출시에는 퍼미션 사전 승인과 주의 분산 심사가 따로 있습니다(2.1절).
- 차종별 지원: 모든 Vehicle SDK 기능은 checkXXXCapabilities로 지원 여부를 확인하도록 설계해야 합니다(2.2절).

## 6. 확인 못 한 것

아래 항목은 공개 자료만으로 결론을 내리지 못했습니다. 기획서에 쓰기 전에 직접 실행이나 공식 답변으로 확인해야 합니다.

| 항목 | 확인 못 한 이유 | 확인 방법 |
| --- | --- | --- |
| 준비 중(Coming Soon) SDK가 에뮬레이터에서 실제로 호출되는지 | 로그인 후 프로젝트를 만들고 에뮬레이터에서 실행해야 알 수 있음. 이 조사는 로그인하지 않았음 | 에뮬레이터에서 TextToSpeech ON_DEVICE, SpeechToText ON_DEVICE, FusedLocation isSupported 호출 |
| Vehicle State와 Vehicle Control의 API 경계 | 신청 화면이 로그인 필요로 확인 못 함. 이 보고서는 CAR_* 조회 / CONTROL_CAR_* 제어로 추정 | Playground Workspace의 SDK 상세 화면 |
| Gleo Interface(App Schema)를 공모전 앱이 쓸 수 있는지 | 공모전 SDK 목록에 없고 App Schema 등록 절차가 공개 문서에 없음 | 공모전 온라인 설명회(2026.10.28) 안내 확인 |
| Pleos Connect 실차가 제공하는 AAOS 프로퍼티 범위 | 실차 접근 없음. 문서는 모델마다 다르다고만 안내 | CarPropertyManager.getPropertyList 결과 |
| 에뮬레이터에서 차량 속도를 바꾸는 방법 | 셋업 가이드는 "차량 속도" 변경을 언급하지만 사용 가이드 카드 목록에 속도 카드가 없음 | Virtual Console 화면 직접 확인 |
| Vehicle SDK 리스너의 갱신 주기 | 문서에 Hz나 주기 값이 없음 | 에뮬레이터에서 콜백 간격 측정 |
| 일반 Android 카메라·마이크 API 사용 가능 여부 | Pleos 문서에 언급 없음 | 에뮬레이터 권한 요청 실험, 앱 심사 가이드 재확인 |
| 좌석 점유 센서가 뒷좌석에도 있는 차종 | API는 1~3열을 정의하지만 실차 센서 위치는 차종별 | checkSeatOccupancyCapabilities 결과 |
| getTelltalesInfo의 실제 요구 권한 | 같은 페이지에 CAR_SAFETY(어노테이션)와 PRIVATE_CAR_SAFETY(설명)가 함께 적혀 있음 | normal 권한으로 호출해 ERROR_SECURITY_PERMISSION 여부 확인 |

