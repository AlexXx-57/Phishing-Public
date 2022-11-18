import os
try:
    import colorama
except:    
    print("Some modules are not installed!!\nPlease wait. Installing.......")
    os.system('pip install colorama --quiet')
    os.system('cls' if os.name == 'nt' else 'clear')

from colorama import Fore, Style
import os
import time



def PrintBanner():
    print('''
   	{red} ____  _     _     _       _   _            _{reset}    
	{yellow}|  _ \| |__ (_)___| |__   | | | | __ _  ___| | __{reset}
	{bright}{yellow}| |_) | '_ \| / __| '_ \  | |_| |/ _` |/ __| |/ /{reset}
	{green}|  __/| | | | \__ \ | | | |  _  | (_| | (__|   < {reset}
	{blue}|_|   |_| |_|_|___/_| |_| |_| |_|\__,_|\___|_|\_\{reset}
    {bright}Version {green}{ver}\t\t\t\t\t\tBy: {yellow}CyberGeek{white}
    '''.format(ver=2.0, red=Fore.RED, yellow=Fore.YELLOW, green=Fore.GREEN,
    blue=Fore.BLUE, pink=Fore.MAGENTA, white=Fore.WHITE, reset=Style.RESET_ALL, bright=Style.BRIGHT))

    time.sleep(2) 

# PrintBanner()





