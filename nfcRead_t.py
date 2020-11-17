#!/usr/bin/python3
####    test nfcRead.py #######
import subprocess
import hexdump
from nfcRead import nfcReadNtag2

########################################
# several python versions of hexdump don't work with the tag:
# UnicodeDecodeError: 'utf-8' codec can't decode bytes in position 3-4: invalid continuation byte
# But bash and "pip install hexdump" DO work:
# python version:
# pip install hexdump
#$ python3 -m hexdump Ntag2.mfd 
#00000000: 04 2C 4C EC A2 72 63 80  33 48 00 00 E1 10 12 00  .,L..rc.3H......
#00000010: 01 03 A0 0C 34 03 00 FE  00 00 00 00 00 00 00 00  ....4...........
#00000020: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................
#00000030: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................
# bash version
#pi@rpi4:~/nfc/python $ hexdump Ntag2.mfd 
#0000000 2704 e04b 72a2 8063 4833 0000 10e1 0012
#0000010 0301 0ca0 0334 fe00 0000 0000 0000 0000
#0000020 0000 0000 0000 0000 0000 0000 0000 0000
#*
#0000040

    
print(" Place a tag near the Reader")
print(" KEEP IT THERE until operation is completed!")

fname="Ntag2.mfd"
returnCode = nfcReadNtag2(fname)

if(returnCode != 0):
        print("No tag found - keep it there longer?")
else:
# now read dump the file
        print("Success!")
        f=open(fname,"r")
        #data=(f.read())
        hex(f.read(),2, ' ')
        
        
