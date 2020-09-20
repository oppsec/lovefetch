#!/usr/bin/env python3

from os import system
from os import name as os_name
from sys import platform as sys_platform
from socket import gethostname as hostname
from platform import platform as os_platform
from platform import machine as machine_platform
from cpuinfo  import get_cpu_info as cpu_info

from psutil import virtual_memory, boot_time
from datetime import datetime, date
from ascii import *

LOVEFETCH_VERSION = '1.0.0'

hostUsername    = hostname()
osPlatform      = os_platform()
machinePlatform = machine_platform()
cpuInfo         = cpu_info()['brand_raw']
memory           = round(virtual_memory().total / (1024.0 ** 3), 2)
dateToday       = date.today()
upTime          = datetime.fromtimestamp(boot_time()).strftime("%Y-%m-%d %H:%M:%S")

def clearTerminal():
    system('cls' if os_name == 'nt' else 'clear')

def lovefetch():
    clearTerminal()

    if sys_platform.startswith('win'):
        print(windows)
    elif sys_platform.startswith('linux'):
        print(linux)
    else:
        print(unknown)

    print(f'[bold magenta] Username\t\t~> {hostUsername} [/bold magenta]')
    print(f'[bold magenta] Date\t\t\t~> {dateToday} [/bold magenta]')
    print(f'[bold magenta] OS\t\t\t~> {osPlatform} [/bold magenta]')
    print(f'[bold magenta] Uptime\t\t\t~> {upTime} [/bold magenta]')
    print(f'[bold magenta] Memory\t\t\t~> {memory} GB [/bold magenta]')
    print(f'[bold magenta] CPU\t\t\t~> {cpuInfo} [/bold magenta]')
    print(f'[bold magenta] Machine Platform\t~> {machinePlatform} [/bold magenta]\n')
    print(f'[bold green] Lovefetch version: {LOVEFETCH_VERSION} [/bold green]')

lovefetch()
