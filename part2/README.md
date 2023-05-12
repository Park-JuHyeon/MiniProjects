# 미니프로젝트 Part2
2023.05.02 ~ 2023.05.16

## C# WPF 학습
- SCADA/HMI 시뮬레이션(SmartHome 시스템) 시작
	- C# WPF
	- MahApps.Metro(MetroUI 디자인 라이브러리)
	- Bogus(더미데이터 생성 라이브러리)
	- Newtonsoft.json
	- M2Mqtt(통신 라이브러리)
	- DB 데이터바인딩
	- LiveCharts
	- OxyChart
	
- SmartHome 시스템 문제점
	- 실행 후 시간이 소요되면 UI제어가 느려짐 - 텍스트의 갯수를 제한함으로써 해결
	- LiveCharts는 대용량 데이터 차트는 무리(LiveChart v.2는 동일)
	- 대용량 데이터 차트는 OxyPlot를 사용
	
- 실시간 데이터 가져오기 앱

<img src="https://raw.githubusercontent.com/Park-JuHyeon/MiniProjects/main/images/smarthome_publisher.gif"
 width = "450" />

- 스마트홈 모니터링 앱

<img src="https://raw.githubusercontent.com/Park-JuHyeon/MiniProjects/main/images/smarthome_monitor1.gif"
 width = "450" />

<img src="https://raw.githubusercontent.com/Park-JuHyeon/MiniProjects/main/images/smarthome_monitor2.png"
 width = "450" />






