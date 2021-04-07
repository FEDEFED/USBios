from sys import argv
import os

usage='''
USBios 0.1
Usage: USBios [options] [payloadfile]

options:
    -l: long,large: Show working and guide the user in a graphical 
                interface (needs a good chunk of the screen)
    -s: short,small: Prints just Done (payloadfile needs to be specified, 
                if you do not knowhow to write the payload file use 'USBios -l')

'''

arg=True
try:
    t=argv[1]
except IndexError:
    print(usage)
    arg=False
if arg:
    if t=='-l':
        os.system('python3 LUSBios.py')
    elif t=='-s':
        os.system('python3 SUSBios.py '+argv[2]+' '+argv[3])
    else:
        print(usage)
