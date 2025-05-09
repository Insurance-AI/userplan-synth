import random
import pandas as pd

lic_plans = [
    ("LIC's Single Premium Endowment Plan", "Endowment Plan", 8, 65),
    ("LIC's New Endowment Plan", "Endowment Plan", 8, 60),
    ("LIC's New Jeevan Anand", "Endowment Plan", 18, 50),
    ("LIC's Jeevan Lakshya", "Endowment Plan", 18, 50),
    ("LIC's Jeevan Labh Plan", "Endowment Plan", 8, 59),
    ("LIC's Amritbaal", "Child Plan", 0, 13),
    ("LIC's Bima Jyoti", "Endowment Plan", 18, 60),
    ("LIC's Jeevan Azad LIC’s Bima Shree", "Endowment Plan", 18, 55),
    ("LIC's New Money Back Plan-20 Years", "Endowment Plan", 13, 50),
    ("LIC's New Money Back Plan-25 Years", "Endowment Plan", 13, 45),
    ("LIC's New Children's Money Back Plan", "Child Plan", 0, 12),
    ("LIC's Jeevan Tarun", "Child Plan", 0, 12),
    ("LIC's Bima Ratna LIC’s Digi Term", "Endowment Plan", 18, 55),
    ("LIC’s Digi Credit Life", "Endowment Plan", 18, 60),
    ("LIC’s Yuva Credit Life", "Endowment Plan", 18, 40),
    ("LIC’s Yuva Term", "Term Plan", 18, 40),
    ("LIC's New Tech-Term", "Term Plan", 18, 65),
    ("LIC's New Jeevan Amar", "Term Plan", 18, 65),
]

other_plans = [
    ("HDFC Click 2 Protect", "ULIP", 18, 65),
    ("SBI Life eShield", "Term Plan", 18, 65),
    ("Max Life Online Term Plan", "Endowment Plan", 18, 60),
    ("ICICI Prudential iProtect Smart", "Term Plan", 18, 65),
    ("Bajaj Allianz Life Smart Protect", "ULIP", 18, 60),
    ("Tata AIA Life Insurance", "Term Plan", 18, 65)
]

all_plans = lic_plans + other_plans

columns = [
    "Insurance Name", "Insurance Type", "Entry Age Min", "Entry Age Max",
    "Sum Assured Min", "Sum Assured Max", "Premium Min", "Premium Max",
    "Income Criteria", "Riders Available", "Policy Term Range", "Life Cover Till Age",
    "Full Name", "Age", "Gender", "Smoking Status", "Annual Income",
    "Desired Sum Assured", "Policy Term (Years)", "Payout Type"
]

def generate_row(index):
    age = random.randint(0, 80)
    income = random.randint(100000, 1500000)

    eligible_plans = [plan for plan in all_plans if plan[2] <= age <= plan[3]]
    if not eligible_plans:
        return None

    name, plan_type, min_age, max_age = random.choice(eligible_plans)

    if plan_type == "Endowment Plan":
        sum_assured_min = random.randint(200000, 500000)
        sum_assured_max = sum_assured_min + random.randint(100000, 1000000)
        premium_min = max(5000, sum_assured_min // 1000)
        premium_max = max(premium_min + 5000, sum_assured_max // 1000)
    elif plan_type == "Term Plan":
        sum_assured_min = random.randint(500000, 1000000)
        sum_assured_max = sum_assured_min + random.randint(500000, 2000000)
        premium_min = max(3000, sum_assured_min // 1500)
        premium_max = max(premium_min + 5000, sum_assured_max // 1500)
    elif plan_type == "ULIP":
        sum_assured_min = random.randint(1000000, 3000000)
        sum_assured_max = sum_assured_min + random.randint(500000, 5000000)
        premium_min = max(8000, sum_assured_min // 1000)
        premium_max = max(premium_min + 5000, sum_assured_max // 1000)
    elif plan_type == "Child Plan":
        sum_assured_min = random.randint(100000, 300000)
        sum_assured_max = sum_assured_min + random.randint(50000, 500000)
        premium_min = max(1000, sum_assured_min // 1000)
        premium_max = max(premium_min + 1000, sum_assured_max // 1000)

    desired_sum_assured = random.randint(sum_assured_min, sum_assured_max)

    income_criteria = "₹5L+" if income >= 500000 else "₹5L-"
    riders = random.choice(["Accident Benefit", "Critical Illness", "Premium Waiver"])
    policy_term_range = f"{random.randint(5, 15)}-{random.randint(20, 30)}"
    life_cover_till = random.randint(age + 10, age + 40)

    gender = random.choice(["Male", "Female", "Other"])
    smoking_status = "Non-Smoker" if age < 18 else random.choice(["Smoker", "Non-Smoker"])
    payout_type = random.choice(["Lump sum", "Installments"])

    return [
        name, plan_type, min_age, max_age,
        sum_assured_min, sum_assured_max, premium_min, premium_max,
        income_criteria, riders, policy_term_range, life_cover_till,
        f"User{index}", age, gender, smoking_status, income,
        desired_sum_assured, random.randint(5, 30), payout_type
    ]

df = pd.DataFrame(columns=columns)
for i in range(30000):
    row = generate_row(i)
    if row:
        df.loc[len(df)] = row

# Save to CSV
df.to_csv("final_insurance_dataset_cleaned.csv", index=False)

print(df.head())
