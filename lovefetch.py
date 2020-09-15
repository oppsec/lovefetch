import os
import sys
import socket
import platform
import cpuinfo

from psutil import virtual_memory, boot_time
from rich import print
from datetime import datetime, date
from ascii import windows, linux, macos, unknow

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Informations

hostUsername = socket.gethostname() # Username
osPlatform = platform.platform() # OS name
machinePlatform = platform.machine() # Machine Platform (AMD64...)
dateTime = date.today() # Current day
upTime = datetime.fromtimestamp(boot_time()).strftime("%Y-%m-%d %H:%M:%S") # Boot time
computerMemory = virtual_memory() # Computer memory
getCPU = cpuinfo.get_cpu_info() # Get computer CPU
computerCPU = getCPU['brand_raw'] # Get computer CPU name

def lovefetch():
    clearTerminal()

    if sys.platform.startswith('win'):
        print(windows)
    elif sys.platform.startswith('linux'):
        print(linux)
    elif sys.platform.startswith('darwin'):
        print(macos)
    else:
        print(unknow)

    print(f'[bold magenta] Username ~> {hostUsername} [/bold magenta]')
    print(f'[bold magenta] Date ~> {dateTime} [/bold magenta]')
    print(f'[bold magenta] OS ~> {osPlatform} [/bold magenta]')
    print(f'[bold magenta] Uptime ~> {upTime} [/bold magenta]')
    print(f'[bold magenta] Memory ~> {computerMemory.total} [/bold magenta]')
    print(f'[bold magenta] CPU ~> {computerCPU} [/bold magenta]')
    print(f'[bold magenta] Machine Platform ~> {machinePlatform} [/bold magenta] \n')
    print('[bold green] Lovefetch version ~> 1.0.0 [/bold green]')


lovefetch()