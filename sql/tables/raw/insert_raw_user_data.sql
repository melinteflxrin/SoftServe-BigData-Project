INSERT INTO raw.user_data (
    user_id,
    name,
    age,
    weight_kg,
    height_cm,
    gender,
    calorie_goal,
    macro_goal,
    activity_start,
    activity_type,
    steps,
    heart_rate,
    calories_burned,
    sleep_start,
    sleep_end,
    sleep_quality_score,
    goal_type,
    goal_target 
) VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s 
);