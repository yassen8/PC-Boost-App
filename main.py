from tkinter import *
import os
import pathlib
import shutil
import time

BACKGROUND = "#00abc9"
root = Tk()
root.title("Yassen's Pc Boost App")
root.configure(bg=BACKGROUND)
root.iconbitmap("Icon.ico")
SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()
root.geometry("{}x{}+0+0".format(SCREEN_WIDTH, SCREEN_HEIGHT))

Label(root, text="Sup", bg=BACKGROUND, fg="black", font=("Comic Sans MS", 50, "bold")).pack()
Label(root, text="Click on the button to boost your pc (please don't spam 🙏)", bg=BACKGROUND, fg="black", font=("Comic Sans MS", 30, "bold")).pack()
Label(root, text="Please make sure to run the program as administrator, without it the program won't have premission to delete certain files", bg=BACKGROUND, fg="black", font=("Comic Sans MS", 15, "bold")).pack()
Label(root, text="----------------------------------------------------------------------------------------------------------------------------", bg=BACKGROUND, fg="black", font=("Comic Sans MS", 15, "bold")).pack()
Feedback_Frame = Frame(root, bg=BACKGROUND, width=int((SCREEN_WIDTH * (30 / 100))), height=int((SCREEN_HEIGHT * (70 / 100))))
Feedback_Frame.pack(side="right", anchor="e", padx=int((SCREEN_WIDTH * (15 / 100))))
def FeedBack(feedback, color):
    new_label = Label(Feedback_Frame, text=feedback, bg=BACKGROUND, fg=color, font=("Comic Sans MS", int(((SCREEN_WIDTH + SCREEN_HEIGHT) * (0.55 / 100))), "bold"), wraplength=int((SCREEN_WIDTH * (30 / 100))))
    new_label.pack(pady=int((SCREEN_HEIGHT * (0.5 / 100))))
    root.after(5000, lambda: new_label.destroy())

def EndTask():
    try:
        root.destroy()
    finally:
        os._exit(0)

def CleanFolder(path):
    try:
        for file in pathlib.Path.iterdir(path):
            try:
                if file.is_file() or file.is_symlink():
                    os.remove(file)
                else:
                    shutil.rmtree(file, True)
            except Exception:
                continue
    except Exception:
        raise Exception
    
def Boost():
    try:
        FeedBack("Flushing DNS..", "white")
        if os.system("ipconfig /flushdns") == 0:
            FeedBack("DNS Flushed Successfully !", "#51FF00")
        else:
            FeedBack("Couldn't Flush DNS, Please make sure to open the app as administrator", "red")
        FeedBack("Stopping SysMain..", "white")
        if os.system('net stop "SysMain"') == 0:
            FeedBack("Stopped SysMain Successfully !", "#51FF00")
        else:
            FeedBack("Couldn't Stop Sysmain, Please make sure to open the app as administrator", "red")
        FeedBack("Disabling SysMain Startup..", "white")
        if os.system('sc config "SysMain" start=disabled') == 0:
            FeedBack("Disabled Sysmain Startup Successfully !", "#51FF00")
        else:
            FeedBack("Couldn't Disable Sysmain Startup, Please make sure to open the app as administrator", "red")
        FeedBack("Cleaning Recycle bin..", "white")
        if os.system('powershell.exe -NoProfile -Command "Clear-RecycleBin -Force"') == 0:
            FeedBack("Cleared Recycle bin Successfully !", "#51FF00")
        else:
            FeedBack("Couldn't Clean Recycle bin, Please make sure to open the app as administrator", "red")
    except Exception:
        FeedBack("Error while cleaning, Please make sure to open the app as administrator", "red")
    caches = {}
    temp = pathlib.Path(os.environ.get("TEMP"))
    if temp.exists(): caches["temp"] = temp
    ptemp = pathlib.Path(os.environ.get("SystemRoot")) / "Temp"
    if ptemp.exists() : caches["%temp%"] = ptemp
    prefetch = pathlib.Path(os.environ.get("SystemRoot")) / "Prefetch"
    if prefetch.exists(): caches["prefetch"] = prefetch
    logs = pathlib.Path(os.environ.get("SystemRoot")) / "Logs"
    if logs.exists(): caches["logs"] = logs
    log_files = pathlib.Path(os.environ.get("SystemRoot")) / "LogFiles"
    if log_files.exists: caches["log files"] = log_files
    for cache in caches:
        try:
            FeedBack(f"Cleaning {cache} Cache..", "white")
            CleanFolder(caches[cache])
            FeedBack(f"Cleaned {cache} Cache Successfully !", "#FFBB00")
        except Exception:
            FeedBack(f"Couldn't clean {cache} cache in {caches[cache]}, Please make sure to open the app as administrator", "red")
            continue

def Reset():
    SysMainStarted = False
    SysMainEnabled = False
    try:
        FeedBack("Starting SysMain..", "white")
        os.system('net start "SysMain"')
        SysMainStarted = True
        FeedBack("Started SysMain Successfully !", "#51FF00")
        FeedBack("Enabling SysMain Startup..", "white")
        os.system('sc config "SysMain" start=enabled')
        SysMainEnabled = True
        FeedBack("Enabled SysMain Startup Successfully !", "#51FF00")
    except Exception:
        if not SysMainStarted:
            FeedBack("Couldn't Start SysMain, Please make sure to open the app as administrator", "red")
        if not SysMainEnabled:
            FeedBack("Couldn't Enable SysMain Startup, Please make sure to open the app as administrator", "red")

Buttons_Frame = Frame(root, bg=BACKGROUND, border=2)
Buttons_Frame.pack(side="left", anchor="nw", pady=100)
Button(Buttons_Frame, text="Boost", bg="#00d9ff", fg="black", font=("Comic Sans MS", 40, "bold"), relief="groove", command=Boost).pack()
Button(Buttons_Frame, text="Reset Changes", bg="#B60000", fg="black", font=("Comic Sans MS", 20, "bold"), relief="groove", command=Reset).pack(pady=10)
root.protocol("WM_DELETE_WINDOW", EndTask)

while "__main__" == __name__:
    root.mainloop()