# sec-test @speckly

This Python script is a menu-driven information security application that provides various functionalities related to network scanning, FTP file operations, and sending custom packets. The script is modularized, utilizing separate Python files for different functionalities.

> [!NOTE]  
> All hosts are hardcoded as 'localhost', as this was made for educational purpose, not for productional use

## Usage
1. Clone the repository.
2. Install the required dependencies using the provided `pip install` commands. (optional, script can assist in this)
3. Run the script.

## Functionality

### Network Scan (Nmap)
- Option: `1`
- Initiates a network scan using Nmap.
- After the scan, press Enter to continue.

### FTP Operations
- Option: `2`
- FTP operations sub-directory:
- Download file: Option `1`
- Upload file: Option `2`
- Start server: Option `3`
- Exit: Option `4`
- If starting the server, a new command prompt is opened, and the user should input the server data directory in the new terminal.
- For download/upload, the user is prompted for FTP server connection details.
- Option `4` exits the FTP sub-menu.

### Send Custom Packet
- Option: `3`
- Calls the `custom-packet` module to send a custom packet.
- Press Enter to return after sending the packet.

### Quit
- Option: `4`
- Exits the main menu and terminates the program.

