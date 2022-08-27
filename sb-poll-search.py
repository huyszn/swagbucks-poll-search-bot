"""MIT License

Copyright (c) 2022 Huy Mai

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
import random, pickle, config


class SB:
    """The SB object logs into Swagbucks and helps you automate poll answers and search wins."""

    def __init__(self, email, password, driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))):
        """Logs into Swagbucks with your email and password from config.py using Selenium.
        
        Parameters:
            email (str): Your login email in config.py for your Swagbucks account.
            password (str): Your login password in config.py for your Swagbucks account.
        """
        self.driver = driver
        try: # load cookies into Swagbucks if cookies.pkl is detected
            driver.get('https://www.swagbucks.com/') 
            cookies = pickle.load(open('cookies.pkl', 'rb'))
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            sleep(5)
        except: # login into Swagbucks and save cookies to cookies.pkl for future runs of script
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
            sleep(5)

    def poll(self):
        """Randomly selects a poll answer and submits your answer to earn 1 SB."""
        driver = self.driver
        driver.get('https://www.swagbucks.com/polls') 
        sleep(5)
        driver.execute_script(f"document.querySelectorAll('td.pollCheckbox')[{random.randint(0,1)}].click();")
        sleep(3)
        #driver.execute_script("document.getElementById('btnVote').click()")
        driver.find_element(By.ID,'btnVote').click()
        sleep(5)

    def search(self):
        """Automates your searches and claims your search wins."""
        driver = self.driver
        links = ['https://www.swagbucks.com/g/l/xcq6yq',
        'https://www.swagbucks.com/g/l/6vyye1',
        'https://www.swagbucks.com/g/l/p3btd7',
        'https://www.swagbucks.com/g/l/1j26i4']

        # first search win
        print('Begin first search win')
        for url in links:
            driver.get(url)
            # claims sb for the first search win (captcha?)
            if url == links[3]:
                sleep(10)
                driver.execute_script("document.getElementById('claimSearchWinForm').submit()")
            sleep(16)
        print('End first search win')
        
        # second search win
        print('Begin second search win')
        for url in (x for _ in range(8) for x in links):
            driver.get(url)
            sleep(16)
        
        driver.get(random.choice(links))
        sleep(10)
        # claims sb for the second search win (captcha?)
        driver.execute_script("document.getElementById('claimSearchWinForm').submit()")
        print('End second search win')
        sleep(30)

    def tearDown(self):
        """Stops your Chrome session."""
        self.driver.quit()


if __name__ == '__main__':
    swag = SB(config.EMAIL, config.PASSWORD)
    swag.poll()
    swag.search()
    swag.tearDown()