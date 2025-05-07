# 🧹 Data Cleaner – Customer Feedback

This Python script cleans a CSV file of customer feedback. It removes duplicates, fills missing values, and normalizes the text (lowercase, no special characters).

---

## 📦 Features

- ✅ Removes duplicate rows
- ✅ Fills missing feedback with a placeholder
- ✅ Converts text to lowercase
- ✅ Removes special characters
- ✅ Exports cleaned data to CSV and Excel

---

## 🔧 Requirements

- Python 3.x  
- pandas (install with `pip install pandas`)

---

## 🚀 How to Use

1. Place your `feedback.csv` in the project folder  
2. Run the script:

```bash
python data_cleaner.py
```

3. Outputs:
- `cleaned_feedback.csv`
- `cleaned_feedback.xlsx`

---

## 📄 Sample Input (`feedback.csv`)

```csv
id,feedback
1,Great service!
2,LOVED it!!
3,
4,great service!
5,Okay experience.
```

---

## 📂 Output Example

```csv
id,feedback
1,great service
2,loved it
3,no feedback
5,okay experience
```

---

## 👨‍💻 Author

**Abdul Salam** — Python & Data Analytics Freelancer  
📬 Open to freelance projects and collaborations
