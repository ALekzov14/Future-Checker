#Imports
from DrissionPage import ChromiumPage, ChromiumOptions


import time
import random

#Random
r = random.uniform

#DrissionPage
options = ChromiumOptions()
options.set_argument('--incognito')

#ChromiumPage
page = ChromiumPage(options).latest_tab

#Check
url = 'https://www.futureclient.net/forum/index.php'
check_url = "https://www.futureclient.net/forum/index.php"
bad_url = "https://www.futureclient.net/forum/member.php"


