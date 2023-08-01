

#imports


import pymem ,pymem.process ,keyboard ,re ,os ,webbrowser ,cryptocode ,requests ,time #main
from rich.console import Console; from threading import Thread; from math import pi
from datetime import datetime as dt; from tkinter import messagebox
import getpass ,configparser;getpass.getuser();from math import *



licenseDateCheck = 'https://raw.githubusercontent.com/SL1dee36/nesoftware/main/exports00001.json'  #exports00001.json переименовать и создать для разных пользователей
DateResponse = requests.get(licenseDateCheck).json()

#Year/mounth/day################################################################
current_datetime = dt.now()
year = int(DateResponse["signatures"]["year"])
mounth = int(DateResponse["signatures"]["mounth"])
day = int(DateResponse["signatures"]["day"])
hour = int(DateResponse["signatures"]["hour"])
minutes = int(DateResponse["signatures"]["minutes"])

DataL = dt(year,mounth,day, hour, minutes)
################################################################################


# < Получаем оффсеты >
offsets = 'https://raw.githubusercontent.com/SL1dee36/nesoftware/main/ecsgo.json'
response = requests.get(offsets).json()

dwLocalPlayer = int(response["signatures"]["dwLocalPlayer"])
dwForceJump = int(response["signatures"]["dwForceJump"])
m_fFlags = int(response["netvars"]["m_fFlags"])


from time import sleep;from os import system as s;from ctypes import windll as w
w.kernel32.SetConsoleTitleA(b"NE.software >5D2I<");s("mode con cols=65 lines=20")

console=Console()

autoStart = 0    
bhopSpeed = 0.012

code = 0

cols=0

WHILE=True

try:
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read('C:/Users/{}/AppData/Roaming/settings.ini'.format(getpass.getuser()))  # читаем конфиг

    username  = (config["ACCOUNT"]["username"])  # обращаемся как к обычному словарю!
    password  = (config["ACCOUNT"]["password"])
    token     = (config["ACCOUNT"]["token"])
    scode     = (config["ACCOUNT"]["scode"])
    acon      = (config["ACCOUNT"]["acon"])

    config2 = configparser.ConfigParser()  # создаём объекта парсера
    config2.read('C:/Users/{}/AppData/Roaming/configs.ini'.format(getpass.getuser()))  # читаем конфиг

    bind_wh   = (config2["BIND"]["WH"])  #ЧЕКАЕМ БИНДЫ
    bind_rh   = (config2["BIND"]["RH"])
    bind_en   = (config2["BIND"]["EN"])
    bind_qd   = (config2["BIND"]["QD"])
    bind_rcs  = (config2["BIND"]["RCS"])  #RCS Добавить

    bind_menu = (config2["BIND"]["Menu"])
    bind_bhop = (config2["BIND"]["BHOP"])
    bhop_speed = (float(config2["MISC"]["BhopSpeed"]))
    bhop_loop = (config2["BIND"]["Bhopmode"])
    space_button = (config2["MISC"]["BhopButton"])

    if acon == 'True':
        WHILE = False

    while WHILE:
                logining = input("\n\n\n   [+] Обнаружена учётная запись: {}\n   [?] Пожалуйста введите пинкод: ".format(username))
                if logining == cryptocode.decrypt(scode,password):
                    print("   [+] Вход выполнен...")
                    acon1 = input("     [+] Входить автоматически? \n    [?] y/n:   ")
                    acon = True
                    config = configparser.ConfigParser()
                    config['ACCOUNT'] = {'username': username,
                                        'password': password,
                                        'token': token,
                                        'scode': scode,
                                        'acon' : acon}
                    with open('C:/Users/{}/AppData/Roaming/settings.ini'.format(getpass.getuser()), 'w') as configfile:
                        config.write(configfile)
                    WHILE = False
                else:
                    s("cls")
                    if cols>=4:
                        print("   [!] Пароль введён неверно более 3 раз!");sleep(3)
                        break
                    cols+=1
                    print("   [@] Пинкод введён неверно! {} раз.\n".format(cols))


