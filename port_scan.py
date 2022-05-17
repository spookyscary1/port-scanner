#!/usr/bin/env python

import socket

HOST = "192.168.83.11"  # plz replace with host IP address

# loops through all ports
# for i in range (0,65,536):
for i in range(0,65536):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port=i
    server_addr = (HOST, port)
    port_status=sock.connect_ex(server_addr)
    if port_status==0:
        print("port "+ str(i)+" is open")
    sock.close()
    