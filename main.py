"""Author: @speckly
https://github.com/speckly
Created on 9 Jan 2023

File: main.py
"""

import os
import ftplib
import importlib
pck = importlib.import_module("custom-packet")
cli = importlib.import_module("ftp-client")
nmapC = importlib.import_module("nmap-scanner")
#only run along main when multithreading is supported
#serv = importlib.import_module("ftp-server") 

def vInterface():
    """Void function, prints main menu and asks for main menu input (1-4)
    Calls functions from other .py files in this folder based on input
    No arguments or returns
    """
    
    uInp = 0 # User input for the program menu
    while uInp != 4:
        os.system('cls')
        print("""
** PSEC Info Security Apps **
1) Scan network
2) Upload/download file using FTP
3) Send custom packet
4) Quit    
            """)
        while True:
            try: 
                uInp = int(input("\nEnter an option: "))
                if uInp not in range(1, 5):
                    raise ValueError
                break
            except ValueError:
                print("Invalid input please try again")
        match uInp:
            case 1: # Nmap
                nmapC.scan()
                input("Enter to continue: ")
            case 2: # FTP
                while True:
                    os.system('cls')
                    print("""
** FTP **
1) Download file
2) Upload file
3) Start server
4) Exit""")
                    while True:
                        opt = input("\nEnter an option: ")
                        if opt.strip() not in "1234":
                            print("Invalid input try again")
                        else:
                            opt = int(opt)
                            break 
                    if opt == 3:
                        os.system('start cmd /c python ftp-server.py') # Starts server in new cmd
                        print("Server started, input server date directory in the new terminal before using it")
                        input("\nEnter any key to continue: ")
                    elif opt == 4:
                        break
                    else: # Options 1 and 2 are here
                        FTP_PORT = 2121
                        ftp = ftplib.FTP() 
                        try:
                            ftp.connect('localhost', FTP_PORT)
                            ftp.login()
                            if opt == 1:
                                cli.getFile(ftp) 
                            elif opt == 2:
                                cli.upFile(ftp)
                        except:
                            print("Error connecting to server.")
                            input("\nEnter any key to continue: ")
            case 3:
                pck.main()
                input("Enter to return: ")
            case 4: 
                return

if __name__ == "__main__":
    vInterface()