except:
        username = input("\n\n\n   [+] Введите желаемое Имя: ")
        password = input("   [+] Придумайте пароль: ")
        
        s("cls")
        secretcode = (input("\n\n\n   [?] {} придумайте PINcode: ".format(username)))
        acon = False
        token = (hash(secretcode))*pi
        scode = cryptocode.encrypt(secretcode,password)


        config = configparser.ConfigParser()
        config['ACCOUNT'] = {'username': username,
                             'password': password,
                             'token': token,
                             'scode': scode,
                             'acon' : acon}
        
        with open('C:/Users/{}/AppData/Roaming/settings.ini'.format(getpass.getuser()), 'w') as configfile:
            config.write(configfile)
        
        bind_menu = 'home'
        bind_bhop = 'F9'
        bind_en =   'F7'
        bind_qd =   'F8'
        bind_rh =   'F5'
        bind_wh =   'F6'
        bind_rcs =  'F11'
        bhop_speed = 0.015
        bhop_loop = 'legit'
        space_button = 'space'
        bhpinf = 'Чем ниже BhopSpeed, тем быстрее скорость автопрыжка, но больше затраты ЦП!'


        config2 = configparser.ConfigParser()
        config2['BIND'] = {'WH':   bind_wh,
                          'RH':    bind_rh,
                          'EN':    bind_en,
                          'QD':    bind_qd,
                          'RCS':  bind_rcs,
                          'BHOP': bind_bhop,
                          'Menu': bind_menu,
                          'BhopMode': bhop_loop,}
        config2["MISC"] = {'BhopSpeed': bhop_speed,
                           'BhopButton': space_button}

        with open('C:/Users/{}/AppData/Roaming/configs.ini'.format(getpass.getuser()), 'w') as configfile:
                    config2.write(configfile)

        print("\n\n\n   [&] Ваш токен безопастности: ",token)

#data

license_end=r'''

    [!] Дата действия лицензии истекла, чтобы продолжить 
        использование NE.software обновите свою лицензию
    
    [V] $NE.software  < PRO >  
    [$] OK - чтобы перейти на сайт разработчика
    
'''

try:
            now=dt.now()
            deadline = DataL
            if now > deadline:
                messagebox.showinfo("[!] NE.launcher",license_end)
                sleep(1)
                webbrowser.open("https://www.nesoft.fun/auth/auth")
                sleep(10)
                exit()

            else:
                period = deadline - now
                dtl="\n\n\n    [+] Осталось: {} Дней, {} Часов".format(period.days,round((period.seconds/3600),2))

except:
            print("[!] ERROR: клиент не может обнаружить часть кода связанную с лицензией!")
            

load=r'''connecting to NE.software ...''' #Loading
main=r'''                                 



    █▄░█ █▀▀ ░ █▀█ █▀█ █▀█         #VerLow 3Y7F
    █░▀█ ██▄ ▄ █▀▀ █▀▄ █▄█         #Hotfix 4/09/2023

       Функция                       БИНД       Состояние
''' 

radh=r'''
   [+] Радар Хак                 :   ''' #1
wall=r'''
   [+] X-ray Зрение              :   ''' #2
bhop=r'''
   [+] Автораспрыжка             :   ''' #3
enem=r'''
   [+] Вражеский Баланс          :   ''' #4
quic=r'''
   [+] Быстрое приседание (beta) :   ''' #5


rcs=r'''


   [+] RecoilControlSystem (DLC) :   ''' #6
esp=r'''
   [+] ESP - Обводка врага (DLC) :   ''' #7
aim=r'''
   [+] AIM - Автонаводка   (DLC) :   ''' #8
settings=r'''
   

   [!] Настройки                 :   ''' #9 
update=r'''
   [%] Обновить меню             :   '''

radh1 = False
bhop1 = False

wall1 = False
enem1 = False#off
quic1 = False#off


