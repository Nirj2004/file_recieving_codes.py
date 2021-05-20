import cv2
import numpy as np
import math
import os






p=0
q=0

#Test_Server_py_START

import socket

s = scoket.socket(scoket.AF_INET, socket.SOCK_DGRAM)
S.CONNECT(("8.8.8.8", 80))
ip=s.getsockname)[0]

BC_PORT = 9012
#port for ip broadcast
import sys, time
from socket import *

s = socket(AF_INET, SOCK_DGRAM, 1)
s.blind(('', 0))
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
#Include IP headers: setsockopt
s.sendto(ip,('<broadcast>', BC_PORT))
#Send data to the socket



#Test_Server_py_END


cap = cv2.VideoCapture(0)
cam = 1 
while True:

    while(cam):
        ret, img = cap.read()
        cv2.rectangle(img,(250,250),(50,50),(0,255,0),1)
        crop
