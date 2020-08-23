import requests 
import datetime
import sys
import time
import argparse
import os 
import colorama 
import csv  
import json 
import vk
import random
from colorama import init
from colorama import Fore, Back, Style
init(autoreset=True)
import itertools
import threading
import time
import base64
import urllib.request
from bs4 import BeautifulSoup
import socket
 
 
os.system('clear')
done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    
 
t = threading.Thread(target=animate)
t.start()
 
#long process here
time.sleep(0.8)
done = True
os.system ('clear')
os.system ('toilet PT - lub')
os.system ('toilet HackPro')
print(Fore.BLUE +Back.WHITE + 'Предстовляет: AllUtils')
print(Fore.RED + 'Выбери утилиту --> ')
print(Fore.YELLOW+"""
<-- Соц. Инжинерия -->
[1] - Deanons
<-- Утилиты для вк -->
[2] - Brute 
[3] - kingfish (Временно не работает)
<-- Hack'eram -->
[4] - spymer
[5] - DoS
[6] - http тунель (ngrok)
""")
 
os.chdir('utils')
 
while True:
    num =str(input("\033[35m\033[5m[*]"))
    if num == ('1') :
        print (Fore.GREEN + 'Запуск Info.com')
        os.system('clear')
        os.system('sh 1.sh')
    elif num == ('2'):
        print (Fore.GREEN + 'Запуск brute')
        os.system('clear')
        os.system('sh 2.sh')
    elif num == ('3'):
        print (Fore.GREEN + 'Запуск Fishing')
        os.system('clear')
        os.system('sh 3.sh')
    elif num == ('4'):
        print (Fore.GREEN + 'Запуск spymer')
        os.system('clear')
        os.system('sh 4.sh')
    elif num == ('5'):
        print(Fore.GREEN+"Запуск DoS")
        os.system('clear')
        os.system('sh 5.sh')
    elif num == ('6'):
        print(Fore.GREEN+'Запуск ngRok')
        os.system('clear')
        os.system('sh 6.sh')
 
    elif num == ('7'):
        print(Fore.GREEN + 'Запуск Cheek')
        os.system('clear')
        os.system('sh 7.sh')

        
 