print(load);sleep(3);s("cls")
#print(main,
#      radh,bind_rh,  "         ",radh1,
#      bhop,bind_bhop,"         ",bhop1,
#      enem,bind_en,  "         ",enem1,
#      quic,bind_qd,  "         ",quic1,
#      wall,bind_wh,  "         ",wall1,
#      settings,
#      bind_menu,
#      update,
#      dtl)

GameNotFound=r'''

    [!] Ошибка подключения! 
    [+] Игра не обнаружена..
    [?] Запустить игру автоматически?
        
    [%] Нажмите ENTER, чтобы продолжить.
    
'''

error = r'''

    [!] Произошла ошибка! Попробуйте запустить позже...
    [+] Если у вас запущен FaceitAC - закройте его.
    [+] Если игра лагает/фризит/тормозит отключите софт.
    
    [%] Нажмите ENTER, чтобы продолжить.

'''


try:
        pm = pymem.Pymem('csgo.exe')
        client = pymem.process.module_from_name(pm.process_handle,
                                                    'client.dll')
        client_bhp = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
        radarH = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)                      #RADARHACK
        address = client.lpBaseOfDll + re.search(rb'\x74\x15\x8B\x47\x08\x8D\x4F\x08',
                                                radarH).start() - 1
        wallH = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)                       #WALLHACK
        address1 = client.lpBaseOfDll + re.search(rb'\x33\xC0\x83\xFA.\xB9\x20',
                                                            wallH).start() + 4
        enemyH = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)                      #ВРАЖЕСКИЙ БАЛИК
        address2 = client.lpBaseOfDll + re.search(rb'.\x0C\x5B\x5F\xB8\xFB\xFF\xFF\xFF',
                                                            enemyH).start()
        quickH = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)                      #БЫСТРОЕ ПРИСЕДАНИЕ
        address3 = client.lpBaseOfDll + re.search(rb'\x81\xE2.{4}\x84\xDB',
                                                            quickH).start() + 4
except:
        print(load);sleep(2);os.system("cls")
        console.print(dtl)
        console.print(GameNotFound, style="red")
        input()
        webbrowser.open('steam://rungameid/730')
        while autoStart == 0:
            try:
                    pm = pymem.Pymem('csgo.exe')
                    client = pymem.process.module_from_name(pm.process_handle,
                                                                'client.dll')
                    client_bhp = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
                    sleep(3)
                    radarH = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)                      #RADARHACK
                    address = client.lpBaseOfDll + re.search(rb'\x74\x15\x8B\x47\x08\x8D\x4F\x08',
                                                            radarH).start() - 1
                    wallH = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)                       #WALLHACK
                    address1 = client.lpBaseOfDll + re.search(rb'\x33\xC0\x83\xFA.\xB9\x20',
                                                                        wallH).start() + 4
                    enemyH = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)                      #ВРАЖЕСКИЙ БАЛИК
                    address2 = client.lpBaseOfDll + re.search(rb'.\x0C\x5B\x5F\xB8\xFB\xFF\xFF\xFF',
                                                                        enemyH).start()
                    quickH = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)                      #БЫСТРОЕ ПРИСЕДАНИЕ
                    address3 = client.lpBaseOfDll + re.search(rb'\x81\xE2.{4}\x84\xDB',
                                                                        quickH).start() + 4
                    autoStart = 1
            except:
                    autoStart = 0

s("cls");print(main,
                radh,bind_rh,  "         ",radh1,
                bhop,bind_bhop,"         ",bhop1,
                enem,bind_en,  "         ",enem1,
                quic,bind_qd,  "         ",quic1,
                wall,bind_wh,  "         ",wall1,
                settings,
                bind_menu,
                update,
                dtl)
