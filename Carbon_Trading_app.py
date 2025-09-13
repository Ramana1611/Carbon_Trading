# carbon_app.py
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import plotly.express as px

# -----------------------
# Load Dataset
# -----------------------
data = pd.read_csv(r"C:\Users\abila\Downloads\carbon.csv")  # <-- change path if needed
data = data.dropna()

# Features and Target for ML model
X = data[["Electricity (kWh)", "Fuel (Liters)"]]
y = data["CO2 Emissions (kg)"]

# Train model
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)

# -----------------------
# Sample Company Data
# -----------------------
companies = [
    {"id": "c1", "name": "Tata Steel", "industry": "Steel", "cap": 500, "actual": 620},
    {"id": "c2", "name": "Infosys", "industry": "IT", "cap": 400, "actual": 300},
    {"id": "c3", "name": "Reliance", "industry": "Energy", "cap": 600, "actual": 650},
    {"id": "c4", "name": "Adani Green", "industry": "Energy", "cap": 350, "actual": 200},
]

def compute_balance(c):
    return c["cap"] - c["actual"]

for c in companies:
    c["balance"] = compute_balance(c)

# -----------------------
# Streamlit App
# -----------------------
st.set_page_config(page_title="Carbon Emission Dashboard", layout="wide")
st.title("🌍 Carbon Emission Dashboard & Trading Platform")

tab1, tab2, tab3 = st.tabs(["CO₂ Predictor", "Company Dashboard", "Trade Simulation"])

# -----------------------
# Tab 1: CO2 Predictor
# -----------------------
with tab1:
    st.header("📈 CO₂ Emission Predictor")
    electricity = st.number_input("Electricity Used (kWh)", min_value=0, step=10)
    fuel = st.number_input("Fuel Consumed (Liters)", min_value=0, step=1)

    if st.button("Predict Emission"):
        sample = pd.DataFrame(
            [[electricity, fuel]],
            columns=["Electricity (kWh)", "Fuel (Liters)"]
        )
        predicted_emission = model.predict(sample)[0]
        credits_needed = predicted_emission / 1000  # 1 credit = 1 ton (1000 kg)

        st.subheader("📊 Prediction Results")
        st.write(f"**Predicted CO₂ Emissions:** {predicted_emission:.2f} kg")
        st.write(f"**Carbon Credits Required:** {credits_needed:.2f}")

        if predicted_emission > 1000:
            st.error("🚨 Recommendation: BUY Carbon Credits")
        else:
            st.success("✅ Recommendation: SELL Extra Carbon Credits")

# -----------------------
# Tab 2: Company Dashboard
# -----------------------
with tab2:
    st.header("🏢 Company Carbon Balance")
    df_companies = pd.DataFrame(companies)

    # Highlight balances
    def highlight_balance(val):
        if val < 0:
            color = "red"
        elif val > 0:
            color = "green"
        else:
            color = "gray"
        return f"color: {color}"

    st.dataframe(df_companies.style.map(highlight_balance, subset=["balance"]))

    # Pie chart: total surplus vs deficit
    total_surplus = sum([c["balance"] for c in companies if c["balance"] > 0])
    total_deficit = sum([abs(c["balance"]) for c in companies if c["balance"] < 0])

    pie_data = pd.DataFrame(
        {"Type": ["Surplus", "Deficit"], "Units": [total_surplus, total_deficit]}
    )

    st.subheader("📊 Total Surplus vs Deficit")
    fig_pie = px.pie(
        pie_data,
        names="Type",
        values="Units",
        color="Type",
        color_discrete_map={"Surplus": "green", "Deficit": "red"},
    )
    st.plotly_chart(fig_pie, use_container_width=True)

# -----------------------
# Tab 3: Trade Simulation
# -----------------------
with tab3:
    st.header("⚡ Carbon Credit Trade Simulation")
    need = [c for c in companies if c["balance"] < 0]
    stock = [c for c in companies if c["balance"] > 0]

    if need and stock:  # Only show trade if both exist
        buyer = st.selectbox(
            "Buyer (Needs credits)", options=need, format_func=lambda x: x["name"]
        )
        seller = st.selectbox(
            "Seller (Has stock)", options=stock, format_func=lambda x: x["name"]
        )
        units = st.number_input("Units to Trade", min_value=1, value=10)

        if st.button("Execute Trade"):
            transfer = min(units, seller["balance"])
            seller["actual"] += transfer
            buyer["actual"] -= transfer
            buyer["balance"] = compute_balance(buyer)
            seller["balance"] = compute_balance(seller)

            st.success(f"✅ Trade executed: {transfer} units from {seller['name']} → {buyer['name']}")
    else:
        st.info("ℹ️ No trades possible: All companies balanced or insufficient stock/need.")
