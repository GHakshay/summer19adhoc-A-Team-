import pandas as pd
import re
file=pd.read_excel("akshat.xlsx")


file['1']=file.iloc[:,:].apply(lambda x:' '.join(x.astype(str)), axis=1)

file['contact'] = file['1'].str.extract('(\d\d\d\d\d\d\d\d\d\d)', expand=True)

print(file['contact'])

arrTolist=file['contact'].values.tolist()
print(arrTolist)


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time

browser=None
Contact = None
from __main__ import input
message = input
Link = "https://web.whatsapp.com/"
wait = None
unsaved_Contacts = None

def input_contacts():
    global unsaved_Contacts
    # List of Contacts
    unsaved_Contacts = arrTolist
    print("Taking the contact list")
    print(unsaved_Contacts)

def input_message():
    global message
    # Enter your message
    print()
    ##    message = input("Enter your message: \n")

    #message =input

    print(message)

def whatsapp_login():
    global wait, browser, Link
##    Link = "https://web.whatsapp.com/"
    browser = webdriver.Firefox(executable_path="geckodriver.exe")
##    wait = WebDriverWait(browser, 6)
##    browser.get(Link)
##    browser.maximize_window()
    print("QR scanned")

def send_unsaved_contact_message():
    global message, unsaved_Contacts
    contacts_with_error = []
    try:
        time.sleep(13)
        input_box = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        for ch in message:
            if ch == "\n":
                ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(
                    Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
            else:
                input_box.send_keys(ch)
        input_box.send_keys(Keys.ENTER)
        print("Message sent successfuly")

    except NoSuchElementException:
        # if browser.find_elements_by_xpath('//*[@id="pane-side"]'):  # _1c8mz _1RYPC
        # contacts_with_error.append(unsaved_Contacts)
        # print(unsaved_Contacts + "is not valid")
        print("Failed to send message")
    return

def sender():
    global unsaved_Contacts
    if len(unsaved_Contacts) > 0:
##        browser = webdriver.Firefox(executable_path="geckodriver.exe")
        for i in unsaved_Contacts:
            try:
                link = 'https://api.whatsapp.com/send?phone=91' + i + '&text=&source=&data='
                browser.get(link)
                time.sleep(2)
                browser.find_element_by_xpath('//*[@id="action-button"]').click()
                time.sleep(1)
                browser.find_element_by_class_name('action__link').click()
                time.sleep(2)
                print("Sending message to", i)
                send_unsaved_contact_message()
                time.sleep(3)
            except:
                contacts_with_error = []
                lt = contacts_with_error.append(i)
                print(lt)
                print('not sent')

#if __name__ == "__main__":
print("Start")

# Taking contact list as input to send messages
input_contacts()
# Enter the message you want to send
input_message()

# Let us login and Scan
print("SCAN YOUR QR CODE FOR WHATSAPP WEB")
whatsapp_login()

# Send message to all Contact List
sender()

# message sending Task Complete    #     print("Task Completed")
