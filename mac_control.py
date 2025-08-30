import os
import pyautogui
import webbrowser
import time

def open_app(app_name):
    """Open an app using Spotlight search"""
    pyautogui.hotkey("command", "space")  # Open Spotlight
    time.sleep(0.5)
    pyautogui.typewrite(app_name)
    time.sleep(0.5)
    pyautogui.press("return")

def close_app(app_name):
    """Close an app using killall"""
    os.system(f"killall '{app_name}'")

def open_website(url):
    """Open website in default browser"""
    webbrowser.open(url)

def system_command(command):
    """Run any shell command"""
    os.system(command)
