"""Author: @speckly
https://github.com/speckly
Filename: custom-packet.py

Description: A script to send a custom packet with user input attributes of the packet
Includes, source and destination address, number of packets, packet types and packet data
"""

try:
    from scapy.all import send, IP, TCP, ICMP, UDP 
except ModuleNotFoundError:
    if input("scapy is required to run this program, execute pip install scapy? (Y): ").lower().strip() in ["", "y"]:
        import os # Only required here
        os.system("pip install scapy")
        print("Restart is required, quitting")
    exit()

import re  
# srp and sr1 is for layer 2, send for layer 3

def send_packet(src_addr:str , src_port:int , dest_addr:str, dest_port:int, pkt_type:str, pkt_data:str)  -> bool:
    """Create and send a packet based on the provided parameters

    Args:
        src_addr(str) : Source IP address
        src_port(int) : Source Port
        dest_addr(str): Destination IP address
        dest_port(int): Destination Port
        pkt_type(str) : Type of packet (T)TCP, (U)UDP, (I)ICMP echo request. Note it is case sensitive
        pkt_data(str) : Data in the packet
    Returns:
        bool: True if send successfull, False otherwise
    """    

    if pkt_type == "T":
        pkt = IP(dst=dest_addr,src=src_addr)/TCP(dport=dest_port,sport=src_port)/pkt_data
    elif  pkt_type == "U":
        pkt = IP(dst=dest_addr,src=src_addr)/UDP(dport=dest_port,sport=src_port)/pkt_data
    else:
        pkt = IP(dst=dest_addr,src=src_addr)/ICMP()/pkt_data
    try:
        send(pkt ,verbose = False)   # verbose False, hide "Send 1 packets" message on console
        return True
    except:
        return False
        
def vPort(msg):
    # input only a valid port (int) by checking it against regex
    # msg (str): the message to output during input
    # returns iPort (int)
    while True:
        try: 
            port = input(msg) 
            if not port.isnumeric():
                raise ValueError
            iPort = int(port) #for integer comparison
            if iPort < 1 or iPort > 65535:
                raise ValueError
            break
        except ValueError:
            print("Invalid input please try again")
    return iPort 

def vURL(msg):
    # input only a valid URL (str) by checking it against regex
    # msg (str): the message to output during input
    # returns inp (str URL)
    #matches optional http:// or https://
    #matches second level domain upper lower a-z 0-9
    #matches top level domain upper lower a-z
    regex = ("^(https?:\/\/)?"
    + "([a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)" 
    + "[a-zA-Z]{2,}$")
    pObj = re.compile(regex) #str to Pattern object 
    while True:
        inp = input(msg)
        if (inp == None):
            print("Invalid input")
        elif(re.search(pObj, inp)): #None == False, re.Match object == True
            break
        else:
            print("Invalid input")
        #strip protocol for 
        if "http://" in inp:
            inp = inp.replace("http://", "")
        elif "https://" in inp:
            inp = inp.replace("https://", "")
    return inp
def main():
    """Obtain inputs to create custom packet

    Inputs are stored into local variables on demand, not by args.
    Returns: Nil
    """    
    print("\n************************")
    print("* Custom Packet        *")
    print("************************\n")
    src_addr = vURL("Enter Source address of Packet: ") #TODO: is it a URL or addr?
    src_port = vPort("Enter Source Port of Packet: ")
    dest_addr= vURL("Enter Destination address of Packet: ")
    dest_port= vPort("Enter Destination Port of Packet: ")
    while True:
        pkt_type = input("Enter Type (T) TCP, (U) UDP, (I) ICMP echo request (T/U/I): ")
        if pkt_type.strip() not in ["T", "U", "I"]:
            print("Invalid input try again")
        else:
            break
    if pkt_type == "I":
        print("  Note: Port number for ICMP will be ignored")
    pkt_data = input("Packet RAW Data (optional, DISM-DISM-DISM-DISM left blank): ")
    if pkt_data == "":
        pkt_data = "DISM-DISM-DISM-DISM"
    pkt_count = vPort("No of Packet to send (1-65535): " ) # not a port but requires the same int range as vPort
    start_now = input("Enter Y to Start, Any other return to main menu: ")
    if start_now.lower() != "y": 
        return
    count = 0 #successful sends
    for i in range(pkt_count):
        if send_packet(src_addr, src_port, dest_addr, dest_port, pkt_type, pkt_data):
            count  = count + 1 
    print(count , " packet(s) sent" )
    return
