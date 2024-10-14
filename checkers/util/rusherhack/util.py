import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

#Check
url = 'https://www.rusherhack.org/users/'
check_url = "https://www.rusherhack.org/users/index.php"
bad_url = "https://www.rusherhack.org/users/login_validate.php"

#WebDriever
options = Options()
options.headless = False
driver = None

if driver is None:
    driver = webdriver.Firefox(options=options)