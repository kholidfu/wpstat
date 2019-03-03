import time
import os
import json

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


# ! GLOBAL VARS
GOOGLE_CHROME_BIN = os.environ['GOOGLE_CHROME_BIN']
CHROME_DRIVER = os.environ['CHROME_DRIVER']

options = Options()
# options.add_argument("--headless")
options.binary_location = GOOGLE_CHROME_BIN
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')


# load data from credentials.json
with open("credentials.json") as f:
    wp_data = json.loads(f.read())


def wp_get_stat(hostname, wp_username, wp_password):
    """WP Login func.
    
    Parameters
    ----------
        - hostname : str
        - wp_username : str
        - wp_password : str

    Return
    ------
        - None
    
    """
    URL = "https://wordpress.com/log-in"
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER, options=options)
    driver.get(URL)

    print("Try to logging in into WP with Selenium")
    username = driver.find_element_by_id("usernameOrEmail")
    time.sleep(5)
    username.send_keys(wp_username)
    driver.find_element_by_xpath('//*[@id="primary"]/div/main/div/div[1]/div/form/div[1]/div[2]/button').click()
    password = driver.find_element_by_id("password")
    time.sleep(3)
    password.send_keys(wp_password)
    driver.find_element_by_xpath('//*[@id="primary"]/div/main/div/div[1]/div/form/div[1]/div[2]/button').click()
    time.sleep(3)
    print("You're logged in!")
    URL = "%s/wp-admin/index.php?page=stats" % hostname
    driver.get(URL)
    print("Trying to get stats for => %s" % hostname)
    time.sleep(5)
    # * LOGOUT
    driver.find_element_by_xpath('//*[@id="wp-admin-bar-my-account"]/a').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="wp-admin-bar-user-info"]/div/form/button').click()
    time.sleep(4)
    # * QUIT BROWSER
    driver.quit()


def main():
    for i in wp_data:
        wp_get_stat(i["url"], i["username"], i["password"])


if __name__ == "__main__":
    main()