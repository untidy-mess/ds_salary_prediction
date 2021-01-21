# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 10:25:09 2020

@author: Arnab Wahid
"""

import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')

# Salary parsing

df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0 )
df['employer_prodived'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary' in x.lower() else 0 )

df = df[df['Salary Estimate'] !='-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_Kd = salary.apply(lambda x: x.replace('K', '').replace('$', ''))

minus_hr = minus_Kd.apply(lambda x: x.lower().replace('per hour', '').replace('employer provided salary', '').replace(':', ''))

df['min_salary'] = minus_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = minus_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary + df.max_salary)/2


# Compaly name text only

company_rating = df['Company Name'].apply(lambda x: x[-3:])
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis = 1)


# State field
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])
df.job_state.value_counts()

df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)


# Age of company
df['age'] = df.Founded.apply(lambda x: x if x < 1 else 2020-x)


# Job descripting parsing (Pandas, Python, etc.)
df['Job Description'][0]

# Python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df.python_yn.value_counts()

# RStudio
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' or 'r-studio' or 'rstudio' in x.lower() else 0)
df.R_yn.value_counts()

# Spark
df['spark_yn'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark_yn.value_counts()

# AWS
df['aws_yn'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.aws_yn.value_counts()

# Excel
df['excel_yn'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.excel_yn.value_counts()

# Anaconda
df['anaconda_yn'] = df['Job Description'].apply(lambda x: 1 if 'anaconda' in x.lower() else 0)
df.anaconda_yn.value_counts()

# Jupyter
df['jupyter_yn'] = df['Job Description'].apply(lambda x: 1 if 'jupyter' in x.lower() else 0)
df.jupyter_yn.value_counts()


df.columns

df_out = df.drop(['Unnamed: 0'], axis = 1)

df_out.to_csv('salary_data_cleaned.csv', index = False)


