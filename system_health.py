import os
from rich.console import Console
from rich.prompt import Prompt


console = Console()


def colour_print(colour, string):
    console.print(string, style = f'bold {colour}')


def execute_shell(cmd):
    return os.popen(cmd).read()


def display_ram():
    res = execute_shell("free -m | tail -n 2 | head -n 1 | tr -s ' ' | cut -d' ' -f4").strip()
    colour_print("#00F0F0", f"Available RAM: {res} MB")


def display_load_average():
    res = execute_shell("cat /proc/loadavg")
    colour_print("#00F0F0", f"Load Average: {res}")


def display_hostname_details():
    res = execute_shell("hostnamectl status")
    colour_print("#00F0F0", res)


def display_all_process_count():
    res = execute_shell("ps aux | wc -l")
    colour_print("#00F0F0", f"All process count: {res}")


def display_uptime():
    res = execute_shell("uptime").split(",")[0]
    colour_print("#00F0F0", f"Uptime: {res}")


