import os
import time

def setup():
    print("""
    ███████╗██╗   ██╗████████╗██╗   ██╗██████╗ ███████╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗
    ██╔════╝██║   ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
    █████╗  ██║   ██║   ██║   ██║   ██║██████╔╝█████╗      ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
    ██╔══╝  ██║   ██║   ██║   ██║   ██║██╔══██╗██╔══╝      ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
    ██║     ╚██████╔╝   ██║   ╚██████╔╝██║  ██║███████╗    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
    ╚═╝      ╚═════╝    ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
    
[!] Name        : Future Team Checker
[!] Version     : beta 1.2.1 

    """)
    time.sleep(0.15)

    print('....Loading....')
    s = '█'
    for i in range(101):
        time.sleep(0.06)
        print('\r', i * s, str(i), '%', end='')

    print("\n")
    print("Our Products:")
    print('[1] Future checker')
    time.sleep(0.40)
    print('[2] RusherHack checker')
    time.sleep(0.40)
    print('[4] Future sorter')
    time.sleep(0.40)
    print('[5] Rusherhack sorter\n')

    write = int(input('>>> '))

    if write == 1:  # Future checker
        os.system('python Future.py')
    if write == 2:  # RusherHack checker
        os.system('python RusherHack.py')
    if write == 3:  # Future sorter
        os.system('python ../sorter/sorter_future.py')
    if write == 4:  # Rusherhack sorter
        os.system('python ../sorter/sorter_rusherhack.py')

setup()