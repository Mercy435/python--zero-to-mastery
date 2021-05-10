from selenium import webdriver

# creating an instance of the chrome browser
chrome_browser = webdriver.Chrome('./chromedriver.exe')
# print(chrome_browser)
# chrome_browser.maximize_window()
# chrome_browser.minimize_window()

chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')  # to go to this url
# go to inspect, to copy an html text title
# print('Selenium Easy Demo - Simple Form to Automate using Selenium' in chrome_browser.title)  # gives true

# assert is used to search for sth,, if present, it doesnt return an error
assert 'Selenium Easy Demo' in chrome_browser.title  # gives true

# go to the html page and look for a class name, id or sth u can find by
show_message_button = chrome_browser.find_element_by_class_name('btn-default')
print(show_message_button.get_attribute('innerHTML'))  # prints text show message

assert 'Show Message' in chrome_browser.page_source  # page source is the html of the entire

# go to the html page to see the id
user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()  # clear what is there
user_message.send_keys('I AM EXTRA COOL')  # to send this to the message/ type as though someone is typing

# to simulate a click
show_message_button.click()

# to display output message
output_message = chrome_browser.find_element_by_id('display')
assert 'I AM EXTRA COOL' in output_message.text
print(output_message.get_attribute('innerHTML'))

# using css selector, go the html and grab the css id
user_button2 = chrome_browser.find_element_by_css_selector('#get-input > .btn')  # for parent and all children buttons
print(user_button2)

chrome_browser.close()  # closes the immediate one that is open
chrome_browser.quit()  # closes entire browser

# automation can be used for messages, bots .....
# use wait or pauses to delete automation cos websites can detect human or robot due to the speed in carrying out
# commands