import ctypes
import platform
import os
import datetime
import json


def parseJSON():
    with open("checkFreeMB.json", 'r') as fjson:
        initJson = json.load(fjson)
    return initJson


def outJSON(data, outpath):
    with open(outpath, 'w') as f:
        json.dump(data, f, sort_keys=False, default=str)
        # f.write(data)


def get_free_space_mb(pathlist):
    """Return folder/drive free space (in megabytes)."""
    if platform.system() == 'Windows':
        freelist = list()
        free_bytes = ctypes.c_ulonglong(0)

        for path in pathlist:
            ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(path), None, None, ctypes.pointer(free_bytes))
            freelist.append(free_bytes.value / 1024 / 1024)
        return freelist
    else:
        freelist = list()
        for path in pathlist:
            st = os.statvfs(path)
            freelist.append(st.f_bavail * st.f_frsize / 1024 / 1024)
        return freelist


def main():
    initJson = parseJSON()
    pathlist = initJson['PATH']
    outpath = initJson['OUTPUT']
    currentTime = datetime.datetime.now()
    if (len(pathlist) == 0 or pathlist == None):
        print
        "please add path in .json"
        exit(1)
    freelist = get_free_space_mb(pathlist)
    jsondict = {'timestamp': currentTime, 'path': pathlist, 'free': freelist}
    outJSON(jsondict, outpath)

main()