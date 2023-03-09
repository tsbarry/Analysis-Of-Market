# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     custom_cell_magics: kql
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: Python 3.10.7 64-bit
#     language: python
#     name: python3
# ---

# %%
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import pandas as pd
import matplotlib.pyplot as plt
from config import key 

# %%
# connect to the database
engine = create_engine(key)
Base = automap_base()
Base.prepare(engine, reflect=True)

# %%
# save classes as variables, prepare classes
jobs = Base.classes.jobs
salaries = Base.classes.salaries
skills = Base.classes.skills

# %%
# query our database (pull data and save into objects)
session = Session(engine)

# %% [markdown]
# Extract all 3 tables from Amazon RDS postgres database

# %%
jobs_table = session.query(jobs)
print(jobs_table)

# %%
salaries_table = session.query(salaries)
print(salaries_table)

# %%
skills_table = session.query(skills)
print(skills_table)

# %%
# Requesting data from the table job 
job_data = session.query(jobs.id, jobs.title, jobs.company_name, jobs.location, jobs.via, jobs.extensions, jobs.posted_at, jobs.schedule_type, jobs.work_from_home, jobs.date_time)
rows_job = job_data.all()
rows_job

# convert into pandas DataFrame
jobs_df = pd.DataFrame(rows_job, columns =['id','title','company_name', 'location','via','extensions','posted_at','schedule_type','work_from_home','data_time'])
jobs_df.head()

# %%
# Requesting data from the table Salaries 
Salaries_data = session.query(salaries.id, salaries.salary_pay, salaries.salary_rate, salaries.salary_avg, salaries.salary_min, salaries.salary_max, salaries.salary_hourly, salaries.salary_yearly, salaries.salary_standardized)
rows_salaries = Salaries_data.all()
rows_salaries

# convert into pandas DataFrame
salaries_df = pd.DataFrame(rows_salaries, columns=["id", "salary_pay", "salary_rate", "salary_avg", "salary_min", "salary_max", "salary_hourly", "salary_yearly", "salary_standardized"])
salaries_df.head()


# %%
# Requesting data from the table skills 
Skills_data = session.query(skills.id, skills.description_tokens)
rows_skills = Skills_data.all()
rows_skills

# convert into pandas DataFrame
Skills_df = pd.DataFrame(rows_skills, columns= ["id", "description_tokens"])
Skills_df.head()

# %%
