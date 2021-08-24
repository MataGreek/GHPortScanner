import sys
import socket
import pyfiglet
import threading
import colorama
from colorama import *
colorama.init()

print_lock = threading.Lock()

#LOGO

logo = pyfiglet.figlet_format("GH port scanner")
print(logo)
print("-" * 120)
print("                                     Created By Mata | https://www.greekhacking.gr/          ")
print("-" * 120)

#INPUT
print("")
print("")
print("")

try:
    target = input("  Enter the Host Here:    ")
    target_ip = socket.gethostbyname(target)
except Exception:
    print("")
    print(Fore.RED +  "  Error: Could not find the HOST. (Check your internet connection or your input is wrong)")
    print("")
    print("")
    print("")
    sys.exit()


    
print("-" * 60)
print("Please wait, GH scanning the host... ==>  ", (Fore.LIGHTBLUE_EX + target_ip + Fore.RESET))
print("")
print("Will take sometime, go get a coffee :)")
print("-" * 60)
print("")

#PORTS

try:
        for port in range(1,1000):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.2)
            r = s.connect_ex((target_ip,port))
            with print_lock:
                if r == 0:
                    print( Fore.RED + " [+]  " + Fore.WHITE + str(port) + Fore.WHITE + " ==> " + Fore.GREEN + " Open! " + Fore.RESET)
                    s.close()

except KeyboardInterrupt:
    print("")
    print("")
    print("")
    print("Exiting........")
    print("")
    print("")
    print("")

    sys.exit()

    
