from selenium import webdriver
#from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import JavascriptException

from time import sleep, time
import random, pickle, config, math

TAB_NUM = 1 # tab number when a new search is opened
SEARCH_WINS = 0 # number of search wins achieved

class SB:
    """The SB object logs into Swagbucks and helps you automate poll answers and search wins."""

    def __init__(self, email: str, password: str, driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))):
        """Logs into Swagbucks with your email and password from config.py using Selenium.
        
        Parameters:
            email (str): Your login email in config.py for your Swagbucks account.
            password (str): Your login password in config.py for your Swagbucks account.
        """
        self.driver = driver
        driver.maximize_window()
        # load cookies into Swagbucks if cookies.pkl is detected
        try:
            driver.get('https://www.swagbucks.com/')
            cookies = pickle.load(open('cookies.pkl', 'rb'))
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            print('Loaded cookies')
        # login into Swagbucks and save cookies to cookies.pkl for future runs of script
        except FileNotFoundError:
            print('Cookies not found. Logging in and then creating cookies...')
            self.email = email
            self.password = password
            driver.get('https://www.swagbucks.com/p/login') 
            sleep(5)
            driver.find_element('xpath', '//input[@name=\"emailAddress\"]').send_keys(email)
            sleep(2)
            driver.find_element('xpath', '//input[@name=\"password\"]').send_keys(password)
            sleep(5)
            driver.find_element('xpath', '//button[@id="loginBtn"]').click()
            sleep(15) # captcha
            pickle.dump(self.driver.get_cookies(), open('cookies.pkl', 'wb'))
            print('Saved cookies as cookies.pkl')
        finally:
            sleep(5)

    def poll(self):
        """Randomly selects a poll answer and submits your answer to earn 1 SB."""
        driver = self.driver
        driver.maximize_window()
        driver.get('https://www.swagbucks.com/polls') 
        sleep(5)
        # complete the poll
        try:
            driver.execute_script(f"document.querySelectorAll('td.pollCheckbox')[{random.randint(0,1)}].click();")
            sleep(3)
            driver.execute_script("document.getElementById('btnVote').click()")
            print('Submitted answer for poll')
            #driver.find_element(By.ID,'btnVote').click()
        except JavascriptException:
            print('Poll already completed')
        finally:
            sleep(5)

    def open_link_new_tab(self, url: str):
        """Opens URL in a new tab in chrome."""
        global TAB_NUM
        driver = self.driver
        driver.execute_script(f"window.open('{url}', 'Tab {TAB_NUM}')")
        # switch active window to the new tab
        driver.switch_to.window(driver.window_handles[TAB_NUM])
        TAB_NUM += 1

    def search(self):
        """Automates your searches and claims your search wins."""
        global SEARCH_WINS
        driver = self.driver
        driver.maximize_window()
        links = ['https://www.swagbucks.com/g/l/xcq6yq',
        'https://www.swagbucks.com/g/l/6vyye1',
        'https://www.swagbucks.com/g/l/p3btd7',
        'https://www.swagbucks.com/g/l/1j26i4']

        # two search wins
        print(f'Begin search win #{SEARCH_WINS+1}')
        for url in (x for _ in range(10) for x in links):
            # end search if bot achieved two search wins
            if SEARCH_WINS == 2:
                break
            else:
                self.open_link_new_tab(url)
                sleep(16)
                # claims sb for search win (captcha?)
                self.claimSB()

    def tearDown(self):
        """Stops your Chrome session."""
        print('Finished running bot')
        self.driver.quit()

    def claimSB(self):
        """Submits form to claim SB."""
        global SEARCH_WINS
        driver = self.driver
        try:
            driver.execute_script("document.getElementById('claimSearchWinForm').submit()")
            sleep(10)
            print('Claimed SB')
            #driver.refresh()
            sleep(10)
            print(f'End search win #{SEARCH_WINS+1}')
            SEARCH_WINS += 1
            if SEARCH_WINS != 2:
                print(f'Begin search win #{SEARCH_WINS+1}')
        except JavascriptException:
            pass

def main():
    """Main function"""
    start = time()
    swag = SB(config.EMAIL, config.PASSWORD)
    swag.poll()
    swag.search()
    swag.tearDown()
    print(f'Bot ran for: {math.floor(int(time() - start) / 60)} minutes and {int(time() - start) % 60} seconds.')

if __name__ == '__main__':
    main()