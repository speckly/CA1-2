"""Author: @speckly
https://github.com/speckly
Filename: nmap-scanner.py

Description: A script to perform an nmap scan on localhost and host with 
hostname 'scanme.nmap.org', outputs the results of the scan on the top 10 ports per host.

Ref: https://www.studytonight.com/network-programming-in-python/integrating-port-scanner-with-nmap
Ref: https://pypi.org/project/python-nmap/
"""
import os # Only required once

def scan():
    """
  Script to print results of port scan
Run: 
  Nil

Args:
  Nil

Output:
  Prints items such as host, protocol, port and state after a port scan
    """  
    try:
        import nmap
    except ModuleNotFoundError:
        MODULE = "nmap"
        if input(f"{MODULE} is required to run this program, execute pip install {MODULE}? (Y): ").lower().strip() in ["", "y"]:
            os.system(f"pip install {MODULE}")
            print("Restart is required, quitting")
        exit()
    try:
        from rich.align import Align
        from rich.console import Console
        from rich.live import Live
        from rich.table import Table
    except ModuleNotFoundError:
        MODULE = "rich"
        if input(f"{MODULE} is required to run this program, execute pip install {MODULE}? (Y): ").lower().strip() in ["", "y"]:
            os.system(f"pip install {MODULE}")
        else:
            exit()

    # initialize the port scanner
    nmScan = nmap.PortScanner()
    print(f'Type of nmScan : {type(nmScan)}')
    # scan multiple hosts/specify options
    IP = 'localhost scanme.nmap.org'                        
    print(f'Scanning ports: {IP}')
    options = '--top-ports 5 -A -sTU -T5'
    nmScan.scan(hosts=IP, arguments=options)

    # attributes ["Host", "Hostname", "Protocol", "Port ID", "State", "Product", "Extrainfo", "Reason", "CPE"] 
    tab = [] #table data
    for host in nmScan.all_hosts():
        for proto in nmScan[host].all_protocols():
        # print(nmScan[host][proto].keys())
            for port in nmScan[host][proto].keys():
                tab.append([])
                #port attribute pointer for readability of var attrs
                portAttr = nmScan[host][proto][port]
                #definte attributes
                attrs = [host, nmScan[host]["hostnames"][0]["name"], proto, port, portAttr["state"], portAttr["product"], portAttr["extrainfo"], portAttr["reason"], portAttr["cpe"]]
                for attr in attrs:
                    tab[-1].append(attr) #add attributes
    for col in tab:
        for i in range(len(col)):
            if type(col[i]) == int:
                col[i] = str(col[i]) #cannot be int, rich mod rules
    console = Console()

    table = Table(show_footer=False, show_lines=True)
    table_centered = Align.center(table)
    
    scanTime = nmScan.scanstats()["elapsed"]
    print(f"Console scan time: {scanTime}s")
    cols = ["Host", "Hostname", "Protocol", "Port ID", "State", "Product", "Extrainfo", "Reason", "CPE"]
    with Live(table_centered, console=console, screen=False):
        for col in cols:
            table.add_column(col, no_wrap=True)
        for row in tab:
            table.add_row(*row)
        #table_width = console.measure(table).maximum
        table.width = None
    