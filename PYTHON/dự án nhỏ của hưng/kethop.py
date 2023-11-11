while True:


	from random import randint
	import speech_recognition

	robot_ear = speech_recognition.Recognizer()
		
	with speech_recognition.Microphone() as mic:
		print("nhập đấm, lá, hoặc kéo: ")
		audio = robot_ear.listen(mic)   

	try:
		player = robot_ear.recognize_google(audio)
	except:
		player = "vui lòng nhập lại"


	print(player)


	computer = randint(0,2)

	if computer == 0:
		computer = "đấm"
	if computer == 1:
		computer = "lá"
	if computer == 2:
		computer = "kéo"
	print("----")
	print("player choose: " + player)
	print("computer choose: " +  computer)


	if player == "hello":
		if computer == "kéo":
			print("both win")
			computer = "both win"
		if computer == "đấm":
			print("computer win")
			computer = "computer win"
		if computer == "lá":
			print("player win")
			computer = "player win"

	if player == "hi":
		if computer == "kéo":
			print("computer win")
			computer = "computer win"
		if computer == "đấm":
			print("player win")
			computer = "player win"
		if computer == "lá":
			print("both win")
			computer = "both win"

	if player == "how":
		if computer == "kéo":
			print("player win")
			computer = "player win"
		if computer == "đấm":
			print("both win")
			computer = "both win"
		if computer == "lá":
			print("computer win")
			computer = "computer win"



	if "bye" in player:
		print("tạm biệt")
		computer = "tạm biệt"
		break
		


	import pyttsx3
	computer_tai = pyttsx3.init()
	computer_tai.say(computer)
	computer_tai.runAndWait()



	









