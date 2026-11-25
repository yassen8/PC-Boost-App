# PC Booster App

I originally created this project in 2024 for my friend. I decided to upload it on github now (Partially because I'm learning about git and how to use it).

The code written in this project is from 2024 and I'm not going to update it.

## **How to run**

1. Keep `main.py` and `Icon.ico` in the **same folder**
    - Since I'm using tkinter, the app needs `Icon.ico` in its working directory to run, otherwise it'll throw an error since it can't find the icon file.
2. Run the script with Python as administrator:
    ```bash
    python "main.py"
    ```
3. Make sure you're running `main.py` as administrator, otherwise the app won't have the permission needed to run most of the code.

- Keep in mind that this app is Windows-only

## **How it works**

### The app boosts your pc in 6 steps

1. Flushes DNS
2. Stops SysMain
3. Disables SysMain Startup
4. Cleans the recycle bin
5. Cleans temp files (Including Windows temp files, AppData temp files, and Prefetch)
6. Cleans Windows log files

### About SysMain

- SysMain is a built-in Windows background service that watches what apps you open and pre-loads them into RAM to speed up future launches.

- Turning SysMain off helps your PC by cutting background disk and memory overhead, freeing up resources when you actually need them instead of letting Windows keep preloaded data sitting around.

## **How to use it**

1. Make sure you're running `main.py` as administrator
2. Press the **boost** button
3. If you want to re-enable SysMain, press the **reset** button

- The **reset** button re-enables SysMain service, and re-enables SysMain Startup.