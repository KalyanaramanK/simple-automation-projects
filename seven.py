from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


# -----------------------------
# Setup Chrome Driver
# -----------------------------
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


# Open YouTube
driver.get("https://www.youtube.com")


# -----------------------------
# Search Keyword
# -----------------------------
keyword = "Python automation"

search_box = driver.find_element(By.NAME, "search_query")
search_box.send_keys(keyword)
search_box.send_keys(Keys.RETURN)

time.sleep(5)

# -----------------------------
# Extract Video Data
# -----------------------------
videos = driver.find_elements(By.XPATH, '//*[@id="video-title"]')

titles = []
channels = []

for i, video in enumerate(videos[:10]):
    titles.append(video.text)

    try:
        channel = video.find_element(By.XPATH, '../../..//*[@id="channel-name"]').text
    except:
        channel = "Not Found"

    channels.append(channel)

# -----------------------------
# Save to Excel
# -----------------------------
df = pd.DataFrame({
    "Title": titles,
    "Channel": channels
})

df.to_excel("youtube_results.xlsx", index=False)

print("✅ Data saved to youtube_results.xlsx")

# Close browser
driver.quit()