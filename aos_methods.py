import sys
import datetime
from selenium.common.exceptions import NoSuchElementException
import aos_locators as locators
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)


# Fixture method - to open web browser
def setUp():
    # Make a full screen
    driver.maximize_window()
    # Let's wait for the browser response in general
    driver.implicitly_wait(30)
    # navigating to the advantageonlineshopping website
    driver.get(locators.aos_url)
    # Checking that we're on the correct URL address and we're seeing correct title
    if driver.current_url == locators.aos_url and driver.title == ' Advantage Shopping':
        print(f'We\'re at homepage -- {driver.current_url}')
        print(f'We\'re seeing title message -- {driver.title}')
    else:
        print(f'We\'re not at the homepage. Check your code!')
        #driver.close()
        #driver.quit()

def tearDown():
    if driver is not None:
        print(f'-------------------')
        print(f'Hurray.Test is done successfully')
        print(f'Test Completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()

    else:
        print(f'unable to close and quit')

def validate_homepage_texts_links():
    if driver.current_url == locators.aos_url:
        if driver.find_element(By.ID, 'speakersTxt').text == "SPEAKERS":
            print(f'Speakers text is displayed')
        else:
            print(f'Speakers text is not  displayed')
            sleep(2)

        if driver.find_element(By.ID, 'tabletsTxt').text == "TABLETS":
            print(f'Tablets text is displayed')
        else:
            print(f'Tablets text is not displayed')
            sleep(2)

        if driver.find_element(By.ID, 'headphonesTxt').text == "HEADPHONES":
            print(f'Headphones text is displayed')
        else:
            print(f'Headphones text is not displayed')
            sleep(2)

        if driver.find_element(By.ID, 'laptopsTxt').text == "LAPTOPS":
            print(f'Laptops text is displayed')
        else:
            print(f'Laptops text is not displayed')
            sleep(2)

        if driver.find_element(By.ID, 'miceTxt').text == "MICE":
            print(f'Mice title is displayed')
        else:
            print(f'Mice title is not displayed')
            sleep (2)

        try:
            driver.find_element(By.XPATH, "//a[text() = 'SPECIAL OFFER']").click()
            sleep(2)
            print(f'Special offer link is clickable')
        except WebDriverException:
            print(f'unable to click')
        try:
            driver.find_element(By.XPATH, "//a[text() = 'POPULAR ITEMS']").click()
            sleep(2)
            print(f'Popular item link is clickable')
        except WebDriverException:
            print(f'unable to click')
        try:
            driver.find_element(By.XPATH, "//a[text() = 'CONTACT US']").click()
            sleep(2)
            print(f'Contact us link is clickable')
        except WebDriverException:
            print(f'unable to click')

    if driver.current_url == 'https://advantageonlineshopping.com/#/':
        Select(driver.find_element(By.NAME, 'categoryListboxContactUs')).select_by_visible_text('Laptops')
        sleep(1)
        Select(driver.find_element(By.NAME, 'productListboxContactUs')).select_by_visible_text('HP Chromebook 14 G1(ES)')
        sleep(1)
        driver.find_element(By.XPATH, "//input[@name= 'emailContactUs']").send_keys(locators.email)
        sleep(1)
        driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys('this is a test')
        sleep(1)
        driver.find_element(By.ID, 'send_btnundefined').click()
        sleep(1)
    #if driver.find_element(By.XPATH, "//*[@id='registerSuccessCover']/div/p']").text == 'Thank you for contacting Advantage support':

    if driver.find_element(By.XPATH, '//p[contains(text(), "Thank you for contacting Advantage support")]'):
        print(f'Thank you message for contact form is displayed')

        try:
            driver.find_element(By.XPATH, "//a[text() = ' CONTINUE SHOPPING ']").click()
            sleep(3)
            print(f'Continue Shopping link is clickable')
        except WebDriverException:
            print(f'unable to click')
            sleep(3)

    try:
        sitelogo = driver.find_element(By.CLASS_NAME, 'logo')
        if sitelogo.is_displayed():
            print('Logo is displayed')

        sleep(3)
    except WebDriverException as ex:
        print(ex.msg)

    try:
        facebookLink = driver.find_element(By.NAME, 'follow_facebook')
        if facebookLink.is_displayed():
            print('Facebook link is displayed')
            facebookLink.click()

        sleep(3)
        print(f'Facebook link is clickable')
    except WebDriverException as ex:
        print(ex.msg)

    try:
        twitterLink = driver.find_element(By.NAME, 'follow_twitter')
        if twitterLink.is_displayed():
            print('Twitter link is displayed')
            twitterLink.click()

        sleep(3)
        print(f'Twitter link is clickable')
    except WebDriverException as ex:
        print(ex.msg)

    try:
        linkedinLink = driver.find_element(By.NAME, 'follow_linkedin')
        if linkedinLink.is_displayed():
            print('Linkedin link is displayed')
            linkedinLink.click()

        sleep(3)
        print(f'Linkedin link is clickable')
    except WebDriverException as ex:
        print(ex.msg)

    #bb = driver.find_element(By.TAG_NAME, 'body')
    #print(bb)
    #bb.send_keys(Keys.COMMAND + 'W')
    driver.switch_to.window(driver.window_handles[3])
    driver.close()
    sleep(1)
    driver.switch_to.window(driver.window_handles[2])
    driver.close()
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    driver.close()
    sleep(1)
    driver.switch_to.window(driver.window_handles[0])
    sleep(1)


#setUp()
#validate_homepage_texts_links()
#tearDown()




