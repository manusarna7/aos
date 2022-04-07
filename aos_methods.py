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
        print(f'--------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()
    else:
        print(f'unable to close and quit')

def create_new_account():
    if driver.current_url == locators.aos_url:
       driver.find_element(By.ID, 'menuUser').click()
       sleep(3)
       driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
       sleep(3)
       if driver.current_url == 'https://advantageonlineshopping.com/#/register': #or driver.title == '&nbsp;Advantage Shopping':
            #driver.find_element(By.XPATH, '//*[@id="formCover"]/sec-view/div/input').send_keys(locators.new_username)
            driver.find_element(By.XPATH, "//input[@name= 'usernameRegisterPage']").send_keys(locators.new_username)
            sleep(0.25)
            driver.find_element(By.XPATH, "//input[@name= 'emailRegisterPage']").send_keys(locators.email)
            sleep(0.25)
            driver.find_element(By.XPATH, "//input[@name= 'passwordRegisterPage']").send_keys(locators.new_password)
            sleep(0.25)
            driver.find_element(By.XPATH, "//input[@name= 'confirm_passwordRegisterPage']").send_keys(locators.new_password)
            sleep(0.25)
            driver.find_element(By.XPATH, "//input[@name= 'first_nameRegisterPage']").send_keys(locators.firstname)
            sleep(0.25)
            driver.find_element(By.XPATH, "//input[@name= 'last_nameRegisterPage']").send_keys(locators.lastname)
            sleep(0.25)
            driver.find_element(By.XPATH, "//input[@name= 'phone_numberRegisterPage']").send_keys(locators.phone)
            sleep(0.25)
            Select(driver.find_element(By.XPATH, '//*[@id="formCover"]/div[3]/div[1]/sec-view[1]/div/select')).select_by_visible_text('Canada')
            sleep(0.25)
            driver.find_element(By.XPATH, "//input[@name= 'cityRegisterPage']").send_keys(locators.city)
            sleep(0.25)
            driver.find_element(By.XPATH, "//input[@name= 'addressRegisterPage']").send_keys(locators.address)
            sleep(0.25)
            driver.find_element(By.XPATH, "//input[@name= 'state_/_province_/_regionRegisterPage']").send_keys(locators.province)
            sleep(0.25)
            driver.find_element(By.XPATH, "//input[@name= 'postal_codeRegisterPage']").send_keys(locators.postal_code)
            sleep(0.25)
            driver.find_element(By.XPATH, '//*[@id="formCover"]/sec-view/div/input').click()
            sleep(0.25)
            driver.find_element(By.XPATH, '//*[@id="registerPage"]/article/sec-form/div[2]/sec-sender').click()
            sleep(5)

def validate_new_account():
        if driver.current_url == locators.aos_url:
            sleep(1)
            print(f'new account created successfully with username :{locators.new_username}')

            sleep(1)
        else:
            print(f'new account not created successfully. please verify all the required fields (*) are completed')


def log_out():
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[3]').click()
    sleep(1)
    if driver.current_url == locators.aos_url:
        print(f'logged out successfully at :{datetime.datetime.now()}')
        sleep(1)
    else:
        print(f' not able to logged out.something went wrong')

def log_in():
    if driver.current_url == locators.aos_url:
        driver.find_element(By.ID, 'menuUser').click()
        sleep(3)
        driver.find_element(By.XPATH, '/html/body/login-modal/div/div/div[3]/sec-form/sec-view[1]/div/input').send_keys(locators.new_username)
        sleep(3)
        driver.find_element(By.XPATH, '/html/body/login-modal/div/div/div[3]/sec-form/sec-view[2]/div/input').send_keys(locators.new_password)
        sleep(3)
        driver.find_element(By.ID, 'sign_in_btnundefined').click()
        print(f'logged in successfully to the New account with username: {locators.new_username}')
        sleep(10)


setUp()
create_new_account()
validate_new_account()
log_out()
log_in()
log_out()
tearDown()




