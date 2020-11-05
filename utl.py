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
""")

while True:
    os.system ('clear')
	print(Fore.BLUE +Back.WHITE + 'Предстовляет: AllUtils')
	print(Fore.RED + 'Выбери утилиту --> ')
	print(Fore.YELLOW + """

 | ["] Соц. Инжинерия ["]  				  
 | [1] - Deanons (Проверка инфы)
 | [*] Утилиты для вк [*]
 | [2] - Brute (Брут логина)
 | [3] - master fish (Фишинг вк) """)
	print(Fore.BLUE + """
 | [§] Hack'eram [§]
 | [4] - spymer × Смс спамер ×
 | [5] - DoS × Нагрузка на сайт ×
 | [6] - http тунель × ngrok ×
 | [7] - """ + Fore.RED + """YouTube""" + Fore.BLUE + """× Накрутка просмотров на стрим × """ + Fore.GREEN + """
 | [8] - Vk-HACK × И так все понятно ×
 | [9] - OS-Termux ×В разработке×
 | [07] - Описания """)
	print(Fore.RED +
 """║║ ╔═ ╔═ ╔╗ ║║ """ + Fore.GREEN +
""" ╚╣ ╠═ ╠╗ ╠╣ ╠╣ """ + Fore.BLUE +
 """═╝ ╚═ ╚╝ ║║ ║║
 """)
	print(Fore.BLUE + """
× Го 200 сабов в группе ? ×""")
    num =str(input("\033[35m\033[5m[*]"))
    if num == ('1') :
        print (Fore.GREEN + 'Запуск Info.com')
        os.system('clear')
        os.system('cd ~')
		os.system('cd shek')
		os.system('python skek.py')
    elif num == ('2'):
        print (Fore.GREEN + 'Запуск brute')
        os.system('clear')
        os.system('cd ~')
        os.system('cd brut')
        os.system('sh vtins.sh')
    elif num == ('3'):
        print (Fore.GREEN + 'Запуск Fishing')
        os.system('clear')
        os.system('cd ~')
        os.system('cd mfisher')
        os.system('python fsh.py')
    elif num == ('4'):
        print (Fore.GREEN + 'Запуск spymer')
        os.system('clear')
        os.system('cd ~ ')
        os.system('cd spam ')
        os.system('sh install.sh ')
        os.system('python spammer.py ')
    elif num == ('5'):
        print(Fore.GREEN+"Запуск DoS")
        
        os.system('clear')
        os.system('cd ~ ')
        os.system('cd DoS ')
        os.system('sh install.sh')
    elif num == ('6'):
        print(Fore.GREEN+'Запуск ngRok')
        os.system('clear')
        os.system('sh 6.sh')
 
    elif num == ('7'):
        print(Fore.GREEN+'Запуск YT')
        os.system('clear')
        os.system('cd ~ ')
        os.system('cd YouTube ')
        os.system('python yt.py')
        
    
    elif num == ('8'):
        print(Fore.GREEN+'Запуск VK')
        os.system('clear')
        os.system('cd ~ ')
        os.system('cd vkhack ')
        os.system('python vkhack.py')
	
    elif num == ('9'):
        print(Fore.GREEN+'Запуск OS')
        os.system('clear')
        os.system('cd ~ ')
        os.system('cd termuxOS ')
        os.system('python os.py')
    elif num == ('07'):
        print(Fore.GREEN + """
[1] Пишите ключевое слово и вам выводитса иноформация
[2] Вводишь пароль и к нему подбираетса логин
[3] Фишинг вк (В разработке сейчас БЕТА ТЕСТ)
[4] Вводишь номер и на него отпровляетса много потоков смс
[5]Вводишь ссылку на сайт и на него идут пакеты
[6] Запуск сайта в термукс

Вас перенесет в главное меню через 20 секунд!""")
        time.sleep(20.0)

