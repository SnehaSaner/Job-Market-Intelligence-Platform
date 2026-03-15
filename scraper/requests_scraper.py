from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)

# NEW PART — multiple job searches
search_terms = [
    "data analyst",
    "business analyst",
    "power bi analyst",
    "sql analyst",
    "data analytics"
]

job_data = []

for term in search_terms:

    url = f"https://www.indeed.com/jobs?q={term.replace(' ','+')}"

    print("Searching for:", term)

    driver.get(url)

    time.sleep(5)

    jobs = driver.find_elements(By.CSS_SELECTOR, "div.job_seen_beacon")

    print("Jobs found:", len(jobs))

    for job in jobs:

        try:
            title = job.find_element(By.CSS_SELECTOR, "h2").text
        except:
            title = "NA"

        try:
            company = job.find_element(By.CSS_SELECTOR, "[data-testid='company-name']").text
        except:
            company = "NA"

        try:
            location = job.find_element(By.CSS_SELECTOR, "[data-testid='text-location']").text
        except:
            location = "NA"

        job_data.append({
            "job_title": title,
            "company": company,
            "location": location
        })

driver.quit()

df = pd.DataFrame(job_data)

df.to_csv("jobs_data.csv", index=False)

print("Total jobs collected:", len(df))