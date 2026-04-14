import pyautogui
import time

# Add delay between actions (human-like)
pyautogui.PAUSE = 0.5

# -----------------------------
# Step 1: Open Start Menu
# -----------------------------
pyautogui.press('win')
time.sleep(1)

# Type application name (example: Notepad)
pyautogui.write('notepad', interval=0.1)
time.sleep(1)

# Press Enter to open
pyautogui.press('enter')
time.sleep(2)

# -----------------------------
# Step 2: Mouse Click (focus area)
# -----------------------------
pyautogui.click(500, 300)  # adjust coordinates if needed

# -----------------------------
# Step 3: Type Text
# -----------------------------
text = """This is a human-like automation script.
It simulates typing, clicking, and scrolling using Python.
"""

pyautogui.write(text, interval=0.05)

# -----------------------------
# Step 4: Scroll Content
# -----------------------------
pyautogui.scroll(-300)  # scroll down
time.sleep(1)
pyautogui.scroll(300)   # scroll up

# -----------------------------
# Step 5: Take Screenshot
# -----------------------------
screenshot = pyautogui.screenshot()
screenshot.save("automation_screenshot.png")

print("Screenshot saved!")

# -----------------------------
# Step 6: Close Application
# -----------------------------
pyautogui.hotkey('alt', 'f4')
time.sleep(1)

# Don't save (press 'Don't Save' → usually 'n')
pyautogui.press('n')

print("Automation completed!")