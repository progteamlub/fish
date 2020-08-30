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
print("""
／ﾌﾌ 　　　　　 　　 　ム｀ヽ
/ ノ)　　 ∧　　∧　　　　）　ヽ
/ ｜　　(´・ω ・`）ノ⌒（ゝ._,ノ
/　ﾉ⌒＿⌒ゝーく　 ＼　　／
丶＿ ノ 　　 ノ､　　|　/
　　 `ヽ `ー-‘人`ーﾉ /
　　　 丶 ￣ _人’彡ﾉ
　　　／｀ヽ _/\__'
""")
print(Fore.BLUE +Back.WHITE + 'Предстовляет: AllUtils')
print(Fore.RED + 'Выбери утилиту --> ')
print(Fore.YELLOW + """
 +-------------------------------------------------+
 | ["] Соц. Инжинерия ["]  				  
 | [1] - Deanons (Проверка инфы)
 | [*] Утилиты для вк [*]
 | [2] - Brute (Брут логина)
 | [3] - kingfish (Временно не работает) """)
print(Fore.BLUE + """
 | [§] Hack'eram [§]
 | [4] - spymer × Смс спамер ×
 | [5] - DoS × Нагрузка на сайт ×
 | [6] - http тунель × ngrok ×
 | [7] - Описания × И так все
  понятно xD × 								 
 +--------------------------------------------------+""")
print("""
 ║║ ╔═ ╔═ ╔╗ ║║ 
 ╚╣ ╠═ ╠╗ ╠╣ ╠╣ 
 ═╝ ╚═ ╚╝ ║║ ║║
 """)
print(Fore.GREEN + """
× Го 100 сабов в группе PT-Lub? ×
""")

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
        print(Fore.GREEN + '1> Пишите ключевое слово и вам выводитса иноформация \n2>Вводишь пароль и к нему подбираетса логин\n3>Фишинг вк\n4>Вводишь номер и на него отпровляетса много потоков смс\n5>Вводишь ссылку на сайт и на него идут пакеты\n6>Запуск сайта в термукс')
        time.sleep(20.0)

