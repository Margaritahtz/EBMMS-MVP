from http.client import REQUESTED_RANGE_NOT_SATISFIABLE
import json
#import requests
#import redis
import websocket
import asyncio
import serial
from serial import Serial
import random, time
import ast

ws= websocket.WebSocket()


ws.connect('ws://localhost:8000/ws/polData/')

ser = serial.Serial('COM5',9600)
ser.close()
ser.open()
while True:

    data = ser.readline()
    #print(data)
    data.decode('utf-8')
    value=str(data.decode('utf-8'))
    print(value)
    
    #parsed = json.loads(value)
     

    #result = ast.literal_eval(value)
    
    # values_master_list = []

    result = ast.literal_eval(value)

    
    time.sleep(3)

    ws.send(json.dumps({'value':result}))


# for i in range(1000):
#     time.sleep(3)

#     ws.send(json.dumps({'value': random.randint(1,10)}))


    # 'x':'',
    #         'y':'',
    #         'z':'',
    #         'temp':'',
    #         'strain':'',
    #         'humidity':''
