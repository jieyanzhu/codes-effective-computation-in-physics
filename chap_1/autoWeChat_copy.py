# Use this file to send WeChat messages automatically
import time
import pyautogui
import os
import random
import pyperclip
import schedule

def job():
    # Input 'double' for doubleclick and 'single' for singleclick (case sensitive)
    def mapping_image(image, click):
        box_location = pyautogui.locateOnScreen(image)
        if box_location == None:
            print('ERROR: No such image is found!')
            quit()
        else:
            center = pyautogui.center(box_location)
            center = pyautogui.Point(center.x, center.y-40)
            if click == 'double':
                pyautogui.doubleClick(center)
            elif click == 'single':
                pyautogui.leftClick(center)
            else:
                print('ERROR: Undefined command for click!')
            time.sleep(1)

    # Copy and paste your input
    def read_text(text):
        pyperclip.copy(text)
        pyautogui.hotkey('command', 'v')

    # Search for the user you want to chat with
    def locate_user(username):
        mapping_image('search.png', 'single')
        read_text(username)
        time.sleep(1)
        pyautogui.moveRel(xOffset=0, yOffset=85)
        pyautogui.click()
        time.sleep(1)

    # Get a random body temperature between 36 to 37 degree Celsius
    def rand_temp():
        return str(round(random.random()+36, 1))
	
    def main():
        # Get rid of screensaver
        pyautogui.click()
        time.sleep(1)
        os.chdir('/Users/jieyanzhu/Desktop/wechat')
        # Search for the user you want to chat with
        locate_user('迎宾桥') # Replace the argument with the person you want to chat with
        # Start chatting!
        pyautogui.typewrite(rand_temp())
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)

    main()

# Modify the schedule statements to meet your requirement
schedule.every().day.at("08:45").until("2021-08-01 12:00").do(job)
schedule.every().day.at("14:45").until("2021-08-01 12:00").do(job)

# Execute existing schedules
while True:
    schedule.run_pending()
    if schedule.get_jobs() == []:
        break
    time.sleep(60)
