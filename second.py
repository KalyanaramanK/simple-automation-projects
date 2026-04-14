import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Load Excel file
file_path = "students.xlsx"
df = pd.read_excel(file_path)

# Function to calculate concession
def calculate_concession(row):
    concession = 0

    # Marks-based
    if row['Marks'] >= 90:
        concession += 50
    elif row['Marks'] >= 75:
        concession += 30

    # Income-based
    if row['Income'] < 100000:
        concession += 20

    # Category-based
    if row['Category'] in ['SC', 'ST']:
        concession += 25
    elif row['Category'] == 'OBC':
        concession += 10

    return min(concession, 100)

# Apply rules
df['Concession (%)'] = df.apply(calculate_concession, axis=1)

# Save Excel report
output_excel = "concession_report.xlsx"
df.to_excel(output_excel, index=False)

print("Excel report generated!")

# -----------------------------
# Generate PDF Report
# -----------------------------
output_pdf = "concession_report.pdf"
c = canvas.Canvas(output_pdf, pagesize=letter)

y = 750
c.setFont("Helvetica", 12)

c.drawString(50, y, "Student Concession Report")
y -= 30

for index, row in df.iterrows():
    line = f"{row['Name']} | Marks: {row['Marks']} | Income: {row['Income']} | Category: {row['Category']} | Concession: {row['Concession (%)']}%"
    c.drawString(50, y, line)
    y -= 20

    if y < 50:  # New page if needed
        c.showPage()
        y = 750

c.save()

print("PDF report generated!")
#Eligibility Rules (Example)
# Marks ≥ 90 → 50% concession
#🎓 Marks ≥ 75 → 30% concession
#💰 Income < 1,00,000 → +20% extra
#🏷 SC/ST → +25% extra
#🏷 OBC → +10% extra
#Max concession = 100%