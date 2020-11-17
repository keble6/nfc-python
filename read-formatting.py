f = open("./Ntag2.mfd","br") #open for read as a binary file
binary = f.read()
data = list(binary) #convert to a list
#
print("Page")
for page in range(0,45):
  binary=data[page+0:page+4]
  print(str(page).zfill(2),': ', end='')
  for number in binary:
    print('0x' + hex(number)[2:].zfill(2),' ', end='')
  print()
  
