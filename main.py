from vcore import *
import os

from scapy.all import *

vsetup()
vbanner()
while True:
    val0 = smenu("Menu", [
    "List all interfaces",
    "Monitor mode settings",
    "Spam access points",
    "Clear screen",
    "Exit"])

    if val0 == "0":
        os.system("sudo airmon-ng")
    elif val0 == "1":
        dspoa = smenu("Start or stop monitor mode", [
            "Start",
            "Stop"
        ])
        if dspoa == "0":
            os.system("sudo airmon-ng check")
            print("There may be processes that cause a malfunction, do you want to stop them? (y/n)")
            wtkbp = input(f"{Fore.LIGHTGREEN_EX}> {Fore.RESET}")
            if wtkbp.lower() == "y":
                os.system("sudo airmon-ng check kill")
                print("Success!")
            else:
                print("Proceed. Warning, there may be errors")
            os.system("sudo airmon-ng")
            print("Type your interface name...")
            iftimm = input(f"{Fore.LIGHTGREEN_EX}> {Fore.RESET}")
            os.system(f"sudo airmon-ng start {iftimm}")
        else:
            os.system("sudo airmon-ng")
            print("Type your interface name...")
            iftimm = input(f"{Fore.LIGHTGREEN_EX}> {Fore.RESET}")
            os.system(f"sudo airmon-ng stop {iftimm}")
            print("Success!")
            carlo17 = input("Want to restart NetworkManager service? (y/n) > ")
            if carlo17.lower() == "y":
                os.system("service NetworkManager restart")
            else:
                print("Not restarting...")
    elif val0 == "2":
        cls()
        apsnum = input("How many ap's? > ")
        videorlo = smenu("Ap's names?", [
            "One name"
        ])
        if videorlo == "0":
            vadeu = input("Name > ")
            os.system("sudo airmon-ng")
            ifacenam = input("Interface name? > ")
            spamwifis(apsnum, ifacenam, vadeu)
    elif val0 == "3":
        cls()
    elif val0 == "4":
        exit()