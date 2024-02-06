import paho.mqtt.client as mqtt
import numpy as np
from PIL import Image
import json

import serial
from time import sleep

import signal
import sys

ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)

state = 0


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected.")
        client.subscribe("Group_10/predict")
    else:
        print("Failed to connect. Error code: %d." % rc)


dataarr = [0] * 31


def on_message(client, userdata, msg):
    # print("Received message from server.")
    global dataarr
    dataarr = json.loads(msg.payload)


def setup(hostname):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(hostname, 1883, 60)
    client.loop_start()
    return client


arra = [0] * 30

num = 0


def update():
    print("Update")
    global arra
    global num
    arra = [0] * 30 
    num = dataarr[0]
    i = 0
    while i < dataarr[0]:
        temp1 = dataarr[i * 6 + 1]
        arra[temp1 * 6], arra[temp1 * 6 + 2], arra[temp1 * 6 + 3], arra[temp1 * 6 + 4], arra[temp1 * 6 + 5] = \
            temp1, dataarr[i * 6 + 3], dataarr[i * 6 + 4], dataarr[i * 6 + 5], dataarr[i * 6 + 6]
        arra[temp1 * 6 + 1] = dataarr[i * 6 + 2]
        i += 1
    print("Update2")

counter = 0

flago = False

def search():  # 0
    global counter
    global flago
    global state
    if counter < 1:
        user = 'o'
        flago = True
        ser.write(user.encode('utf-8'))
    elif counter < 30:
        sleep(0.2) 
    elif counter == 30:
        user = 'o'
        flago = False
        ser.write(user.encode('utf-8'))
        sleep(0.2)
    elif counter < 36:
        user = 'd'
        ser.write(user.encode('utf-8'))
        sleep(0.2)
    elif counter < 41:
        user = 'x'
        ser.write(user.encode('utf-8'))
        sleep(0.2)
    elif counter < 46:
        user = 'd'
        ser.write(user.encode('utf-8'))
        sleep(0.2)
    elif counter < 51:
        user = 'x'
        ser.write(user.encode('utf-8'))
        sleep(0.2)
    elif counter < 56:
        user = 'd'
        ser.write(user.encode('utf-8'))
        sleep(0.2)
    elif counter < 61:
        user = 'x'
        ser.write(user.encode('utf-8'))
        sleep(0.2)
    elif counter < 66:
        user = 'd'
        ser.write(user.encode('utf-8'))
        sleep(0.2)
    elif counter < 71:
        user = 'x'
        ser.write(user.encode('utf-8'))
        sleep(0.2)
    elif counter == 71:
        counter = -1
    counter += 1

    if dataarr[0] > 0:
        if flago:
            user = 'o'
            flago = False
            ser.write(user.encode('utf-8'))
        state = 1
        counter = 0


type1 = None


def toGarbage():  # 1
    global type1
    global counter
    global state

    mid = -1
    for i in range(0, 5):
        if arra[6 * i + 1] != 0:
            type1 = i
            mid = (arra[6 * i + 2]+arra[6 * i + 4])/2
            break

    if mid < 0:
        print("erro mid")
        return
    elif mid < 0.4:
        user = 'a'
        ser.write(user.encode('utf-8'))
    elif mid < 0.6:
        if type1 == 0:  # coin
            if counter < 1:
                user = 'h'
                ser.write(user.encode('utf-8'))

            elif counter < 15:
                user = 'w'
                ser.write(user.encode('utf-8'))
            else:  
                state = 0
                counter = 0
                user = 'j'
                ser.write(user.encode('utf-8'))
                print("coin get")
                return
        elif type == 4:  # water
            if counter < 1:
                user = 'k'
                ser.write(user.encode('utf-8'))
            elif counter < 20:
                user = 'w'
                ser.write(user.encode('utf-8'))
            else:
                state = 0
                counter = 0
                user = 'l'
                ser.write(user.encode('utf-8'))
                return
        else: 

            if counter < 15:
                user = 'w'
                ser.write(user.encode('utf-8'))
            else: 


                user = 'h'
                ser.write(user.encode('utf-8'))
                sleep(2)
                state = 2 
                counter = 0
                return

        counter += 1 
    else:
        user = 'd'
        ser.write(user.encode('utf-8'))
    sleep(0.2)


def turn():  # 2
    global counter
    global state

    if counter < 20:
        user = 'd'
        ser.write(user.encode('utf-8'))
        sleep(0.2)
        counter += 1
    else:
        counter = 0
        state = 3 


def searchR():  # 3  
    global counter
    global flago
    global state
    if counter < 1:
        user = 'o'
        flago = True
        ser.write(user.encode('utf-8'))
    elif counter < 30:
        pass
    elif counter == 30:
        user = 'o'
        flago = False
        ser.write(user.encode('utf-8'))
    elif counter < 36:
        user = 'd'
        ser.write(user.encode('utf-8'))
    elif counter < 41:
        user = 'x'
        ser.write(user.encode('utf-8'))
    elif counter < 46:
        user = 'd'
        ser.write(user.encode('utf-8'))
    elif counter < 51:
        user = 'x'
        ser.write(user.encode('utf-8'))
    elif counter < 56:
        user = 'd'
        ser.write(user.encode('utf-8'))
    elif counter < 61:
        user = 'x'
        ser.write(user.encode('utf-8'))
    elif counter < 66:
        user = 'd'
        ser.write(user.encode('utf-8'))
    elif counter < 71:
        user = 'x'
        ser.write(user.encode('utf-8'))
    elif counter == 71:
        counter = -1
    counter += 1
    sleep(0.2)
    if arra[6*type1+1] > 2:
        if flago:
            user = 'o'
            flago = False
            ser.write(user.encode('utf-8'))
        state = 4
        counter = 0


def returnTo():  # 4
    global type1
    global counter
    global state
    mid = (arra[6 * type1 + 2] + arra[6 * type1 + 4]) / 2

    if mid < 0.4:
        user = 'a'
        ser.write(user.encode('utf-8'))
        counter += 1
    elif mid < 0.6:
        if counter < 25:
            user = 'w'
            ser.write(user.encode('utf-8'))
            counter += 1
        else:  
            state = 5
            counter = 0
            user = 'j'
            ser.write(user.encode('utf-8'))
            return
    else:
        user = 'd'
        ser.write(user.encode('utf-8'))
        counter += 1
    sleep(0.2)

def turnR():  # 5
    global counter
    global state

    if counter < 10:
        user = 's'
        ser.write(user.encode('utf-8'))
        counter += 1
    elif counter < 22:
        user = 'd'
        ser.write(user.encode('utf-8'))
        counter += 1
    else:
        counter = 0
        state = 0
    sleep(0.2)

# ###############


def main():
    global state

    client = setup("192.168.43.143")
    PATH = "./"

    # Note: Serial port read/write returns "byte" instead of "str"
    #ser.write("testing serial connection\n".encode('utf-8'))
    #ser.write("sending via RPi\n".encode('utf-8'))




    while True:
        update()
        print("state:")
        print(state)
        print("\n")
        print("arra:")
        print(arra)
        print("\n")

        # ------状态机部分------
        if state == 0:
            search()
        elif state == 1:
            toGarbage()
        elif state == 2:
            turn()
        elif state == 3:
            searchR()
        elif state == 4:
            returnTo()
        elif state == 5:
            turnR()


if __name__ == '__main__':
    main()
