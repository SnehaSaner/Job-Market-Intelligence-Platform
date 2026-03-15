import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Job Market Intelligence", layout="wide")

st.title("📊 Job Market Intelligence Dashboard")

# load datasets
jobs = pd.read_csv("../jobs_data.csv")
skills = pd.read_csv("../skill_demand.csv")

# clean data
jobs = jobs.dropna(subset=["job_title"])

# -------------------------
# FILTERS
# -------------------------

st.sidebar.header("Filters")

# Location filter
locations = jobs["location"].dropna().unique()
selected_location = st.sidebar.selectbox("Select Location", ["All"] + sorted(list(locations)))

if selected_location != "All":
    jobs = jobs[jobs["location"] == selected_location]

# Company filter
companies = jobs["company"].dropna().unique()
selected_company = st.sidebar.selectbox("Select Company", ["All"] + sorted(list(companies)))

if selected_company != "All":
    jobs = jobs[jobs["company"] == selected_company]

# -------------------------
# DATA OVERVIEW
# -------------------------

st.subheader("📋 Job Listings")

st.write("Total Jobs Found:", len(jobs))

st.dataframe(jobs, use_container_width=True)

# -------------------------
# SKILL DEMAND
# -------------------------

st.subheader("📈 Skill Demand")

fig, ax = plt.subplots()

ax.bar(skills["skill"], skills["count"])
plt.xticks(rotation=45)

st.pyplot(fig)

# -------------------------
# TOP LOCATIONS
# -------------------------

st.subheader("🌍 Top Hiring Locations")

top_locations = jobs["location"].value_counts().head(10)

fig2, ax2 = plt.subplots()

ax2.barh(top_locations.index, top_locations.values)

st.pyplot(fig2)

# -------------------------
# TOP COMPANIES
# -------------------------

st.subheader("🏢 Top Hiring Companies")

top_companies = jobs["company"].value_counts().head(10)

st.dataframe(top_companies)