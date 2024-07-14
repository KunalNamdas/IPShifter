
import requests
import os
import time
import subprocess
import signal
import sys
import logging
from pystyle import Box
from colorama import init

# Global variables
TOR_SERVICE = 'tor'
TOR_SERVICE_COMMAND = 'service tor'
TOR_SOCKS_PORT = '9050'
API_URL = 'https://api.ipify.org'

# ANSI color codes
GREEN = '\033[92m'
RESET = '\033[0m'
BLUE = '\033[94m'
RED = '\033[91m'
WHITE = '\033[0m'

# ASCII art and developer name
ascii_art = """
▀█▀ ▒█▀▀█ ▒█▀▀▀█ █░░█ ░▀░ █▀▀ ▀▀█▀▀ █▀▀ █▀▀█ 
▒█░ ▒█▄▄█ ░▀▀▀▄▄ █▀▀█ ▀█▀ █▀▀ ░░█░░ █▀▀ █▄▄▀ 
▄█▄ ▒█░░░ ▒█▄▄▄█ ▀░░▀ ▀▀▀ ▀░░ ░░▀░░ ▀▀▀ ▀░▀▀
"""

developer_name = "D E V E L O P E D  B Y  K U N A L  N A M D A S"
decorative_line = "\n" + "  " + "»" * 78 + "\n"

# Setup logging
logging.basicConfig(filename='ipshifter.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to display ASCII art
def display_ascii_art(ascii_art):
    print(GREEN + ascii_art + RESET)

# Function to handle Ctrl+C gracefully
def signal_handler(sig, frame):
    print("\n" + GREEN + "[+] Exiting gracefully..." + RESET)
    logging.info('Exiting gracefully')
    sys.exit(0)

# Install required libraries
def install_lib(lib_name):
    try:
        subprocess.check_output(['pip', 'show', lib_name])
        print('[+]', lib_name, 'is already installed')
        logging.info(f'{lib_name} is already installed')
    except subprocess.CalledProcessError:
        print('[+]', lib_name, 'is not installed')
        logging.warning(f'{lib_name} is not installed')
        subprocess.check_output(['pip', 'install', lib_name])
        print('[!]', lib_name, 'installed successfully')
        logging.info(f'{lib_name} installed successfully')

# Install required packages
def install_package(package_name):
    try:
        subprocess.check_output(['dpkg', '-s', package_name])
        print('[+]', package_name, 'is already installed')
        logging.info(f'{package_name} is already installed')
    except subprocess.CalledProcessError:
        print('[+]', package_name, 'is not installed')
        logging.warning(f'{package_name} is not installed')
        subprocess.check_output(['sudo', 'apt', 'update'])
        subprocess.check_output(['sudo', 'apt', 'install', package_name, '-y'])
        print('[!]', package_name, 'installed successfully')
        logging.info(f'{package_name} installed successfully')

# Change IP address using TOR
def change_ip():
    os.system(f"{TOR_SERVICE_COMMAND} reload")
    logging.info('TOR service reloaded')
    try:
        response = requests.get(API_URL, proxies={'http': f'socks5h://127.0.0.1:{TOR_SOCKS_PORT}', 'https': f'socks5h://127.0.0.1:{TOR_SOCKS_PORT}'})
        new_ip = response.text
        print(f'[+] Your IP has been changed to: {new_ip}')
        logging.info(f'IP changed to {new_ip}')
    except requests.RequestException as e:
        print(f'[-] Error changing IP: {str(e)}')
        logging.error(f'Error changing IP: {str(e)}')

# Main function
def main():
    display_ascii_art(ascii_art)
    signal.signal(signal.SIGINT, signal_handler)

    install_package('python3-pip')
    install_package('tor')

    packages_to_install = ['pystyle', 'colorama', 'requests']
    for package in packages_to_install:
        install_lib(package)

    init(autoreset=True)
    interface = input("Enter Your Wireless Interface Name: ")
    os.system("clear")

    print(decorative_line)
    print(f"            {GREEN}▌║█║▌│║▌│║▌║▌█║ {RED}IPShifter v1.0{GREEN} ▌│║▌║▌│║║▌█║▌║█{RESET}\n")
    print(f"            D E V E L O P E D  B Y  K U N A L  N A M D A S                    ")
    print(decorative_line)

    os.system(f"{TOR_SERVICE_COMMAND} start")
    time.sleep(10)
    print(f"            \033[1;32;40m Change your SOCKS to 127.0.0.1:{TOR_SOCKS_PORT}\n                   ")

    x = input("[+] Time to change IP in seconds [type=60] >> ")
    lin = input("[+] How many times do you want to change your IP [type=1000] For infinite IP change, type [0] >> ")

    os.system('clear')

    print()
    print(f"            {BLUE}▌║█║▌│║▌│║▌║▌█║ {WHITE}IPShifter v1.0{BLUE} ▌│║▌║▌│║║▌█║▌║█{RESET}\n")
    print(f"            D E V E L O P E D  B Y  K U N A L  N A M D A S                    ")
    print()

    print("                 \033[1;32;94m Change your SOCKS to 127.0.0.1:9050\n                   ")

    if int(lin) == 0:
        try:
            while True:
                change_ip()
                time.sleep(int(x))
        except KeyboardInterrupt:
            print('\nAuto TOR is closed.')
            logging.info('Auto TOR closed')
    else:
        for i in range(int(lin)):
            change_ip()
            time.sleep(int(x))

if __name__ == '__main__':
    main()