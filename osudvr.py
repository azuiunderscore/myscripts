import pyautogui
import time

print("make sure you have obs open in the background, add a keybind for start and stop recording for ctrl+, and ctrl+. respectively, or edit the code yourself to make it so it uses your own binds, it should be readable enough. Then, leave your computer on with the osu! window on the home screen (the one with the giant osu logo) with nothing else on osu, like the f9 menu, for example, open.")
user = input("What player would you like to autospectate? (I think this is case sensitive but I never tested it) (lol): ")
path = "/home/azui/.local/share/osu-wine/OSU/Logs/runtime.log"
print("waiting...")
while True:
    with open(path) as f:
        for line in f:
            pass
        last_line = line
        if user in last_line:
            #time.sleep used frequently throughout to try to account for lag, this slows things down significantly, obviously, but you won't be at your computer to notice anyway if you're using this.
            time.sleep(3)
            pyautogui.keyDown("f9")
            time.sleep(1)
            pyautogui.keyUp("f9")
            #this causes issues on non 1920x1080 resolutions
            pyautogui.click(484,101)
            pyautogui.typewrite(user)
            time.sleep(4)
            #this does as well
            pyautogui.click(236, 229)
            pyautogui.typewrite("1")
            pyautogui.keyDown("ctrlleft")
            pyautogui.keyDown(",")
            pyautogui.keyUp("ctrlleft")
            pyautogui.keyUp(",")
            break
print("Player located")
        #this is actually fucking stupid, I'm stupid, Idk how control flow works, there's no way I can't just add this to the original loop but I'm, as I said before, stupid.
while True:
    with open(path) as f:
        for line in f:
            pass
        last_line = line
        if "Stopped spectating" in last_line:
            pyautogui.keyDown("ctrlleft")
            pyautogui.keyDown(".")
            pyautogui.keyUp("ctrlleft")
            pyautogui.keyUp(".")
            break
print("recording finished!")





