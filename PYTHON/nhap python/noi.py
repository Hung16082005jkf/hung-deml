
while True:


	import speech_recognition
	from datetime import date, datetime

	robot_ear = speech_recognition.Recognizer()
	
	with speech_recognition.Microphone() as mic:
		print("robot: I'm Listening")
		audio = robot_ear.listen(mic)

	try:
		you = robot_ear.recognize_google(audio)
	except:
		you = "anhyeuem"
	print(you)

	from datetime import date, datetime
	if you == "":
		naruto = "i love you khachung"
	elif you == "hello":
		naruto = "hello hung"
	elif you == "today":
		today = date.today()
		naruto = today.strftime("%B %d, %Y")
	elif "president" in you:
		naruto = "nguyen xuan phuc"
	elif "time" in you:
		now = datetime.now()
		naruto = now.strftime("%H hours %M minutes %S seconds")
	elif "bye" in you:
		naruto = "bye khachung"
		break	
	else:
		naruto = "i go to sleeps"

		print("nguyenthihanh: " + naruto)

		
		import pyttsx
		naruto_mouth = pyttsx3.init()
		naruto_mouth.say(naruto)
		naruto_mouth.runAndWait()






	




