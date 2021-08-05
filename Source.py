import pyautogui
import webbrowser
import time

message = input("Text to be spammed(type enter if you want to spam clipboard)→")
repeats = int(input("Number of times spammed→"))
delay = int(input("Delay between each message in miliseconds→"))

ask= str (input("Before you begin, would you like to visit my youtube channel?(y/n)→"))

if ask == "y":
	url="https://www.youtube.com/channel/UCXUlNlQpwUV8cCMK8T_spRQ/"
	webbrowser.open_new(url)

print("Okay, now lets continue with the process. Open up your messaging app, please")

isLoaded = input("Press Enter when the app is loaded up.")

print("There is an 8 second cooldown for you to switch to the text input of the messaging app")

time.sleep(8)


for i in range(0,repeats):
	if message != "":
		pyautogui.typewrite(message)     
		pyautogui.press("enter")
	else:	
		pyautogui.hotkey('ctrl', 'v')      
		pyautogui.press("enter")

	time.sleep(delay/1000)

final = input("Worked like a charm. Have a good day! (press enter to close this window)")