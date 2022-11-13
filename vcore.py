from colorama import Fore, Back
import time 
import os

from scapy.all import *
from threading import Thread
from faker import Faker

def smenu(title, items):
    print(f"{Fore.GREEN}╔══════┅┅ {Fore.LIGHTGREEN_EX}{title}")
    for i in range(len(items)):
        print(f"{Fore.GREEN}║")
        print(f"{Fore.GREEN}╠═▸ {i}. {Fore.RESET}{items[i]}")
    print(f"{Fore.GREEN}║\n╚═┅┅{Fore.RESET}")
    krisjf = input(f"\n{Fore.LIGHTGREEN_EX}[{Fore.RESET}🐉{Fore.LIGHTGREEN_EX}] Option > {Fore.RESET}")
    return str(krisjf)
def cls():
    os.system("cls" if os.name == "nt" else "clear")
    
def vsetup():
    def oscomp():
        if os.name == "nt":
            cls()
            print(f"{Fore.RED}THIS ONLY WORKS ON LINUX SYSTEMS!{Fore.RESET}")
            exit()
    def vulnus_made():
        print(f"""{Fore.GREEN}
 /$$    /$$ /$$   /$$ /$$       /$$   /$$ /$$   /$$  /$$$$$$ 
| $$   | $$| $$  | $$| $$      | $$$ | $$| $$  | $$ /$$__  $$
| $$   | $$| $$  | $$| $$      | $$$$| $$| $$  | $$| $$  \__/{Fore.LIGHTGREEN_EX}
|  $$ / $$/| $$  | $$| $$      | $$ $$ $$| $$  | $$|  $$$$$$ 
 \  $$ $$/ | $$  | $$| $$      | $$  $$$$| $$  | $$ \____  $$
  \  $$$/  | $$  | $$| $$      | $$\  $$$| $$  | $$ /$$  \ $$
   \  $/   |  $$$$$$/| $$$$$$$$| $$ \  $$|  $$$$$$/|  $$$$$$/
    \_/     \______/ |________/|__/  \__/ \______/  \______/ {Fore.RESET}
""")
    cls()
    vulnus_made()
    time.sleep(2)
    cls()

def vbanner():
    print(f"""{Fore.LIGHTGREEN_EX}
 ██▒   █▓ ▒█████   ██▓  ▄▄▄█████▓ ██▓ █    ██  ███▄ ▄███▓
▓██░   █▒▒██▒  ██▒▓██▒  ▓  ██▒ ▓▒▓██▒ ██  ▓██▒▓██▒▀█▀ ██▒
 ▓██  █▒░▒██░  ██▒▒██░  ▒ ▓██░ ▒░▒██▒▓██  ▒██░▓██    ▓██░
  ▒██ █░░▒██   ██░▒██░  ░ ▓██▓ ░ ░██░▓▓█  ░██░▒██    ▒██ 
   ▒▀█░  ░ ████▓▒░░██████▒▒██▒ ░ ░██░▒▒█████▓ ▒██▒   ░██▒
   ░ ▐░  ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ░░   ░▓  ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░
   ░ ░░    ░ ▒ ▒░ ░ ░ ▒  ░  ░     ▒ ░░░▒░ ░ ░ ░  ░      ░
     ░░  ░ ░ ░ ▒    ░ ░   ░       ▒ ░ ░░░ ░ ░ ░      ░   
      ░      ░ ░      ░  ░        ░     ░            ░   
     ░                                                   {Fore.RESET}
""")


def send_beacon(ssid, mac, ifacem, infinite=True):
    dot11 = Dot11(type=0, subtype=8, addr1="ff:ff:ff:ff:ff:ff", addr2=mac, addr3=mac)
    # ESS+privacy to appear as secured on some devices
    beacon = Dot11Beacon(cap="ESS+privacy")
    essid = Dot11Elt(ID="SSID", info=ssid, len=len(ssid))
    frame = RadioTap()/dot11/beacon/essid
    sendp(frame, inter=0.1, loop=1, iface=ifacem, verbose=0)

# faker.name()
def spamwifis(n_ap, iface, spmname):
    faker = Faker()
    ssids_macs = [
        (
        f"{spmname}{i}",
        faker.mac_address()
        ) for i in range(int(n_ap)) ]

    for ssid, mac in ssids_macs:
        Thread(target=send_beacon, args=(ssid, mac, iface)).start()
