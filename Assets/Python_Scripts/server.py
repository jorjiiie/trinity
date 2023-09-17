# Created by Youssef Elashry to allow two-way communication between Python3 and Unity to send and receive strings

# Feel free to use this in your individual or commercial projects BUT make sure to reference me as: Two-way communication between Python 3 and Unity (C#) - Y. T. Elashry
# It would be appreciated if you send me how you have used this in your projects (e.g. Machine Learning) at youssef.elashry@gmail.com

# Use at your own risk
# Use under the Apache License 2.0

# Example of a Python UDP server

import UdpComms as U
import time
from Trinity_Backend import AiConvo
import os

# Create UDP socket to use for sending (and receiving)
sock = U.UdpComms(udpIP="127.0.0.1", portTX=8000, portRX=8001, enableRX=True, suppressWarnings=True)

agent = AiConvo.AiConvo()

while True:
    data = sock.ReadReceivedData() # read data "1 2"
    if data != None: # if NEW data has been received since last ReadReceivedData function call
        print(data)
        agent.get_script()
        convo_and_action = agent.get_convo_and_action(str(data))
        sock.SendData(convo_and_action) # Send this string to other application

    time.sleep(1)