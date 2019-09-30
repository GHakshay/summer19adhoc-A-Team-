import pandas as pd

file = pd.read_excel('path of your excel sheet containing contact numbers')

ext = file.iloc[:, 1:2]
arrTolist = ext.values.tolist()

listTostr = str(arrTolist)[1:-1]

strContact = listTostr.replace('], [', ',').replace('[', '').replace(']', '')

finalContactList = strContact.split(",")
# print(finalContactList)

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
try:
    import autoit
except:
    pass
import time

browser: WebDriver = webdriver.Firefox(
    executable_path="path of your webdriver whether chromedriver or geckodriver(for mozilla)")
Contact = None
message = None
Link = "https://web.whatsapp.com/"
wait = None
unsaved_Contacts = None

def input_contacts():
    global unsaved_Contacts
    # List of Contacts
    unsaved_Contacts = finalContactList
    print("Taking the contact list")
    print(unsaved_Contacts)

def input_message():
    global message
    # Enter your message
    print()
    ##    message = input("Enter your message: \n")
    message = 'bot message...no need to reply'

    print(message)

def whatsapp_login():
    global wait, browser, Link
    Link = "https://web.whatsapp.com/"
    browser = webdriver.Firefox(executable_path="path of your webdriver whether chromedriver or geckodriver(for mozilla)")
    wait = WebDriverWait(browser, 6)
    browser.get(Link)
    browser.maximize_window()
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
        for i in unsaved_Contacts:
            try:
                link = 'https://api.whatsapp.com/send?phone=91' + i + '&text=&source=&data='
                browser.get(link)
                time.sleep(2)
                browser.find_element_by_xpath('//*[@id="action-button"]').click()
                # browser.find_element_by_xpath('//*[@class="action__link"]').click()
                time.sleep(1)
                browser.find_element_by_class_name('action__link').click()
                time.sleep(2)
                print("Sending message to", i)
                send_unsaved_contact_message()
                time.sleep(3)
            except NoSuchElementException:
                contacts_with_error = []
                lt = contacts_with_error.append(i)
                print(lt)
                print('not sent')

if __name__ == "__main__":
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
