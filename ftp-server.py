"""Author: @speckly
https://github.com/speckly

A program to start a ftp server and allow users to interact with it 
Ref: 
https://pyftpdlib.readthedocs.io/en/latest/tutorial.html
https://pyftpdlib.readthedocs.io/en/latest/api.html
"""

try:
    from pyftpdlib.authorizers import DummyAuthorizer
    from pyftpdlib.handlers import FTPHandler
    from pyftpdlib.servers import FTPServer
except ModuleNotFoundError:
    import os
    MODULE = "pyftpdlib"
    if input(f"{MODULE} is required to run this program, execute pip install {MODULE}? (Y): ").lower().strip() in ["", "y"]:
        os.system(f"pip install {MODULE}")
    else:
        exit()

def servStart():
    # Instantiate a dummy authorizer for managing 'virtual' users
    authorizer = DummyAuthorizer() # handle permission and user
    # Define an anonymous user and input home directory having read permissions
    while True:
        try:
            direct = input("Enter server home directory: ")
            authorizer.add_anonymous(direct , perm='elradfmwM') #originally elr is not enough 
            break
        except:
            print("Invalid directory please try again")
    # Instantiate FTP handler class
    handler = FTPHandler # understand FTP protocol
    handler.authorizer = authorizer

    # Instantiate FTP server class and listen on 127.0.0.1:2121
    address = ('127.0.0.1', 2121)
    server = FTPServer(address, handler)

    server.serve_forever()

servStart()