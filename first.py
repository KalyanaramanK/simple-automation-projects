import pyautogui
import time
import subprocess

# Open Notepad
subprocess.Popen('notepad.exe')
time.sleep(2)  # wait for Notepad to open

# Text to type
text = """AUTOMATION USING PYTHON

This paragraph is automatically typed using Python.
It demonstrates automation of simple text-processing tasks.
"""

# Type text
pyautogui.write(text, interval=0.05)

# Save file (Ctrl + S)
pyautogui.hotkey('ctrl', 's')
time.sleep(1)

# Enter file name
pyautogui.write('C:\\Users\\Public\\automation_notepad.txt')
time.sleep(1)

# Press Enter to save
pyautogui.press('enter')

print("Notepad automation completed!")