from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

from checkers.Abyss import proxy

options = Options()
options.add_argument("--proxy-server={}".format(proxy))
driver = webdriver.Firefox(options=options)

