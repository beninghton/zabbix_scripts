#!/usr/bin/python
import os
import json
import re

if __name__ == "__main__":
    # Iterate over all block devices, but ignore them if they are in the
    # skippable set
    #skippable =  (r'/\d+/')
    skippable = os.listdir("/sys/class/block")
    #print (skippable)
    result = []
    for l in skippable:
        match = re.search(r'\d+',l)
        if not match:
            result += [l]	
    #print (result)			
    #skippable = ("sr", "loop", "ram")
    #skippable = (r'^[0-9]+$')
    #devices = (device for device in os.listdir("/sys/class/block")
    #           if not any(ignore in device for ignore in skippable))
   	
    data = [{"{#DEVICENAME}": device} for device in result]
    print(json.dumps({"data": data}, indent=4))
