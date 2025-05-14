# Data Warehousing Project:<br/> Health, Fitness & Nutrition Analytics

## Table of contents
1. [Scenario](#1-scenario)
2. [Business Requirements & Goals](#2-business-requirements--goals)
3. [Reports, Dashboards & KPIs](#3-reports-dashboards--kpis)
4. [Data Warehouse Design, Tables & Sources](#4-data-warehouse-design-tables--sources)<br>
   4.1 [APIs and Data Sources](#41-apis-and-data-sources)<br>
   4.2 [ETL Process](#42-etl-process)<br>
   4.3 [Schemas](#43-schemas)<br>
      - [Raw Schema](#raw-schema)<br>
      - [Staging Schema](#staging-schema)<br>
      - [Trusted Schema](#trusted-schema)<br>

---

## 1. Scenario

You are a data engineer at a health-tech startup that develops a mobile app to monitor user health.<br>
It tracks activity, sleep, and nutrition data, providing real-time insights and analytics over time.

---

## 2. Business Requirements & Goals

### Business Requirements 
- Provide health analytics for users (nutrition,fitness,sleep).  
- Help users track progress toward personal goals.  
- Offer predictive insights into calorie balance and fitness level trends.  

### Core Business Goals 
- **Activity Monitoring** – Collect and visualize daily activity metrics (steps, heart rate, calories burned).  
- **Sleep Insights** – Track sleep duration and quality.  
- **Nutrition Tracking** – Monitor daily caloric intake and macro goals.  
- **Goal Adherence** – Analyze user behavior around set goals.  

---

## 3. Reports, Dashboards & KPIs

### Reports  
- Daily caloric intake vs goal  
- Macronutrient breakdown (carbs, fat, protein)  
- Exercise and calorie burn analysis  
- Weekly goal adherence (% of goals met)  
- Weight and BMI trends  

### Dashboards  
- **Nutrition**: Caloric intake vs goal, macro distribution, top calorie foods  
- **Activity**: Steps, heart rate, calories burned, active vs sedentary time  
- **Sleep**: Sleep quality, total hours, start/end times  
- **Progress Tracker**: Goal streak, weight trends, daily health score 

### KPIs  
- % of users hitting daily calorie goals  
- Average macronutrient distribution per user  
- % of users achieving weekly fitness targets  
- Daily average calories burned  
- Number of consecutive days with goal adherence  
- Weekly goal adherence rate (activity, nutrition, sleep)  
- Most commonly exceeded macros (e.g., too much fat or sugar)

---

## 4. Data Warehouse Design, Tables & Sources

### 4.1 APIs and Data Sources

- **HealthApp**: Synthetic data is generated using the `healthapp.py` script.  
  - To generate raw data, run the following command:
    ```bash
    python src/extract/healthapp.py
    ```
  - This script creates the necessary schemas and tables in the `raw` schema (if they do not already exist) and populates them with data for user profiles, activity logs, sleep logs, nutrition logs, and goals logs.  
- [**USDA API**](https://www.ers.usda.gov/developer/data-apis/): Nutritional data for food items is fetched dynamically via API calls within the `healthapp.py` script.  

---

### 4.2 ETL Process

The ETL pipeline consists of the following steps:

1. **Extract**:  
   - Data is extracted from the `HealthApp` and `USDA API`.  
   - The `healthapp.py` script handles the extraction of synthetic data and API calls.  

2. **Transform**:  
   - Data is cleaned and transformed using the `transform.py` script.  
   - To run the transformation process, use the following command:
     ```bash
     python src/transform/transform.py
     ```

3. **Load**:  
   - Transformed data is loaded into the `staging` and `trusted` schemas.  

---

### 4.3 Schemas

The data warehouse is organized into three schemas: **raw**, **staging**, and **trusted**. Each schema serves a specific purpose in the ETL pipeline:

#### Raw Schema
- **Purpose**: The initial storage for raw, unprocessed data directly extracted from the sources.  
- **Tables**:  
  - `raw.user_profile`  
  - `raw.activity_log`  
  - `raw.sleep_log`  
  - `raw.nutrition_log`  
  - `raw.goals_log`  

#### Staging Schema
- **Purpose**: Stores cleaned and transformed data, ready for further processing.  
- **Tables**:  
  - `staging.user_profile`  
  - `staging.activity_log`  
  - `staging.sleep_log`  
  - `staging.nutrition_log`  
  - `staging.goals_log`  

#### Trusted Schema
- **Purpose**: Stores the final, fully processed data that is ready for analytics and reporting.  
- **Tables**:  
  - `trusted.user_profile`  
  - `trusted.activity_summary`  
  - `trusted.sleep_summary`  
  - `trusted.nutrition_summary`  
  - `trusted.goal_adherence`  