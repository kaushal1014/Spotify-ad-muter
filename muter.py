from pycaw.pycaw import AudioUtilities 
import os,threading,time,ctypes
from win10toast import ToastNotifier
import multiprocessing,threading

toaster = ToastNotifier()
def notification():
    toaster.show_toast("Spotify", "ad incoming gonna mute it master", threaded=True,
                   icon_path="spotify.ico", duration=4)  
    time.sleep(40)

#NotiProcess=multiprocessing.Process(target=notification)





while True:
    NotiProcess=threading.Thread(target=notification)
    EnumWindows = ctypes.windll.user32.EnumWindows    
    EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
    GetWindowText = ctypes.windll.user32.GetWindowTextW
    GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
    IsWindowVisible = ctypes.windll.user32.IsWindowVisible
    
    time.sleep(5)      
    titles = [] 
    def foreach_window(hwnd, lParam):
        if IsWindowVisible(hwnd):
            length = GetWindowTextLength(hwnd)
            buff = ctypes.create_unicode_buffer(length + 1)
            GetWindowText(hwnd, buff, length + 1)
            titles.append(buff.value)
        return True
    EnumWindows(EnumWindowsProc(foreach_window), 0)
    if "Advertisement" in titles:  
        sessions = AudioUtilities.GetAllSessions()
        if NotiProcess.is_alive()==True:
            pass
        else:
            NotiProcess.start()
        
        for session in sessions:
            
            volume = session.SimpleAudioVolume
            volume.SetMute(1, None)
    elif "Spotify" in titles:      
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            volume = session.SimpleAudioVolume
            volume.SetMute(1, None)
    else:
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            volume = session.SimpleAudioVolume
            volume.SetMute(0, None)





