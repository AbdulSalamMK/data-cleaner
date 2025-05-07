import pandas as pd
import re

# Step 1: Load the CSV file
df = pd.read_csv("feedback.csv")

# Step 2: Remove duplicate rows
df = df.drop_duplicates()

# Step 3: Fill missing values in 'feedback' column
df['feedback'] = df['feedback'].fillna("No feedback")

# Step 4: Normalize text - lowercase and remove special characters
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)  # Keep only letters, numbers, and spaces
    return text.strip()

df['feedback'] = df['feedback'].apply(clean_text)

# Step 5: Save the cleaned data to a new CSV
df.to_csv("cleaned_feedback.csv", index=False)

print("✅ Cleaned feedback saved to 'cleaned_feedback.csv'")
