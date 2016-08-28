#!/usr/bin/env python

import socket
import sys

class LoginServer:
    
    def __init__(self, host_ip, port):
        
        self.HOST_IP = host_ip
        self.PORT= port
        self.TIMEOUT = 20
        
    def login(self):
        
        client_socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        client_socks.settimeout(self.TIMEOUT)
        
        client_socks.connect((self.HOST_IP, self.PORT))
        
        HELLO = 'HELLO'
        client_socks.sendall(HELLO)
        
        while True:
            
            data = client_socks.recv(4096)
            print data
            
            answer = raw_input('>>:')
            
            client_socks.sendall(answer)

def main():
    
    init = LoginServer('127.0.0.1', 8001)
    init.login()
    
if __name__ == "__main__":
    main()
