


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
		you = "i very love vivian"


	print("anhyeu: " + you)



	if you == "hello":
		robot = "hello hung"
	elif "":
		robot = "vivian want to make love with hung"
	elif "today" in you:
		today = date.today()
		robot = today.strftime("%B %d, %Y")
	elif "time" in you:
		now = datetime.now()
		robot = now.strftime("%H hours %M minutes %S seconds")
	elif you == "what are you doing":
		robot = "tôi đang nõi chuyện với bạn"
	elif "home" in you:
		robot = "have vivian"
	elif "bye" in you:
		robot = "bye anhyeu"
		break
	elif "make love" in you:
		robot = "i love you baybe"
	elif "president" in you:
		robot = "nguyễn xuân phúc"
	else:
		robot = "vivian want to make love with hung"

	print("vivian love: " + robot)
	import pyttsx3
	robot_ear = pyttsx3.init()
	robot_ear.say(robot)
	robot_ear.runAndWait()




	





	