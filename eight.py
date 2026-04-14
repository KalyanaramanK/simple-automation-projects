import requests
from bs4 import BeautifulSoup
import pandas as pd

# -----------------------------
# 1. Web Scraping
# -----------------------------
url = "http://books.toscrape.com/catalogue/page-1.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

products = soup.find_all("article", class_="product_pod")

data = []

for product in products:
    name = product.h3.a["title"]
    price = product.find("p", class_="price_color").text
    rating_class = product.find("p")["class"][1]  # e.g., "Three"

    data.append({
        "Name": name,
        "Price": price,
        "Rating": rating_class
    })

df = pd.DataFrame(data)

# -----------------------------
# 2. NLP Classification (Simple AI)
# -----------------------------
def classify_product(name):
    name = name.lower()

    if any(word in name for word in ["science", "physics", "chemistry"]):
        return "Education"
    elif any(word in name for word in ["love", "romance"]):
        return "Romance"
    elif any(word in name for word in ["mystery", "crime"]):
        return "Mystery"
    elif any(word in name for word in ["history", "war"]):
        return "History"
    else:
        return "General"

df["Category"] = df["Name"].apply(classify_product)

# -----------------------------
# 3. Save Output
# -----------------------------
df.to_csv("products.csv", index=False)
df.to_excel("products.xlsx", index=False)

print("✅ Data extracted and saved successfully!")
print(df.head())