🌍 Carbon Trading & Emission Dashboard
📌 Project Overview

Carbon emissions are one of the major causes of climate change. Companies often exceed their emission limits, leading to regulatory and sustainability challenges.
This project provides a Machine Learning-powered platform to:

Predict CO₂ emissions based on electricity and fuel usage.

Monitor company performance against emission caps via an interactive dashboard.

Simulate carbon credit trading between companies with surplus and deficit credits.

🚀 Features

ML-based Prediction → Accurate CO₂ emission forecasting.

Interactive Dashboard → Real-time monitoring of company emissions.

Carbon Credit Trading Simulation → Buyers & sellers can trade credits.

Visual Insights → Charts, tables, and graphs for clarity.

Sustainability Focus → Helps companies move towards carbon neutrality.

🏗️ Project Structure
📂 Carbon-Trading-Project
 ┣ 📄 Carbon_Trading_app.py   # Streamlit application
 ┣ 📊 carbon.csv              # Dataset (Electricity, Fuel, Emissions)
 ┣ 📑 Corbon_Trading.pptx     # Presentation (Project details)
 ┗ 📄 README.md               # Documentation

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/carbon-trading.git
cd carbon-trading

2️⃣ Install dependencies
pip install -r requirements.txt


If requirements.txt is missing, install manually:

pip install streamlit pandas scikit-learn plotly

3️⃣ Run the app
streamlit run Carbon_Trading_app.py

📊 Usage
🔹 CO₂ Predictor

Enter electricity used (kWh) and fuel consumed (Liters).

The model predicts CO₂ emissions (kg).

Shows required carbon credits (1 credit = 1000 kg CO₂).

🔹 Company Dashboard

Displays company-wise emission caps and actual emissions.

Highlights surplus (green) and deficit (red) balances.

Pie chart of total surplus vs. deficit.

🔹 Trade Simulation

Select buyer (deficit) and seller (surplus).

Execute trade of carbon credits.

Balances update in real-time.

📈 Results / Outcomes

Accurate CO₂ emission predictions.

Automatic calculation of carbon credit requirements.

Company performance dashboard with real-time insights.

Trade simulation balances surpluses & deficits effectively.

🔮 Future Enhancements

Integrate IoT-based real-time emission data.

Implement dynamic carbon credit pricing.

Add database support for storing trade history.

Expand to global carbon markets.

Provide policy insights for regulators.

👥 Team Members

Prem Kumar

S Aravindhan

M Abilash

S Arun Kumar

Ramana K
