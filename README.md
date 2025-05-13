# Data Warehousing Project:<br/> Health, Fitness & Nutrition Analytics

## Table of contents
1. [Scenario](#scenario)
2. [Business Requirements & Goals](#business-requirements--goals)
3. [Reports, Dashboards & KPIs](#reports-dashboards--kpis)
4. [Data Warehouse Design, Tables & Sources](#data-warehouse-design-tables--sources)

---

## Scenario

You are a data engineer at a health-tech startup that develops a mobile app to monitor user health.<br>
It tracks workouts, sleep, and nutrition data, providing real-time insights and analytics over time.

---

## Business Requirements & Goals

**Business Requirements**  
- Provide health analytics for users (fitness, nutrition, sleep).  
- Help users track progress toward personal goals.  
- Offer predictive insights into calorie balance and fitness level trends.  

**Core Business Goals**  
- **Activity Monitoring** – Collect and visualize daily activity metrics (steps, heart rate, calories burned).  
- **Sleep Insights** – Track sleep duration and quality.  
- **Nutrition Tracking** – Monitor daily caloric intake and macro goals.  
- **Goal Adherence** – Analyze user behavior around set goals.  
- **Behavioral Insights** – Provide early signals for health improvement or risk.

---

## Reports, Dashboards & KPIs

**Reports**  
- Daily caloric intake vs goal  
- Macronutrient (carbs/fat/protein) breakdown by day  
- Exercise and calorie burn vs intake analysis  
- Goal reports (weekly % of goals met)  
- Weight and BMI trend over time

**Dashboards**  
- **Nutrition Dashboard**  
  - Current day caloric intake vs goal  
  - Macro distribution pie chart  
  - Foods with highest calories/macros  
- **Activity Dashboard**  
  - Steps, heart rate, calories burned per day  
  - Active minutes vs sedentary time  
- **Sleep Dashboard**  
  - Sleep quality score, total hours slept  
  - Sleep start/end times  
- **Progress Tracker**  
  - Goal streak  
  - Weight loss/gain vs plan  
  - Daily health score

**KPIs**  
- % of users hitting daily calorie goals  
- Average macronutrient distribution per user  
- % of users achieving weekly fitness targets  
- Daily average calories burned  
- Number of consecutive days with goal adherence  
- Weekly goal adherence rate (activity, nutrition, sleep)  
- Most commonly exceeded macros (e.g., too much fat or sugar)

---

## Data Warehouse Design, Tables & Sources

**Data Warehouse Design**  
- **Server**: `health_dw`  
- **Database**: `health_analytics_db`  

**Sources** 
- **HealthApp** – Own platform data collected via the mobile app.  
- [**USDA API**](https://www.ers.usda.gov/developer/data-apis/) – Partner platform providing food nutritional information.<br>  

**Tables**

**user_profile** (Personal Info)
| Column         | Description                      |
|----------------|----------------------------------|
| `user_id` (PK) | Unique user identifier           |
| `name`         | User's full name                 |
| `age`          | User's age                       |
| `weight`       | User's weight                    |
| `height`       | User's height                    |
| `gender`       | User's gender                    |
| `calorie_goal` | Daily calorie goal               |
| `macro_goal`   | Macro goals (JSON: carbs, protein, fat) |

---

**activity_log** (Fitness Data)
| Column           | Description                       |
|------------------|-----------------------------------|
| `activity_id` (PK)| Unique activity identifier       |
| `user_id`         | Associated user ID               |
| `timestamp`       | Date and time of activity        |
| `activity_type`   | Type of activity (e.g., running) |
| `steps`           | Number of steps                  |
| `heart_rate`      | Heart rate during activity       |
| `calories_burned` | Calories burned during activity  |

---

**sleep_log** (Sleep Data)
| Column               | Description                  |
|----------------------|------------------------------|
| `sleep_id` (PK)      | Unique sleep log ID          |
| `user_id`            | Associated user ID           |
| `date`               | Sleep date                   |
| `sleep_start`        | Sleep start time             |
| `sleep_end`          | Sleep end time               |
| `sleep_quality_score`| Numeric score of sleep quality |

---

**nutrition_log** (Nutrition Data)
| Column               | Description                          |
|-----------------------|--------------------------------------|
| `nutrition_id` (PK)   | Unique nutrition entry ID            |
| `user_id`            | Associated user ID                   |
| `date`               | Entry date                           |
| `food_item`          | Name of food item                    |
| `meal_type`          | Meal type (e.g., breakfast, lunch)   |
| `calories_per_100g`  | Calories per 100 grams of the food item |
| `carbs_per_100g`     | Grams of carbohydrates per 100 grams |
| `protein_per_100g`   | Grams of protein per 100 grams        |
| `fat_per_100g`       | Grams of fat per 100 grams           |

---

**goals_log** (Goal Tracking)
| Column         | Description                          |
|----------------|--------------------------------------|
| `goal_id` (PK) | Unique goal ID                       |
| `user_id`      | Associated user ID                   |
| `date`         | Date the goal applies to             |
| `goal_type`    | Goal category (activity, sleep, etc.)|
| `target_value` | Intended target                      |
| `actual_value` | Value achieved                       |
| `status`       | Status (met / not met)               |
