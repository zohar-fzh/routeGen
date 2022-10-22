import wget
import os
from fnmatch import fnmatch

files = os.listdir(".")
for file in files:
    if(fnmatch(file,'cn-aggregated*')):
        os.remove(file)

if (os.path.exists("./target")):
    files = os.listdir("./target")
    for file in files:
        if(fnmatch(file,'windows*')):
            os.remove("./target/"+file)
        if(fnmatch(file,'linux*')):
            os.remove("./target/"+file)
else:
    os.mkdir("./target")

url = 'http://www.ipdeny.com/ipblocks/data/aggregated/cn-aggregated.zone'
wget.download(url)

sourceFile = open('./cn-aggregated.zone')

targetFile1 = open("./target/windowsAddRoute.bat",mode = 'w')
targetFile2 = open("./target/windowsDelRoute.bat",mode = 'w')

targetFile3 = open("./target/linuxAddRoute.sh",mode = 'w')
targetFile4 = open("./target/linuxDelRoute.sh",mode = 'w')

lines = sourceFile.read().splitlines()
for line in lines:
    targetFile1.write("route add -p ")
    targetFile1.write(line)
    targetFile1.write(" 192.168.0.1\n")

    targetFile2.write("route delete ")
    targetFile2.write(line+"\n")

    targetFile3.write("ip route add ")
    targetFile3.write(line)
    targetFile3.write(" via 192.168.0.1\n")

    targetFile4.write("ip route del ")
    targetFile4.write(line+"\n")

sourceFile.close()
targetFile1.close()
targetFile2.close()
targetFile3.close()
targetFile4.close()
