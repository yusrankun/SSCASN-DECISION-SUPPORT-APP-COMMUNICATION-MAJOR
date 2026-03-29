# 🎯 CPNS Recommendation System - Communication Studies

A **Streamlit-based application** to help users find the most suitable CPNS (Indonesian civil servant) positions based on:

* 💰 Salary
* 📍 Location
* 🏢 Institution
* ⚔️ Competition level

The dataset is collected from the official SSCASN (BKN) portal and focuses on **Communication Studies graduates**.

---

## 🚀 Features

* 🔎 Filter by province
* 💰 Minimum salary filter
* 🏢 Institution filter (optional)
* 🧠 Recommendation system based on scoring
* 📊 Interactive data table
* 📥 Download filtered results

---

## 🧠 Scoring Logic

The recommendation score is calculated using:

score = salary_avg / (competition_ratio + 1)

Where:

* salary_avg = average of minimum and maximum salary
* competition_ratio = number of applicants / number of positions

👉 Higher score means:

* Higher salary
* Lower competition

---

## 📂 Project Structure

project/
│
├── app.py
├── raw_cpns_ilmu_komunikasi.csv
├── requirements.txt
└── README.md

---

## ▶️ Installation & Run

### 1. Clone repository

git clone https://github.com/username/cpns-recommender.git
cd cpns-recommender

### 2. Install dependencies

pip install -r requirements.txt

### 3. Run the app

streamlit run app.py

---

## 📊 Dataset

* Source: SSCASN BKN API
* Major: Communication Studies
* Total data: ~5352 job positions

### Data fields include:

* Institution
* Job position
* Location
* Salary (min & max)
* Number of positions
* Number of applicants

---

## 🧠 Future Improvements

* 📊 Data visualization (EDA dashboard)
* 🌍 Map-based visualization
* 🤖 Machine learning-based recommendation
* 🧩 Multi-major support
* 📈 Trend analysis across institutions

---

## 📸 Preview

Add application screenshots here

---

## 🏆 Use Cases

This project is suitable for:

* Data Science portfolio
* Decision Support System
* Exploratory Data Analysis (EDA)
* Real-world public sector data analysis

---

## 👨‍💻 Author

Created by: **[Your Name]**

---

## ⭐ Notes

This project uses publicly available data from SSCASN for educational and analytical purposes.