while True:
    try:
        if keyboard.is_pressed(bind_wh):
            sleep(0.3)
            if wall1 == False:
                wall1 = True
            else:
                wall1 = False
            s("cls");print(main,
                            radh,bind_rh,  "         ",radh1,
                            bhop,bind_bhop,"         ",bhop1,
                            enem,bind_en,  "         ",enem1,
                            quic,bind_qd,  "         ",quic1,
                            wall,bind_wh,  "         ",wall1,
                            settings,
                            bind_menu,
                            update,
                            dtl)
            pm.write_uchar(address1, 2 if pm.read_uchar(address1) == 1 else 1)


        if keyboard.is_pressed(bind_rh):
            sleep(0.3)
            if radh1 == False:
                radh1 = True
            else:
                radh1 = False
            s("cls");print(main,
                            radh,bind_rh,  "         ",radh1,
                            bhop,bind_bhop,"         ",bhop1,
                            enem,bind_en,  "         ",enem1,
                            quic,bind_qd,  "         ",quic1,
                            wall,bind_wh,  "         ",wall1,
                            settings,
                            bind_menu,
                            update,
                            dtl)
            pm.write_uchar(address, 0 if pm.read_uchar(address) != 0 else 2)

        if keyboard.is_pressed(bind_bhop):
            sleep(0.3)
            if bhop1 == False:
                bhop1 = True
            else:
                bhop1 = False
            s("cls");print(main,
                            radh,bind_rh,  "         ",radh1,
                            bhop,bind_bhop,"         ",bhop1,
                            enem,bind_en,  "         ",enem1,
                            quic,bind_qd,  "         ",quic1,
                            wall,bind_wh,  "         ",wall1,
                            settings,
                            bind_menu,
                            update,
                            dtl)
        
        if bhop_loop == 'legit' and bhop1 == True:
            # < Запускаем функцию >
            if pm.read_int(client_bhp + dwLocalPlayer):
                player = pm.read_int(client_bhp + dwLocalPlayer)
                force_jump = client_bhp + dwForceJump
                on_ground = pm.read_int(player + m_fFlags)

            if keyboard.is_pressed(space_button):
                if on_ground == 257 or on_ground == 263:
                    pm.write_int(force_jump, 5)
                    time.sleep(0.17)
                    pm.write_int(force_jump, 4)

        if keyboard.is_pressed("END"):
            sleep(0.3)
            break
        else:
            sleep(0.0001)
        

        if keyboard.is_pressed(bind_menu):
            sleep(0.3)
            s("start C:/Users/{}/AppData/Roaming/configs.ini".format(getpass.getuser()))



        #UPDATE BINDS 
        if keyboard.is_pressed('F10'):
            sleep(0.3)
            s("cls");print(main,
                            radh,bind_rh,  "         ",radh1,
                            bhop,bind_bhop,"         ",bhop1,
                            enem,bind_en,  "         ",enem1,
                            quic,bind_qd,  "         ",quic1,
                            wall,bind_wh,  "         ",wall1,
                            settings,
                            bind_menu,
                            update,
                            dtl)
            try:
                config2 = configparser.ConfigParser()
                config2.read('C:/Users/{}/AppData/Roaming/configs.ini'.format(getpass.getuser()))
                bind_wh = (config2["BIND"]["WH"])  #ЧЕКАЕМ БИНДЫ
                bind_rh = (config2["BIND"]["RH"])
                bind_en = (config2["BIND"]["EN"])
                bind_qd = (config2["BIND"]["QD"])

                bind_menu = (config2["BIND"]["Menu"])
                bind_rcs  = (config2["BIND"]["RCS"])  #RCS Добавить
                bind_bhop = (config2["BIND"]["BHOP"])
                bhop_speed = (float(config2["MISC"]["BhopSpeed"]))
                space_button = (config2["MISC"]["BhopButton"])
                bhop_loop = (config2["BIND"]["BhopMode"])
            except:
                pass


        #SETUP CONFIG & GET RCS API
        if keyboard.is_pressed(bind_rcs):
            print("Скоро!")
            


    except:
        messagebox.showerror("$Error!",error)
        sleep(10)
        break