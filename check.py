import psutil
import os
import time
import sys
import threading
def checkIfProcessRunning(processName):
    print("checking")
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False
    # Check if any Spotify process was running or not.
def RunMuter():
    time.sleep(3)
    os.system('python muter.py')


def is_running(script):
    for q in psutil.process_iter():
        if q.name().startswith('python'):
            if len(q.cmdline())>1 and script in q.cmdline()[1] and q.pid !=os.getpid():
                print("'{}' Process is already running".format(script))
                return True
                

    return False


def kill(script):
    os.system("")



try:
    while True:
        print("timer")
        if checkIfProcessRunning('spotify'):
            print("spotify is running")
            
            
            thread1=threading.Thread(target=RunMuter)
            

            if is_running("muter.py")==True:
                print("muter is running")
                pass
            
            else:
                print("muter is not running will start it")
                thread1.start()
            
            time.sleep(10)
            
            
        else:
            print('No Spotify process was running')
            time.sleep(10)
            kill("muter.py")
except KeyboardInterrupt:
    sys.exit()
