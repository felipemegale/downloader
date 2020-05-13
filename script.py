import os
import sys

def find_ts_files(filename):
    if filename.find('.ts') > -1:
        return True
    return False

files = os.listdir("./")
files.sort()
ts_files = list(filter(find_ts_files, files))

tempVideo = b''

for file in ts_files:
    videoPart = open(file, 'rb')
    print("READING PART {}...".format(file))
    part = videoPart.readlines()
    tempVideo += b"".join(part)
    print("READING PART {} OK".format(file))

print("WRITING TO FILE {}".format(sys.argv[1]))
aggregatedVideo = open(sys.argv[1], 'wb')
aggregatedVideo.write(tempVideo)
aggregatedVideo.close()
print("WRITING TO FILE {} OK".format(sys.argv[1]))
