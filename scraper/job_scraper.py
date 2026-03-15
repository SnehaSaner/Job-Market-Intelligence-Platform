from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)

job_data = []

for page in range(0, 30, 10):   # scrape 5 pages

    url = f"https://www.indeed.com/jobs?q=data+analyst&l=India&start={page}"
    driver.get(url)

    wait = WebDriverWait(driver, 10)

    jobs = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.job_seen_beacon"))
    )

    print("Jobs found on page:", len(jobs))

    for job in jobs:

        title = job.find_element(By.CSS_SELECTOR, "h2").text

        try:
            company = job.find_element(By.CSS_SELECTOR, "[data-testid='company-name']").text
        except:
            company = "NA"

        try:
            location = job.find_element(By.CLASS_NAME, "companyLocation").text
        except:
            location = "NA"

        job_data.append({
            "job_title": title,
            "company": company,
            "location": location
        })

    import random
    time.sleep(random.randint(6,12))

driver.quit()

df = pd.DataFrame(job_data)

df.to_csv("jobs_data.csv", index=False)

print("Total jobs collected:", len(df))