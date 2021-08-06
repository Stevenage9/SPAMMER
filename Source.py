import pyautogui
import webbrowser
import time
import keyboard

message = input("Text to be spammed(type enter if you want to spam clipboard)=>")

choice = 0
while not(choice == 1 or choice == 2):
    choice = int(input("Enter 1 to specify number of messages or 2 for unlimited messages: "))

    if not(choice == 1 or choice == 2):
        print("Please enter either 1 or 2 to select a mode")

ask = str(input("Before you begin, would you like to visit my youtube channel?(y/n)=>"))

if ask == "y":
    url = "https://www.youtube.com/channel/UCXUlNlQpwUV8cCMK8T_spRQ/"
    webbrowser.open_new(url)


if choice == 1:
    repeats = int(input("Number of times spammed=>"))
    delay = int(input("Delay between each message in miliseconds=>"))
	
    print("Open up your messaging app, please")
    isLoaded = input("Press Enter when the app is loaded up.")

    print("There is a 10 second cooldown for you to switch to the text input of the messaging app")

    time.sleep(10)

    for i in range(0, repeats):
        if message != "":
            pyautogui.typewrite(message)
            pyautogui.press("enter")
        else:
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press("enter")

        time.sleep(delay/1000)

    final = input(
        "Worked like a charm. Have a good day! (press enter to close this window)")

elif choice == 2:
    flag = True

    def stop_spammer():
        global flag
        flag = False

    delay = int(input("Delay between each message in miliseconds=>"))
    print("This mode of spammer runs forever. Remember, to stop spamming, press Ctrl+Shift+W and the program will stop!")
    print("Open up your messaging app, please")
    isLoaded = input("Press Enter when the app is loaded up.")

    print("There is a 10 second cooldown for you to switch to the text input of the messaging app")

    time.sleep(10)

    keyboard.add_hotkey('ctrl+shift+w', stop_spammer)

    while True:
	    if flag:
		    if message != "":
			    pyautogui.typewrite(message)
			    pyautogui.press("enter")
		    else:
			    pyautogui.hotkey('ctrl', 'v')
			    pyautogui.press("enter")
		    time.sleep(delay/1000)
	    else:
		    break
	
    final = input("Worked like a charm. Have a good day! (press enter to close this window)")
