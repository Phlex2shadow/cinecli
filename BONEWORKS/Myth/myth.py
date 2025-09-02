# -*- coding: utf-8 -*-
# Copyright (c) 2025 Alex's GlowCity Studio.

import sys
import linecache
import random
import time
import datetime
import getpass
import shlex

from fetch import *


mythwords = ["EnterTheVoidway"]

DELAY = random.randint(1, 4)

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

        for _ in range(3):
            if loginame == username:
                print(
                    "Verifying user entitlement with quantum entanglement authenticator...\n"
                )
                print("Status: ", end="")
                time.sleep(DELAY)
                print("Failed. Retrocausality detected")
                time.sleep(2)
                print("Deja Vu Zone security protocol initialized\n")
                print("Termianl locked until further notice...")
                run_command()
                return
            else:
                print("Error: Identification not recognized. Access denied")
                break
    except KeyboardInterrupt as e:
        sys.exit("Error: Login incorrect")
    except Exception as e:
        print()


def run_command():
    try:
        while True:
            print("> ", end="")
            command_self = input()
            command_args = shlex.split(command_self)
            if command_self == "exit":
                break
            elif command_args:
                command = command_args[0]
                if command in commands:
                    handler = commands[command]
                    if callable(handler):
                        handler(*command_args[1:])
                    else:
                        print(handler)
                else:
                    print(f"{command}: command not found")
    except KeyboardInterrupt:
        sys.exit("Error: User manually logged out")


def mythSaying():
    print("Goodbye, all things.")
    print("All consuming.")
    print("THE POOL STORMS FORTH DOOMED, WE LIVE ON")


def echo(*args):
    print(" ".join(args))


def whoami():
    print(getpass.getuser())


commands = {
    "echo": echo,
    "clear": clscr,
    "whoami": whoami,
}


# Clear screen
clscr()
print("\033[32m")


if __name__ == "__main__":
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
    login()
