#!/usr/bin/python3
import subprocess
#read a NTag2(aka mifare ultralight) tag dump all data in file fname
def nfcReadNtag2(fname):
    # call shell command - see https://www.mankier.com/1/nfc-mfclassic
    subP = subprocess.Popen(["nfc-mfultralight", "r", fname],  stdout=subprocess.PIPE , stderr=subprocess.PIPE)
    stdout, stderr = subP.communicate()
    #if(subP.returncode != 0):
        #print("No tag found - keep it there longer?")
    #print("read return code",subP.returncode)
    #print("read output is:", stdout)
    return (subP.returncode) #0 if OK
