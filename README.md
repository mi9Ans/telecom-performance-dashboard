# telecom-performance-dashboard
A complete business dashboard analyzing telecom customer activity, complaint trends, and maintenance efficiency. The project combines SQL, Python (Pandas), and BI visualization to uncover churn risk and network performance patterns.

# 📊 Telecom Performance Dashboard

## Overview  
This project delivers a complete business dashboard analyzing telecom customer activity, complaint trends, and maintenance efficiency.  
The goal is to uncover **customer churn risk**, identify **regional service issues**, and highlight how **maintenance patterns** impact overall network performance.

The dashboard integrates multiple datasets and provides actionable insights that can guide business decisions and operational improvements.

---

## 🧩 Project Workflow

### 1. Data Sources  
- **Customers.csv** – Customer IDs, plan types, and activity status  
- **Complaints.csv** – Complaint types, regions, and timestamps  
- **Maintenance.csv** – Records of routine and emergency maintenance  
- **NetworkUsage.csv** – Daily data usage metrics (MB)  
- **Ports.csv** – Network port-level downtime and performance data  

### 2. Data Processing  
Performed using **Python (Pandas)** and **SQL**:
- Cleaned null values, standardized date formats, and merged tables.  
- Aggregated KPIs: complaint rate per 100 customers, average usage, and downtime.  
- Calculated metrics for active user ratio, maintenance duration, and complaint density.  

### 3. Dashboard Development  
- Designed a clean, modern business dashboard.  
- Built KPI cards for total customers, complaints, and activity ratio.  
- Visualized complaint and maintenance trends by time, plan, and region.  
- Summarized insights and key recommendations in the final “Insights & Recommendations” section.  

---

## 💡 Key Insights
- Only **41.6% of customers** are active — significant churn risk.  
- **East & North regions** show the highest complaint rates per 100 customers.  
- **Complaints spike mid-year and in October**, aligning with maintenance load peaks.  
- **Ports P034 & P039** contribute to nearly **20% of total downtime**.  
- **High data-usage regions (Central & West)** experience slightly higher complaint rates.  

---

## 🎯 Recommendations
- Launch customer **reactivation campaigns** to reduce churn.  
- Focus **service-quality improvement** in East & North regions.  
- Optimize maintenance scheduling to keep average downtime **below 5 hours**.  
- Upgrade **critical ports (P034 & P039)** to minimize recurring outages.  
- Develop **predictive models** to forecast complaint and maintenance spikes.  
- Strengthen **network reliability** for premium plan customers.  

---

## 🛠 Tools & Technologies
- **Python:** Pandas, Matplotlib  
- **SQL:** Data aggregation and joins  
- **BI Tools:** Microsoft Fabric / Power BI Service  
- **Excel:** Preliminary data profiling and validation  

---

## 📂 Deliverables
- **Dashboard PDF:** [`Telecom_Performance_Dashboard.pdf`](dashboard/Telecom_Performance_Dashboard.pdf)  
- **Case Study Summary:** Key insights and recommendations (see final page).  
- **Notebook:** [`telecom_analysis.ipynb`](notebooks/telecom_analysis.ipynb)  

---

## 📸 Dashboard Preview
![Dashboard Preview](dashboard/dashboard_thumbnail.png)

---

## 📈 Project Impact
This project simulates a real-world telecom analytics environment by merging operational, customer, and maintenance data into a unified view.  
The insights help identify inefficiencies, customer dissatisfaction patterns, and areas for operational optimization.

---

## 📢 Author
**Anshumaan Mishra**  
Freelance Data Analyst  
📧 anshumaanmishra@myyahoo.com 
🔗 [LinkedIn]((https://www.linkedin.com/in/anshumaan-mishra-211118365/))  

---

## 🧾 License
This project is open-source and available for educational and portfolio use.  
Feel free to fork, reference, or adapt with proper attribution.
