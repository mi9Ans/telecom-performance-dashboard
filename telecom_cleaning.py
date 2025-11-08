import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------ LOAD DATA ------------------------
complaints = pd.read_csv('complaints.csv')
customers = pd.read_csv('customers.csv')
maintenance = pd.read_csv('maintenance.csv')
network = pd.read_csv('network_usage.csv')
ports = pd.read_csv('ports.csv')

# ------------------------ INITIAL INSPECTION ------------------------
complaints.info()
customers.info()
maintenance.info()
network.info()
ports.info()

print("\n---Customers Dataset---")
print(customers.head())
print("\n---Complaints Dataset---")
print(complaints.head())
print("\n---Maintenance Dataset---")
print(maintenance.head())
print("\n---Network Usage Dataset---")
print(network.head())
print("\n---Ports Dataset---")
print(ports.head())

print("\nMissing Values in Customers Dataset:\n", customers.isnull().sum())
print("\nMissing Values in Complaints Dataset:\n", complaints.isnull().sum())
print("\nMissing Values in Maintenance Dataset:\n", maintenance.isnull().sum())
print("\nMissing Values in Network Dataset:\n", network.isnull().sum())
print("\nMissing Values in Ports Dataset:\n", ports.isnull().sum())

# ------------------------ DATA CLEANING ------------------------
network['DownloadMB'] = pd.to_numeric(network['DownloadMB'], errors='coerce').round(2)
network['UploadMB'] = pd.to_numeric(network['UploadMB'], errors='coerce').round(2)
network.fillna({'DownloadMB': 0, 'UploadMB': 0}, inplace=True)
network['Total_UsageMB'] = network['DownloadMB'] + network['UploadMB']

# ------------------------ MERGE CUSTOMERS + COMPLAINTS ------------------------
customers_complaints = pd.merge(customers, complaints, on='CustomerID', how='left')
customers_complaints.rename(columns={'Date': 'ComplaintDate'}, inplace=True)
customers_complaints['ComplaintDate'] = pd.to_datetime(customers_complaints['ComplaintDate'])

# ------------------------ BASIC AGGREGATIONS ------------------------
regional_complaints = customers_complaints.groupby('Region')['ComplaintID'].count().reset_index(name='TotalComplaints')
avg_customer_complaints = customers_complaints.groupby('CustomerID')['ComplaintID'].count().reset_index(name='ComplaintCount')
average_complaints = avg_customer_complaints['ComplaintCount'].mean()
region_plan = customers.groupby('Region')['Plan'].value_counts().unstack().fillna(0)
region_issues = customers_complaints.groupby('Region')['IssueType'].value_counts().unstack().fillna(0)

customers_complaints['ComplaintMonth'] = customers_complaints['ComplaintDate'].dt.month_name()
monthly_complaints = customers_complaints.groupby('ComplaintMonth')['ComplaintID'].count().reindex([
    'January','February','March','April','May','June','July','August','September','October','November','December'
]).reset_index(name='TotalComplaints')

# ------------------------ TIMESTAMP ENRICHMENT ------------------------
network['Timestamp'] = pd.to_datetime(network['Timestamp'])
network['Usage_Date'] = network['Timestamp'].dt.date
network['Usage_Month'] = network['Timestamp'].dt.month_name()
network['Hour'] = network['Timestamp'].dt.hour
network['Weekday'] = network['Timestamp'].dt.day_name()

# ------------------------ MAINTENANCE DATE CLEANUP ------------------------
maintenance['Date'] = pd.to_datetime(maintenance['Date'])
maintenance['MaintenanceMonth'] = maintenance['Date'].dt.month_name()

# ------------------------ ANALYTICAL METRICS (For Power BI) ------------------------
# 1. Average Download, Upload, and Total Usage per Customer
usage_summary = network.groupby('CustomerID')[['DownloadMB','UploadMB','Total_UsageMB']].mean().reset_index()

# 2. Total Usage by Hour (Peak Network Hours)
hourly_usage = network.groupby('Hour')[['DownloadMB','UploadMB','Total_UsageMB']].sum().reset_index()

# 3. Total Usage by Weekday (Usage Pattern)
weekday_usage = network.groupby('Weekday')[['DownloadMB','UploadMB','Total_UsageMB']].sum().reset_index()

# 4. Monthly Network Usage Trend
monthly_usage = network.groupby('Usage_Month')[['DownloadMB','UploadMB','Total_UsageMB']].sum().reset_index()

# 5. Region-wise Total Complaints
regional_complaints_summary = regional_complaints.copy()

# 6. Average Monthly Fee by Plan and Region
avg_fee_region_plan = customers.groupby(['Region','Plan'])['MonthlyFee'].mean().reset_index()

# 7. Correlation between Plan and Complaints
plan_complaints = customers_complaints.groupby('Plan')['ComplaintID'].count().reset_index(name='TotalComplaints')

# 8. Maintenance Impact Analysis (Complaints during Maintenance Months)
complaints_maintenance = customers_complaints.copy()
complaints_maintenance['Month'] = complaints_maintenance['ComplaintDate'].dt.month_name()
maintenance_trend = complaints_maintenance.groupby('Month')['ComplaintID'].count().reset_index(name='ComplaintsDuringMaintenance')

# 9. Top 10 Customers by Total Data Usage
top10_usage = usage_summary.sort_values(by='Total_UsageMB', ascending=False).head(10)

# 10. Complaints per Region vs Network Usage
region_usage = pd.merge(regional_complaints_summary, customers[['CustomerID','Region']], on='Region')
region_usage = pd.merge(region_usage, usage_summary, on='CustomerID')
region_usage_summary = region_usage.groupby('Region')[['Total_UsageMB','TotalComplaints']].mean().reset_index()

# ------------------------ EXPORT CLEANED AND ANALYZED DATA ------------------------
usage_summary.to_csv('clean_usage_summary.csv', index=False)
hourly_usage.to_csv('hourly_usage.csv', index=False)
weekday_usage.to_csv('weekday_usage.csv', index=False)
monthly_usage.to_csv('monthly_usage.csv', index=False)
regional_complaints_summary.to_csv('regional_complaints_summary.csv', index=False)
avg_fee_region_plan.to_csv('avg_fee_region_plan.csv', index=False)
plan_complaints.to_csv('plan_complaints.csv', index=False)
maintenance_trend.to_csv('maintenance_trend.csv', index=False)
top10_usage.to_csv('top10_usage.csv', index=False)
region_usage_summary.to_csv('region_usage_summary.csv', index=False)

print("\n✅ All analytical summaries have been generated and saved for Power BI visualization.")

customers.to_csv('customers_clean.csv', index=False)
complaints.to_csv('complaints_clean.csv', index=False)
maintenance.to_csv('maintenance_clean.csv', index=False)
network.to_csv('network_clean.csv', index=False)
ports.to_csv('ports_clean.csv', index=False)



