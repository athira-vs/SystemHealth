#!/usr/bin/python3

from rich.prompt import Prompt
from system_health import *

while True:

    colour_print("green", f"{'_'*20}MENU{'_'*20}")
    colour_print("green", "[1] Display available RAM")
    colour_print("green", "[2] Display Load avearge")
    colour_print("green", "[3] Display Hostname details")
    colour_print("green", "[4] Display all process count")
    colour_print("green", "[5] Display uptime")
    colour_print("red", "[6] Exit")

    ch = Prompt.ask("Select an option", choices = [str(x) for x in range(1,7)])
    
    if ch == '1':
        display_ram()
    elif ch == '2':
        display_load_average()
    elif ch == '3':
        display_hostname_details()
    elif ch == '4':
        display_all_process_count()
    elif ch == '5':
        display_uptime()
    elif ch == '6':
        break
        