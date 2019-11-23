import os
import sys

try:
    from MRT import*
except Exception as rtbloaderror:
    rtberror = rtbloaderror
    loaderror = True
else:
    loaderror = False
if sys.platform.startswith('win32'):
    clear = lambda: os.system('cls')
elif sys.platform.startswith('linux'):
    clear = lambda: os.system('clear')

while True:
    clear()
    print("===========================")
    print("raid tool DIAGNOSIS TOOL")
    print("===========================")
    try:
        print("MRT Version: {}\nSM Version: {}".format(mrtversion,smversion))
    except Exception:
        print("MRT was unable to start")
    print("===========================")
    if loaderror:
        print("There was an error with MRT:")
        print(rtberror)
        print("===========================")
    print("0. Console")
    print("1. Attempt to start menu")
    print("2. Run Diagnostics Test")
    print("3. Run Update")
    s = input(">")
    try:
        if int(s) == 0:
            clear()
            print("0. Back")
            while True:
                try:
                    com = input(">")
                    if com == '0':
                        break
                    exec(com)
                except Exception as e:
                    print(e)
        elif int(s) == 1:
            main(currentattacks)
        elif int(s) == 2:
            diagrun(currentattacks)
        elif int(s) == 3:
            run_update()
    except Exception as e:
        print(e)
        input()
