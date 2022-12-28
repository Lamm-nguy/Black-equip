#_____-----_____-----[Module}-----_____-----_____-----
try:
    import os
    import sys
    import time
    import colorama
    from colorama import Fore,Back, Style
    from colorama import init, AnsiToWin32
    import socket
    import os
    import requests
    import random
    import getpass
    import time
    import sys
except ModuleNotFoundError:
    print("You don't have all dependencies.")
    time.sleep(2)
    print("QUITTING!")
    os.system("cls")
#_____-----_____-----[Black_Equip Logo]-----_____-----_____-----
def Infinity():
    if os.name == "Linux":
        print(Fore.RESET + Fore.BLUE + "     =====     =====")
        print(Fore.RESET + Fore.GREEN + "    ==   ===   ===   ==")
        print(Fore.RESET + Fore.YELLOW + "   ===   =========   ===")
        print(Fore.RESET + Fore.RED + "    ==   ===   ===   ==")
        print(Fore.RESET + Fore.MAGENTA + "     =====       =====")
    else:
        init(wrap=False)
        stream = AnsiToWin32(sys.stderr).stream
        print(Fore.RESET + Fore.BLUE + "     =====     =====", file=stream)
        print(Fore.RESET + Fore.GREEN + "    ==   ===   ===   ==", file=stream)
        print(Fore.RESET + Fore.YELLOW + "   ===   =========   ===", file=stream)
        print(Fore.RESET + Fore.RED + "    ==   ===   ===   ==", file=stream)
        print(Fore.RESET + Fore.MAGENTA + "     =====       =====", file=stream)
#_____-----_____-----[Main]-----_____-----_____-----
def main():
    if os.name == "Linux":
        os.system("clear")
        Infinity()
        print(Back.RESET + Fore.GREEN + " > " + Fore.YELLOW + Back.BLUE + "1 " + Back.RESET + Fore.RESET + Fore.RED + "DDoS", file=stream)
        print(Back.RESET + Fore.GREEN + " > " + Fore.YELLOW + Back.BLUE + "2 " + Back.RESET + Fore.RESET + Fore.RED + "Vulnerability Scan", file=stream)
        print(Back.RESET + Fore.GREEN + " > " + Fore.YELLOW + Back.BLUE + "3 " + Back.RESET + Fore.RESET + Fore.RED + "Command Enforcementer", file=stream)
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
    else:
        os.system("cls")
        Infinity()
        init(wrap=False)
        stream = AnsiToWin32(sys.stderr).stream
        print(Back.RESET + Fore.YELLOW        + " > " + Fore.GREEN + Back.BLUE + "1 " + Back.RESET + Fore.RESET + Fore.RED + "DDoS", file=stream)
        print(Back.RESET + Fore.YELLOW + " > " + Fore.GREEN + Back.BLUE + "2 " + Back.RESET + Fore.RESET + Fore.RED + "Vulnerability Scan", file=stream)
        print(Back.RESET + Fore.YELLOW + " > " + Fore.GREEN + Back.BLUE + "3 " + Back.RESET + Fore.RESET + Fore.RED + "Command Enforcementer", file=stream)
        while True:
            option = input("> ")
            if option == "1":
                print("This option is not supported for Windows")
            if option == "2":
                tg = input("Target > ")
                os.system("nmap -sV --script=vulscan/vulscan.nse " + tg)
            if option == "3":
                commd = input("Command > ")
                os.system(commd)

if __name__ == '__main__':
    try:
        main()
    except:
        os.system("cls")
        stream = AnsiToWin32(sys.stderr).stream
        print("System is Exitting...")
        time.sleep(2)
        print("Exitted!")
