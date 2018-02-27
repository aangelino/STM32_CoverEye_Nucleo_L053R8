import usb.core
import usb.util

# find our device
dev = usb.core.find(idVendor=0x0483, idProduct=0x5750)
if not dev:

    exit(1)
print (dev)
print ("="*50)
