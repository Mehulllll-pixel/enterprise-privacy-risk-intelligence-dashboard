import pandas as pd
import os

RISK_FILE = "privacy_risk_register.csv"
DATA_FILE = "enterprise_data_inventory.csv"


def calculate_risk_level(score):
    if score <= 5:
        return "Low"
    elif score <= 10:
        return "Medium"
    elif score <= 15:
        return "High"
    else:
        return "Critical"


def add_risk():
    risk_id = input("Enter Risk ID: ")
    asset = input("Enter Asset Affected: ")
    description = input("Enter Risk Description: ")
    impact = int(input("Impact (1-5): "))
    likelihood = int(input("Likelihood (1-5): "))

    score = impact * likelihood
    level = calculate_risk_level(score)

    mitigation = input("Enter Suggested Mitigation: ")

    risk_entry = {
        "Risk_ID": risk_id,
        "Asset_Affected": asset,
        "Risk_Description": description,
        "Impact": impact,
        "Likelihood": likelihood,
        "Risk_Score": score,
        "Risk_Level": level,
        "Mitigation": mitigation
    }

    file_exists = os.path.isfile(RISK_FILE)

    df = pd.DataFrame([risk_entry])
    df.to_csv(RISK_FILE, mode='a', header=not file_exists, index=False)

    print("\nRisk successfully logged.")
    print(f"Risk Score: {score}")
    print(f"Risk Level: {level}")


def generate_summary():
    if not os.path.isfile(RISK_FILE):
        print("No risks logged yet.")
        return

    df = pd.read_csv(RISK_FILE)

    print("\n--- Risk Summary Report ---")
    print(f"Total Risks Logged: {len(df)}")
    print("\nRisk Distribution:")
    print(df["Risk_Level"].value_counts())


def show_data_inventory():
    if not os.path.isfile(DATA_FILE):
        print("Data inventory not found.")
        return

    df = pd.read_csv(DATA_FILE)

    print("\n--- Enterprise Data Inventory ---")
    print(df)


def main():
    while True:
        print("\n1. Add Risk")
        print("2. View Risk Summary")
        print("3. View Data Inventory")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            add_risk()
        elif choice == "2":
            generate_summary()
        elif choice == "3":
            show_data_inventory()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option.")


main()