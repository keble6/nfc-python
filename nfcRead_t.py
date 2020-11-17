
#!/usr/bin/python3
####    test nfcRead.py #######
import subprocess
import hexdump
from nfcLib import nfcReadNtag2
    
print(" Place a tag near the Reader")
print(" KEEP IT THERE until operation is completed!")

fname="Ntag2.mfd"
returnCode = nfcReadNtag2(fname)

if(returnCode != 0):
    print("No tag found - keep it there longer?")
else:
    # now read dump the file
    print("Success!")
    f=open(fname,"br")
    #f = open("./Ntag2.mfd","br") #open for read as a binary file
    binary = f.read()
    data = list(binary) #convert to a list
    #
    print("Page")
    for page in range(0,45):
        binary=data[page+0:page+4]
        print(str(page).zfill(2),': ', end='')
        for number in binary:
            print('0x' + hex(number)[2:].zfill(2),' ',end='')
        print()

        
        
