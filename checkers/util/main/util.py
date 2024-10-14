import random

import colorama
from colorama import Fore, Back, Style
import time
proxy_file = '../proxies.txt'

#Gradient
colorama.init(autoreset=True)

def gradient_text(text):
 colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
 for i in range(len(text)):
  print(colors[i % len(colors)] + text[i], end='', flush=True)
  # time.sleep(0.05)
def gradient_text2(text2):
 colors2 = [Fore.BLUE, Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.CYAN, Fore.GREEN, Fore.LIGHTGREEN_EX]
 for z in range(len(text2)):
  print(colors2[z % len(colors2)] + text2[z], end='', flush=True)
  time.sleep(0.05)

#Random
r = random.uniform
r_0_1_0_2 = r(0.1,0.2)
r_0_2_0_3 = r(0.2,0.3)
r_0_3_0_4 = r(0.3,0.4)
r_0_4_0_5 = r(0.4,0.6)
r_0_5_0_6 = r(0.5,0.6)
r_0_6_0_7 = r(0.6,0.7)
r_0_7_0_8 = r(0.7,0.8)
r_0_8_0_9 = r(0.8,0.9)
r_0_9_1 = r(0.9,1)
r_1_1_1 = r(1,1.1)