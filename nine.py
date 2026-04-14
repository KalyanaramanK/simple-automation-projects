import pandas as pd

# -----------------------------
# Load Excel file
# -----------------------------
file_path = "input.xlsx"
df = pd.read_excel(file_path)

# -----------------------------
# BMI Calculation Function
# -----------------------------
def calculate_bmi(weight, height):
    return round(weight / (height ** 2), 2)

# -----------------------------
# BMI Classification
# -----------------------------
def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# -----------------------------
# Apply Calculations
# -----------------------------
df["BMI"] = df.apply(lambda row: calculate_bmi(row["Weight (kg)"], row["Height (m)"]), axis=1)
df["Category"] = df["BMI"].apply(classify_bmi)

# -----------------------------
# Save Output Excel
# -----------------------------
output_file = "bmi_report.xlsx"
df.to_excel(output_file, index=False)

print("✅ BMI report generated successfully!")
print(df)