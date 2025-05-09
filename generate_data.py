import random 
import pandas as pd

# LIC Insurance Plans
lic_plans = [
    ("LIC's Single Premium Endowment Plan", 717, "512N283V03", 8, 65),
    ("LIC's New Endowment Plan", 714, "512N277V03", 8, 60),
    ("LIC's New Jeevan Anand", 715, "512N279V03", 18, 50),
    ("LIC's Jeevan Lakshya", 733, "512N297V03", 18, 50),
    ("LIC's Jeevan Labh Plan", 736, "512N304V03", 8, 59),
    ("LIC's Amritbaal", 774, "512N365V02", 0, 13),
    ("LIC's Bima Jyoti", 760, "512N339V03", 18, 60),
    ("LIC's Jeevan Azad LIC’s Bima Shree", 748, "512N316V03", 18, 55),
    ("LIC's New Money Back Plan-20 Years", 720, "512N280V03", 13, 50),
    ("LIC's New Money Back Plan-25 Years", 721, "512N278V03", 13, 45),
    ("LIC's New Children's Money Back Plan", 732, "512N296V03", 0, 12),
    ("LIC's Jeevan Tarun", 734, "512N299V03", 0, 12),
    ("LIC's Bima Ratna LIC’s Digi Term", 876, "512N356V02", 18, 55),
    ("LIC’s Digi Credit Life", 878, "512N358V01", 18, 60),
    ("LIC’s Yuva Credit Life", 877, "512N357V01", 18, 40),
    ("LIC’s Yuva Term", 875, "512N355V02", 18, 40),
    ("LIC's New Tech-Term", 954, "512N351V01", 18, 65),
    ("LIC's New Jeevan Amar", 955, "512N350V02", 18, 65),
]

# Recognized child plans
child_plans = {
    "LIC's Amritbaal",
    "LIC's New Children's Money Back Plan",
    "LIC's Jeevan Tarun"
}

# Other Private Insurer Plans
other_plans = [
    ("HDFC Click 2 Protect", "ULIP", "912N902A01", 18, 65),
    ("SBI Life eShield", "Term Plan", "522N251B03", 18, 65),
    ("Max Life Online Term Plan", "Endowment Plan", "632N398F02", 18, 60),
    ("ICICI Prudential iProtect Smart", "Term Plan", "734N501Z03", 18, 65),
    ("Bajaj Allianz Life Smart Protect", "ULIP", "122N784A04", 18, 60),
    ("Tata AIA Life Insurance", "Term Plan", "553N920V02", 18, 65)
]

# Combined column headers
columns = [
    "Insurance Name", "Insurance Type", "Entry Age Min", "Entry Age Max", "Sum Assured Min",
    "Sum Assured Max", "Premium Min", "Premium Max", "Requires Medical Exam", "Income Criteria",
    "Riders Available", "Return of Premium", "CSR", "Features", "Policy Term Range", "Life Cover Till Age",
    "Full Name", "Age", "Gender", "Smoking Status", "Annual Income", "Existing Loans/Debts",
    "Existing Insurance Policies", "Desired Sum Assured", "Policy Term (Years)", "Premium Payment Option",
    "Death Benefit Option", "Payout Type", "Medical History", "Lifestyle Habits", "Interest in Optional Riders",
    "Interest in Tax Saving"
]

# Smoking status based on age
def generate_smoking_status(age):
    return "Non-Smoker" if age < 6 else random.choice(["Smoker", "Non-Smoker"])

# Generate one insurance entry row
def generate_insurance_row(index, user_age, user_income, desired_sum_assured):
    # Limit the desired sum assured to 10 times the annual income
    max_sum_assured = user_income * 10
    if desired_sum_assured > max_sum_assured:
        desired_sum_assured = max_sum_assured

    # Determine eligible plans from both LIC and private providers
    all_plans = lic_plans + other_plans
    eligible = [
        (name, "Child Plan" if name in child_plans else (plan_type if name in [p[0] for p in other_plans] else "Endowment Plan"), uin, min_age, max_age)
        for (name, *rest, min_age, max_age) in all_plans
        if min_age <= user_age <= max_age
        for plan_type in [rest[0] if len(rest) > 1 else "Endowment Plan"]
        for uin in [rest[1] if len(rest) > 1 else ""]  # Handle LIC vs others
    ]

    if not eligible:
        return None

    plan = random.choice(eligible)
    insurance_name, insurance_type, uin_no, entry_age_min, entry_age_max = plan

    is_child = insurance_type == "Child Plan"
    sum_assured_min = 100000 if is_child else random.randint(300000, 1000000)
    sum_assured_max = sum_assured_min + random.randint(100000, 500000)
    premium_min = 1000 if is_child else random.randint(5000, 20000)
    premium_max = premium_min + random.randint(500, 10000)

    income_criteria = "Parent income OK" if is_child else ("₹5L+" if user_income >= 500000 else "₹5L-")
    requires_medical_exam = "No" if is_child else random.choice(["Yes", "No"])

    return [
        insurance_name, insurance_type, entry_age_min, entry_age_max, sum_assured_min, sum_assured_max,
        premium_min, premium_max, requires_medical_exam, income_criteria,
        random.choice(["Accident Benefit", "Critical Illness", "Premium Waiver"]),
        random.choice(["Yes", "No"]), round(random.uniform(90, 99), 2),
        "Comprehensive coverage with tax benefits",
        f"{random.randint(5, 20)}-{random.randint(25, 40)}", random.randint(60, 85),
        f"User{index}", user_age, random.choice(["Male", "Female", "Other"]),
        generate_smoking_status(user_age), user_income,
        random.choice([True, False]), random.choice([True, False]),
        desired_sum_assured, random.randint(5, 30),
        random.choice(["Single", "Limited", "Regular"]),
        random.choice(["Level", "Increasing"]), random.choice(["Lump sum", "Installments"]),
        random.choice(["Healthy", "Diabetic", "Hypertensive"]),
        random.choice(["Active", "Sedentary"]),
        random.choice([True, False]), random.choice([True, False])
    ]

df = pd.DataFrame(columns=columns)

for i in range(50000):
    age = random.randint(0, 80)
    income = random.randint(100000, 1500000)
    desired_sum_assured = random.choice([100000, 500000, 1000000, 2000000])
    row = generate_insurance_row(i, age, income, desired_sum_assured)
    if row:
        df.loc[len(df)] = row

print(df.head())

# Save to CSV
df.to_csv("final_insurance_data.csv", index=False)
