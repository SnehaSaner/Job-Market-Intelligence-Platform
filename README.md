# 📊 Job Market Intelligence Platform

A **full-stack analytics project** that collects live job postings for data and business analytics roles, extracts skill demand trends, and provides an interactive dashboard for analysis.  

---
## Screenshots :


## 🛠 Tech Stack

- **Python 3.12** — Data scraping, analysis, and ML  
- **Selenium** — Automates live job scraping from Indeed  
- **Pandas** — Data cleaning and analysis  
- **MySQL** — Database for storing structured job data  
- **Streamlit** — Interactive dashboard  
- **Matplotlib** — Visualization of skill trends  
- **Scikit-learn** — Basic ML model for role prediction  

---

## 🏗 Project Structure
job-market-intelligence-platform/
│
├── scraper/
│   └── job_scraper.py               # Selenium scraper for live job postings
│
├── analysis/
│   └── skill_extractor.py           # Analyzes skills from titles/data
│
├── database/
│   ├── db_connection.py             # MySQL connection setup
│   └── save_to_mysql.py             # Save scraped data to MySQL
│
├── ml_model/
│   └── skill_predictor.py           # Sample ML model predicting Power BI roles
│
├── dashboard/
│   └── dashboard.py                 # Streamlit interactive dashboard
│
├── docs/
│   └── project_overview.md          # Project overview & instructions
│
├── jobs_data.csv                     # Sample dataset scraped from Indeed
├── skill_demand.csv                  # Skill analysis output
└── README.md                         # Main GitHub project description


---

## ⚡ Features

1. **Automated Job Scraping**
   - Scrapes ~80+ live job postings for analytics roles.
   - Collects job title, company, location.

2. **Skill Analysis**
   - Detects top skills: SQL, Power BI, Python, Excel, Tableau, ML.
   - Outputs `skill_demand.csv`.

3. **Database Integration**
   - Stores structured job listings in MySQL.
   - Supports querying for top roles, companies, and locations.

4. **Interactive Dashboard**
   - Filters by location & company.
   - Visualizes skill demand, top hiring locations, top companies.
   - Scrollable table for job listings.

5. **ML Model (Optional)**
   - Predicts if a job title is a Power BI role.
   - Demonstrates basic machine learning workflow.

---

## 📈 How to Run

### 1. Scrape Jobs

```bash
python scraper/job_scraper.py
- Save Data to MySQL
  python database/save_to_mysql.py
- Analyze Skills
  python analysis/skill_extractor.py
- Run Dashboard
  streamlit run dashboard/dashboard.py

## Key Insights

Power BI and SQL are highly demanded in analytics roles.

Data Analyst roles dominate the job market.

Dashboard allows exploration by location, company, and skills.
