import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

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

st.set_page_config(page_title="Privacy Risk Intelligence Dashboard", layout="wide")

st.title("🔐 Enterprise Privacy Risk Intelligence Dashboard")

# =========================
# SIDEBAR - ADD RISK
# =========================

st.sidebar.header("Add New Risk")

risk_id = st.sidebar.text_input("Risk ID")
asset = st.sidebar.text_input("Asset Affected")
description = st.sidebar.text_area("Risk Description")
impact = st.sidebar.slider("Impact (1-5)", 1, 5, 3)
likelihood = st.sidebar.slider("Likelihood (1-5)", 1, 5, 3)
mitigation = st.sidebar.text_area("Mitigation Strategy")

if st.sidebar.button("Log Risk"):
    score = impact * likelihood
    level = calculate_risk_level(score)

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

    df_new = pd.DataFrame([risk_entry])
    df_new.to_csv(RISK_FILE, mode='a', header=not file_exists, index=False)

    st.success(f"Risk Logged | Score: {score} | Level: {level}")

# =========================
# MAIN DASHBOARD
# =========================

st.header("📊 Risk Overview")
# =========================
# EXECUTIVE KPI SUMMARY
# =========================

if os.path.isfile(RISK_FILE) and os.path.getsize(RISK_FILE) > 0:
    df_kpi = pd.read_csv(RISK_FILE)

    total_risks = len(df_kpi)
    high_risks = len(df_kpi[df_kpi["Risk_Level"].isin(["High", "Critical"])])
    avg_score = round(df_kpi["Risk_Score"].mean(), 2)

    k1, k2, k3 = st.columns(3)

    k1.metric("Total Risks Logged", total_risks)
    k2.metric("High / Critical Risks", high_risks)
    k3.metric("Average Risk Score", avg_score)

else:
    st.info("No risks logged yet. Please add a new risk from the sidebar.")

if os.path.isfile(RISK_FILE) and os.path.getsize(RISK_FILE) > 0:

    df = pd.read_csv(RISK_FILE)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Risk Distribution")
        fig, ax = plt.subplots()
        sns.countplot(
            data=df,
            x="Risk_Level",
            order=["Low", "Medium", "High", "Critical"],
            ax=ax
        )
        st.pyplot(fig)

    with col2:
        st.subheader("Risk Heatmap (Impact vs Likelihood)")
        pivot = df.pivot_table(
            index="Impact",
            columns="Likelihood",
            values="Risk_Score",
            aggfunc="mean"
        )
        fig2, ax2 = plt.subplots()
        sns.heatmap(pivot, annot=True, cmap="Reds", ax=ax2)
        st.pyplot(fig2)

    st.subheader("📄 Risk Register")
    st.dataframe(df)
    st.download_button(
        label="Download Risk Register as CSV",
        data=df.to_csv(index=False),
        file_name="privacy_risk_report.csv",
        mime="text/csv"
    )

else:
    st.info("No risks logged yet. Please add a new risk from the sidebar.")

# =========================
# DATA INVENTORY SECTION
# =========================

st.header("📁 Enterprise Data Inventory")

if os.path.isfile(DATA_FILE):
    data_df = pd.read_csv(DATA_FILE)
    st.dataframe(data_df)
else:
    st.warning("Data inventory file not found.")