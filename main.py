#!/usr/bin/python3

import socket 
import argparse

def banner():
    print("""
     ________________                - Printpwn -
    /______________ /|    - a toolkit for exploiting printers -
   /___________/___//|      Written by: @encrypted23 & @sticks
  |===        |----| |              Version: 1.0
  |           |   ô| |
  |___________|   ô| |
  | ||/.´---.||    | |        
  |-||/_____\||-.  | |           
  |_||=L==H==||_|__|/                            
                    
""")


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", type=str, dest="ip_addr", help="--target IP", default=None)
    parser.add_argument("-c", type=str, dest="port", help="--checks for port 9100", default=None)

    args = parser.parse_args()

    ip_addr = ""
    port = ""

    ip_addr = args
    port = args

    if port:
        Check(port)
    else:
        print("[-] Invalid option please check -h for help")


def Check(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = port
    port_1 = 9100

    try:
        print("[+] Checking for port 9100..")
        s.connect((host, port_1))
        print("[+] Port 9100 is open!")
    
    except:
        print("[-] Port 9100 is not open")


banner() 
main()
