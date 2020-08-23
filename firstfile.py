import os
import pyttsx3

pyttsx3.speak("Welcome to my text to open application programme")

while True:
	p=input("Please write which application you want open:")
	
	if (("don't" in p) | ("donot" in p) | ("dont" in p)  ):
		pyttsx3.speak("Your app will not open")

	elif  (("chrome" in p) or("my browser" in p) or ("default browser" in p)  ) and (("run" in p) or ("execute" in p) or ("start" in p) or ("open" in p) or ("begin" in p)) : 
		pyttsx3.speak("your application is open")
		os.system("chrome")

	elif (("notepad" in p) or ("texteditor" in p) or ("editor" in p) ) and (("run" in p) or ("execute" in p) or ("start" in p) or ("open" in p) or ("begin" in p)) : 
		pyttsx3.speak("your application is open")
		os.system("notepad")

	
	elif(("outlook" in p) or ("defaultmail" in p)) and (("run" in p) or ("execute" in p) or ("start" in p) or ("open" in p) or ("begin" in p)) : 
		pyttsx3.speak("your application is open")
		os.system("outlook")
	
	elif(("putty" in p) or ("ssh client" in p)) and (("run" in p) or ("execute" in p) or ("start" in p) or ("open" in p) or ("begin" in p)) : 
		pyttsx3.speak("your application is open")
		os.system("putty")
	
	elif(("vlc" in p) or ("player" in p)) and (("run" in p) or ("execute" in p) or ("start" in p) or ("open" in p) or ("begin" in p)) : 
		pyttsx3.speak("your application is open")
		os.system("vlc")

	
	elif (("microsoftedge" in p) or ("microedge") or ("windowbrowser" in p) ) and (("run" in p) or ("execute" in p) or ("start" in p) or ("open" in p) or ("begin" in p)) :  
		pyttsx3.speak("your application is open")
		os.system("microsoftedge")

	elif (("cmd" in p) or ("command prompt") or ("myshell" in p) or ("shell" in p) or ("commandline" in p)) and (("run" in p) or ("execute" in p) or ("start" in p) or ("open" in p) or ("begin" in p)) :  
		pyttsx3.speak("your application is open")
		os.system("cmd")
	
	
	elif ("exit" in p) or ("stop" in p) or ("terminate" in p):
		break;	
	
	else:
		print("Not valid input")





      
