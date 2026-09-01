# UK Transportation Analytics

### Power BI Challenge | SQL Server + Power BI + DAX

[![Power BI](https://img.shields.io/badge/Power%20BI-Analytics-yellow?logo=powerbi)](https://powerbi.microsoft.com/)
[![SQL Server](https://img.shields.io/badge/SQL%20Server-Database-red?logo=microsoftsqlserver)](https://www.microsoft.com/sql-server)
[![DAX](https://img.shields.io/badge/DAX-Data%20Analysis-blue)](https://learn.microsoft.com/dax/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/)

An end-to-end **Transport Analytics Dashboard** developed for the **DataBuzz Power BI Challenge**, using **SQL Server, Power BI and DAX** to transform transport and EV charging data into interactive business insights.

---

## Project Overview

This project explores **UK transport journey performance and EV charging infrastructure** through an interactive five-page Power BI report.

The dashboard focuses on:

- 🚍 Transport journey performance
- ⏱️ Journey delays and punctuality
- 🚆 Transport mode comparison
- 🌦️ Weather impact on delays
- 📍 Area and regional performance
- ⚡ EV charging infrastructure

The project follows an end-to-end analytics workflow:

**SQL Server → Data Preparation → Data Modelling → DAX → Power BI → Analysis → Data Storytelling**

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **SQL Server** | Data source, transformation and analytical views |
| **Power BI** | Interactive dashboard and visualization |
| **DAX** | Measures, rankings and analytical calculations |
| **Power Query** | Data transformation and preparation |
| **Git & GitHub** | Version control and project documentation |

---

## 📁 Project Structure

```text
DataBuzz-PowerBI-Transport-Analytics/
│
├── PowerBI/
│   └── DataBuzz_Transport_Analytics.pbix
│
├── SQL/
│   ├── uk_transport_contest_full_data.sql
│   │
│   └── Views/
│       ├── vw_Top100_Delayed_Journeys.sql
│       └── vw_Top20_Delayed_Journeys_By_Mode.sql
│
├── Screenshots/
│   ├── 01_Punctuality_Overview.png
│   ├── 02_Mode_Delay_Analysis.png
│   ├── 03_Area_Deep_Dive.png
│   ├── 04_Top_100_Delay_Investigation.png
│   └── 05_EV_Charging_Infrastructure.png
│
├── Documentation/
│   └── PowerBI_Report_High_Quality.pdf
│
└── README.md
```

---

# 📈 Dashboard Pages

## 1. Punctuality Overview

The first page provides a high-level view of overall transport punctuality and journey performance.

### Key Analysis

- Total journeys
- Average delay
- On-time performance
- Delayed journeys
- Delay distribution
- Transport mode performance
- Journey trends

This page provides the starting point for understanding the overall transport network.

---

## 2. Mode Delay Analysis

This page compares journey delays across different transport modes.

A SQL view was created for the **Top 20 Delayed Journeys by Transport Mode** to support focused mode-level analysis.

### Key Analysis

- Delay comparison across transport modes
- Top delayed journeys
- Average delay
- Journey performance
- Transport mode filtering
- Dynamic DAX analysis

This helps identify which transport modes experience the greatest delays.

---

## 3. Area Deep Dive

This page focuses on transport performance across different areas and regions.

### Key Analysis

- Average delay by area
- Regional performance
- Weather impact on delays
- Area-level comparisons
- Dynamic Top N analysis
- Conditional formatting

The page helps identify areas that may require further investigation.

---

## 4. Top 100 Delay Investigation

A dedicated **drill-through page** for investigating the **Top 100 Most Delayed Journeys**.

A SQL view was created to rank journeys based on delay duration.

### Investigation Fields

- Route
- Area
- Transport mode
- Date
- Delay duration
- Passengers
- Weather condition

The drill-through functionality allows users to move from summary-level analysis to detailed journey-level investigation.

---

## 5. EV Charging Infrastructure

This page explores the availability and distribution of EV charging infrastructure.

### Key Analysis

- Total charge points
- Total connectors
- Average connectors per point
- Active charge points
- Charge points by region
- Charging capacity by speed type
- Charge point status
- Top areas by charging infrastructure
- EV charging equity

### ⚡ EV Charging Equity

Charging availability was analysed using:

**Charge Points per 100,000 Population**

Areas are classified into four categories:

| Classification | Description |
|---|---|
| 🟢 **Well Served** | Higher charging availability |
| 🔵 **Adequate** | Moderate charging availability |
| 🟠 **Under Served** | Lower charging availability |
| 🔴 **Charging Desert** | Very limited charging availability |

The classification is calculated dynamically using **DAX**.

---

# 🗄️ SQL Server

SQL Server was used as the primary data source and preparation layer.

The model contains data relating to:

- Areas
- Routes
- Journeys
- EV charging points

SQL was also used to create analytical views supporting the Power BI report.

### 🔹 Top 100 Most Delayed Journeys

The **Top 100 Most Delayed Journeys** view identifies the 100 journeys with the highest delay duration.

It supports:

- Delay ranking
- Journey-level investigation
- Drill-through analysis
- Detailed delay analysis

### 🔹 Top 20 Delayed Journeys by Transport Mode

The **Top 20 Delayed Journeys by Transport Mode** view supports the analysis of the most delayed journeys across different transport modes.

It provides a focused view of severe delays by mode.

---

# 🧮 DAX Analysis

DAX was used extensively to create analytical measures and interactive functionality.

### Key DAX Calculations

- Average delay
- Total journeys
- Delayed journeys
- On-time performance
- Total charge points
- Total connectors
- Average connectors per point
- Active charge point percentage
- Charge points per 100,000 population
- EV charging equity classification
- Dynamic Top N analysis
- Ranking measures

---

# 🎛️ Power BI Features

The report uses several Power BI capabilities to make the analysis interactive.

### Features Used

- 📊 KPI Cards
- 📈 Bar Charts
- 📊 Column Charts
- 🍩 Donut Charts
- 📋 Matrix Visuals
- 🎯 Interactive Slicers
- 🔍 Drill-through
- 🔢 Dynamic Top N
- 🎨 Conditional Formatting
- 🧭 Interactive Navigation

---

# 🎯 Key Business Questions

The dashboard helps answer questions such as:

1. Which transport modes experience the highest delays?
2. Which areas have the greatest average delays?
3. Where are delays happening most frequently?
4. How does weather affect journey delays?
5. Which journeys are among the most delayed?
6. Which areas require deeper investigation?
7. How is EV charging infrastructure distributed across regions?
8. Which areas have the highest charging availability?
9. Which areas are well served by EV charging infrastructure?
10. Which areas may have limited charging availability?

---

# 📸 Dashboard Preview

## Punctuality Overview

![Punctuality Overview](https://github.com/akhileshraut/UK-Transportation-Analytics-/blob/020d6b404116351e1832a397bb36e912f33bbe8d/Images/01_Punctuality_Overview.png)

---

## Mode Delay Analysis

![Mode Delay Analysis](https://github.com/akhileshraut/UK-Transportation-Analytics-/blob/8a82a8a3df013641e73f6ab5ef8a194a8461c527/Images/02_Mode_Delay_Analysis.png)

---

## Area Deep Dive

![Area Deep Dive](https://github.com/akhileshraut/UK-Transportation-Analytics-/blob/8a82a8a3df013641e73f6ab5ef8a194a8461c527/Images/03_Area_Deep_Dive.png)

---

## Top 100 Delay Investigation

![Top 100 Delay Investigation](https://github.com/akhileshraut/UK-Transportation-Analytics-/blob/8a82a8a3df013641e73f6ab5ef8a194a8461c527/Images/04_Top_100_Delay_Investigation.png)

---

## EV Charging Infrastructure

![EV Charging Infrastructure](https://github.com/akhileshraut/UK-Transportation-Analytics-/blob/8a82a8a3df013641e73f6ab5ef8a194a8461c527/Images/05_EV_Charging_Infrastructure.png)

---

# 📄 Project Documentation

A high-quality PDF version of the complete Power BI report is included in the `Documentation` folder.

👉 **[View the Power BI Report PDF](Documentation/PowerBI_Report_High_Quality.pdf)**

---

# 🔗 Interactive Power BI Report

Explore the interactive Power BI report:

👉 **[View Interactive Power BI Report](https://app.powerbi.com/view?r=eyJrIjoiOWY1Yjc0ZmMtNDBiYS00Zjg5LTgxZjEtNWNlM2RmZWYwZDhjIiwidCI6ImMyY2E1ZGZkLTI3YjgtNGIxOS05ZmJhLTc2OWJmYTBkNjY2NyJ9)**

---

# 📂 Repository Contents

### 📊 Power BI

The `.pbix` file contains:

- Data model
- DAX measures
- Visualizations
- Filters
- Drill-through functionality
- Report navigation

### 🗄️ SQL

The SQL folder contains:

- Source SQL script
- Analytical SQL views

### 📸 Screenshots

Screenshots of all five dashboard pages are included for portfolio presentation and quick review.

### 📄 Documentation

A high-quality PDF version of the complete report is included for offline viewing.

---

# ⚠️ Data & Refresh Note

The Power BI project was developed using a **local SQL Server data source**.

The `.pbix` file contains the report and model configuration. Refreshing the data may require access to the original SQL Server environment.

The published Power BI report is provided for interactive viewing.

---

# 💡 Key Learning

This challenge reinforced that building a good Power BI dashboard is not only about creating visuals.

The complete analytical journey matters:

```text
SQL Server
     ↓
Data Preparation
     ↓
Data Modelling
     ↓
DAX
     ↓
Power BI
     ↓
Interactive Analysis
     ↓
Data Storytelling
```

This project strengthened practical skills in:

- SQL
- SQL Server
- Power BI
- DAX
- Data Modelling
- Data Analysis
- Dashboard Design
- Drill-through Analysis
- Data Storytelling

---

# 👨‍💻 Author

## Akhilesh Raut

**Data Analytics | Power BI | SQL | DAX**

---

## ⭐ Project Highlights

| Area | Highlights |
|---|---|
| 🗄️ **SQL Server** | Data preparation and analytical SQL views |
| 📊 **Power BI** | Interactive dashboard and data visualization |
| 🧮 **DAX** | Measures, rankings, Top N analysis and EV equity |
| 🧩 **Data Modelling** | Fact and dimension based analytical model |
| 🔍 **Drill-through** | Detailed investigation of Top 100 delayed journeys |
| 📖 **Data Storytelling** | Turning transport data into actionable insights |

---

## ⭐ If you find this project useful

Feel free to explore the Power BI report, SQL scripts, dashboard screenshots and project documentation.

**Built with SQL Server, Power BI and DAX. 🚀**
