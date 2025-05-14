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
| Column         | Data Type        | Description                                       |
|----------------|------------------|---------------------------------------------------|
| `user_id`      | `SERIAL PK`      | Unique user identifier                            |
| `name`         | `VARCHAR(100)`   | User's full name                                  |
| `age`          | `INTEGER`        | User's age                                        |
| `weight_kg`    | `NUMERIC(4,1)`   | User's weight (kg)                                |
| `height_cm`    | `NUMERIC(4,1)`   | User's height (cm)                                |
| `gender`       | `VARCHAR(10)`    | User's gender                                     |
| `calorie_goal` | `INTEGER`        | Daily calorie goal                                |
| `macro_goal`   | `JSON`           | Macro goals: carbs, protein, fat (as JSON object) |

---

**activity_log** (Fitness Data)
| Column           | Data Type        | Description                                      |
|------------------|------------------|--------------------------------------------------|
| `activity_id`    | `SERIAL PK`      | Unique activity ID                               |
| `user_id`        | `INTEGER FK`     | References `user_profile(user_id)`               |
| `timestamp`      | `TIMESTAMP`      | Date and time of activity                        |
| `activity_type`  | `VARCHAR(50)`    | Type of activity (e.g., walking, running)        |
| `steps`          | `INTEGER`        | Number of steps                                  |
| `heart_rate`     | `INTEGER`        | Heart rate during activity                       |
| `calories_burned`| `INTEGER`        | Calories burned during activity                  |

---

**sleep_log** (Sleep Data)
| Column               | Data Type        | Description                                      |
|----------------------|------------------|--------------------------------------------------|
| `sleep_id`           | `SERIAL PK`      | Unique sleep log ID                              |
| `user_id`            | `INTEGER FK`     | References `user_profile(user_id)`               |
| `date`               | `DATE`           | Sleep date                                       |
| `sleep_start`        | `TIMESTAMP`      | Sleep start time                                 |
| `sleep_end`          | `TIMESTAMP`      | Sleep end time                                   |
| `sleep_quality_score`| `INTEGER`        | Sleep quality score                              |


---

**nutrition_log** (Nutrition Data)
| Column               | Data Type        | Description                                      |
|----------------------|------------------|--------------------------------------------------|
| `nutrition_id`       | `SERIAL PK`      | Unique nutrition entry ID                        |
| `user_id`            | `INTEGER FK`     | References `user_profile(user_id)`               |
| `date`               | `DATE`           | Entry date                                       |
| `food_item`          | `VARCHAR(100)`   | Name of food item                                |
| `meal_type`          | `VARCHAR(20)`    | Meal type (e.g., breakfast, lunch)               |
| `calories_per_100g`  | `INTEGER`        | Calories per 100 grams                           |
| `carbs_per_100g`     | `INTEGER`        | Carbs per 100g (grams)                           |
| `protein_per_100g`   | `INTEGER`        | Protein per 100g (grams)                         |
| `fat_per_100g`       | `INTEGER`        | Fat per 100g (grams)                             |

---

**goals_log** (Goal Tracking)
| Column         | Data Type        | Description                                      |
|----------------|------------------|--------------------------------------------------|
| `goal_id`      | `SERIAL PK`      | Unique goal ID                                   |
| `user_id`      | `INTEGER FK`     | References `user_profile(user_id)`               |
| `date`         | `DATE`           | Date the goal applies to                         |
| `goal_type`    | `VARCHAR(50)`    | Goal category (activity, sleep, nutrition)       |
| `target_value` | `INTEGER`        | Intended target                                  |
| `actual_value` | `INTEGER`        | Actual value achieved                            |
| `status`       | `VARCHAR(10)`    | Status (e.g., met / not met)                     |
