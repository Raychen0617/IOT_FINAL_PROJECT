# DAI2.py  -- new version of Dummy Device DAI.py, modified by tsaiwn@cs.nctu.edu.tw

# you can get from here:  https://goo.gl/6jtP41   ; Search dummy + iottalk  for other files

import time, DAN, requests, random 
import threading, sys
import os
import globals
import importlib
import sounddevice as sd
from numpy import linalg as LA
import numpy as np

# ServerURL = 'http://Your_server_IP_or_DomainName:9999' #with no secure connection

# ServerURL = 'http://192.168.20.101:9999' #with no secure connection

#  注意你用的 IoTtalk 伺服器網址或 IP 

ServerURL = 'https://7.iottalk.tw' #with SSL secure connection

# ServerURL = 'https://Your_DomainName' #with SSL connection  (IP can not be used with https)

Reg_addr = None  #if None, Reg_addr = MAC address



mac_addr = 'C86208BD218'  # put here for easy to modify;;  the mac_addr in DAN.py is NOT used

# Copy DAI.py to DAI2.py and then modify the above mac_addr, then you can have two dummy devices

Reg_addr = mac_addr   # Otherwise, the mac addr generated in DAN.py will always be the same !

DAN.profile['dm_name']='Weather_dummy'   # you can change this but should also add the DM in server
DAN.profile['df_list']=['wea_date'] 
DAN.profile['d_name']='0716230_sound'
DAN.device_registration_with_retry(ServerURL, Reg_addr)

# global gotInput, date

gotInput=False
date="haha"
allDead=False

###################################

#doRead read input from user

###################################

duration = 1 # seconds
global max_volume
max_volume = 0


def print_sound(indata=0, outdata=50, frames=1000, time=10, status=50):
    global gotInput, volume_norm    
    volume_norm = np.linalg.norm(indata)*10
    print (int(volume_norm))
    if(int(volume_norm)>10):
        max_volume = int(volume_norm)
        #
        #print("max volume = ",max_volume,"\n")
        DAN.push ('wea_date',max_volume,max_volume)
    
    
    gotInput = True


while True:

    with sd.Stream(callback=print_sound):
        sd.sleep(duration * 1000)

    if gotInput == True:
        #print ("push max volume",max_volume)
        gotInput = False

    try:    
        time.sleep(0.5)
        
    except KeyboardInterrupt:
        break

#creat a thread to do Input data from keyboard, by tsaiwn@cs.nctu.edu.tw
#threadx = threading.Thread(target=print_sound)
#threadx.daemon = True
#threadx.start()

'''
while True:
    
    try:



        if gotInput:
           
           print ("push max volume",max_volume)

           DAN.push ('wea_date',max_volume,max_volume)


           gotInput=False   # so that you can input again 

    except Exception as e:

        print(e)

        if str(e).find('mac_addr not found:') != -1:

            print('Reg_addr is not found. Try to re-register...')

            DAN.device_registration_with_retry(ServerURL, Reg_addr)

        else:

            print('Connection failed due to unknow reasons.')

            time.sleep(1)    

    try:

       time.sleep(0.2)

    except KeyboardInterrupt:

       break

time.sleep(0.5)

try: 

   DAN.deregister()

except Exception as e:

   print("===")

print("Bye ! --------------", flush=True)

sys.exit( )
'''