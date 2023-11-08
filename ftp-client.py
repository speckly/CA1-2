"""Author: @speckly
https://github.com/speckly

Ref: https://pythonspot.com/ftp-client-in-python/
"""

import os

def getFile(ftp):
    # Download file from folder defined in ftp-server.py
    file = input("Enter filename to download from server: ")
    cwd = os.getcwd() # Get original cwd before changing cwd
    while True: 
        direct = input("Enter local directory for putting the downloaded file: ")
        try:
            os.chdir(direct) 
            break
        except PermissionError:
            print("Insufficient directory permissions please try again")
        except NotADirectoryError:
            print("Not a directory, please try again")
        except FileNotFoundError:
            print("Directory not found please try again")
    try:
        fExist = 0 # Truth value if file never existed, 1 = True
        if not os.path.isfile(file): # If file does not exist in client directory
            fExist = 1 # Change the truth value to True, that file never existed
        ftp.retrbinary("RETR " + file ,open(file, 'wb').write)
        print(f'Downloaded file: {file}')
    except Exception:
        print(f'Error in downloading: {file}')
        if fExist == 1: # Since file never existed but storbinary function wrote an empty file
            os.remove(file) # Delete the empty file
    os.chdir(cwd) # Return to original wd
    input("Enter any key to continue: ")

def upFile(ftp):
    # Similar to getFile()
    file = input("Enter filename to upload to server: ")
    cwd = os.getcwd() 
    while True:  
        try:
            direct = input("Enter home directory for getting the file to upload: ")
            os.chdir(direct) 
            break
        except PermissionError:
            print("Insufficient directory permissions please try again")
        except NotADirectoryError:
            print("Not a directory, please try again")
        except FileNotFoundError:
            print("Directory not found please try again")
    try:
        ftp.storbinary("STOR " + file, open(file, "rb"))
        print(f'Uploaded file: {file}')
    except Exception:
        print(f'Error in uploading: {file}')
    os.chdir(cwd)
    input("Enter any key to continue: ")