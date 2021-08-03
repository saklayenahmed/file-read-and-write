import os
absPath = os.path.dirname(os.path.abspath(__file__))

file = absPath+'/inputFile.txt'
path = os.path.abspath(file)
print(path)

f = open(file , 'r')
passFile= open(absPath+'/passFile.txt','w')
failFile =open(absPath+'/failFile.txt','w')
count = 0
for line in f:
    line_spilt = line.split()
    if line_spilt[2] =='P':
        passFile.write(line)
    else:
        failFile.write(line)
f.close()
passFile.close()
failFile.close()

