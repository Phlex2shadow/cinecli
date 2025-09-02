# -*- coding: utf-8 -*-
# Copyright (c) 2025 Alex's GlowCity Studio.

import sys
import linecache
import random
import time
import datetime
import getpass


myth = ["EnterTheVoidway", "cat"]

delay = random.randint(1, 4)

utc_time = datetime.datetime.now(datetime.UTC).strftime("%H:%M:%S")
username = getpass.getuser()


def clscr():
    print("\033[H\033[J", end="")


def login():
    try:
        print("[Myth] Boot")
        print("Last login:", utc_time, "UTC", "******** ****")
        print("Login: ", end="")
        loginame = input()

        for i in range(3):
            if loginame in username:
                print(
                    "Verifying user entitlement with quantum entanglement authenticator...\n"
                )
                status()
                break
            else:
                print("Error: Identification not recognized. Access denied")
                break
    except KeyboardInterrupt as e:
        sys.exit("Error: Login incorrect")
    except Exception as e:
        print("DUMP")


def status():
    print("Status: ", end="")
    time.sleep(delay)
    print("Failed. Retrocausality detected")
    time.sleep(2)
    lockdown()


def lockdown():
    print("Deja Vu Zone security protocol initialized\n")
    print("Termianl locked until further notice...")
    run_cmd()


def run_cmd():
    try:
        while True:
            print("> ", end="")
            cmd = input()
            if cmd in ["help", "?"]:
                print("There no help page for Myth")
            elif cmd == "whoami":
                print(username)
            elif cmd in myth:
                mythSaying()
            elif cmd == "exit":
                break
            else:
                print("Command not found")
    except KeyboardInterrupt as e:
        sys.exit("Error: User manually logged out")
    finally:
        sys.exit("Excessive retry. Shutdown...")


def mythSaying():
    print("Goodbye, all things.")
    print("All consuming.")
    print("THE POOL STORMS FORTH DOOMED, WE LIVE ON")


# Clear screen
clscr()

print("\033[32m")

# Print motd
print("""
          ░         ░                                                           
         ░█░       ░█░   ▒█░▒████        █▓ ███████ ██████████ █ ████       █ TM
        ░███░     ░███░   ▒█░▒████      █▓        █ ████       █ ████       █   
       ░▒████░   ░▒████░   ▒█░▒████    █▓         █ ████       █ ████       █   
      ░█░▒████░ ░█░▒████░   ▒█░▒████  █▓          █ ████       █ ████       █   
     ░█▓█░▒████░█▀█░▒████░   ▒█░▒█████▓           █ ████       █ ████       █   
    ░█▓ ▒█░▒████▓ ▒█░▒████░   ▒█░ ████            █ ████       █ ████       █   
   ░█▓   ▒█░▒██▓   ▒█░▒████░   ▒█ ████            █ ████       █ ████████████   
  ░█▓     ▒█░▒▓     ▒█░▒████░   █ ████            █ ████       █ ████       █   
 ░█▓       ▒█        ▒█░▒████░  █ ████            █ ████       █ ████       █   
░█▓         ▒         ▒█░▒████░ █ ████            █ ████       █ ████       █   

Brought to you by
  \\  |                    _ \\ _)       |   ©
 |\\/ |   _ \\    \\    - \\  |  | | (_-<  | /  
_|  _| \\___/ _| _| \\___/ ___/ _| ___/ _\\_\\  
================================================================================
""")

if __name__ == "__main__":
    login()
