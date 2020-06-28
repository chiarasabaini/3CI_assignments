"""GETINFO"""

__author__ = "Sabaini Chiara 3CI"
__version__ = "01.01"
__date__ = "2020-05-16"

import wmi
import time
from datetime import datetime

def main():
    start_time = time.time()
    print("Start time: " + str(datetime.now()))
    
    getinfo()

    print("Done")
    print("End time: " + str(datetime.now()))
    print("Execution time: " + str(time.time() - start_time) + 's')
    print("")
   

def getinfo():

    c = wmi.WMI(".")

    colNetProtocol = c.Win32_NetworkProtocol()
    colNetClient = c.Win32_NetworkClient()

    for item in colNetProtocol:
        print(f"Caption: {item.Caption}")
        print(f"Description: {item.Description}")
        print(f"Install date: {item.InstallDate}")
        print(f"Status: {item.Status}")
        print(f"Guarantees delivery: {item.GuaranteesDelivery}")
        print(f"Name: {item.Name}")
        print(f"Maximum address size: {item.MaximumAddressSize}")
        print(f"Maximum message size: {item.MaximumMessageSize}")

    for item in colNetClient:
        print(f"Caption: {item.Caption}")
        print(f"Description: {item.Description}")
        print(f"Install date: {item.InstallDate}")
        print(f"Status: {item.Status}")
        print(f"Manufacturer: {item.Manufacturer}")
        print(f"Name: {item.Name}")

if __name__ == "__main__":
    main()