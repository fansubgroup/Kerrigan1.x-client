#!/usr/bin/env python

import socket
import sys
import json
from multiprocessing import Process

class LoginServer:

    def __init__(self, host_ip, port):

        self.HOST_IP = host_ip
        self.PORT= port
        self.TIMEOUT = 200



    def send_recv(self):

        client_socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        client_socks.settimeout(self.TIMEOUT)

        client_socks.connect((self.HOST_IP, self.PORT))

        HELLO = 'HELLO'

        client_socks.sendall(HELLO)

        while True:

            data_json = client_socks.recv(4096)

            # date_json like ['Show', really_data]

            data = json.loads(data_json)

            print data[1]

            if len(data[0]):

                answer = raw_input('[%s]>>:' % data[0])

                send_process = Process(target = sendp, args = (client_socks, answer))

                send_process.daemon = True

                send_process.start()

            else:

                answer = raw_input('[Normal Mod]>>:')

                send_process = Process(target = sendp, args = (client_socks, answer))

                send_process.daemon = True

                send_process.start()


def sendp(client_socks, answer):

    client_socks.sendall(answer)


def main():
    
    init = LoginServer('127.0.0.1', 8001)

    init.send_recv()

if __name__ == "__main__":

    main()
