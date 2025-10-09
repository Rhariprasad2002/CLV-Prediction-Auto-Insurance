from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np
import os
import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend to fix Tkinter warnings
import matplotlib.pyplot as plt

app = Flask(__name__)

# Load model and encoders
gbr = joblib.load("clv.pkl")
oe = joblib.load("oe.pkl")
le1 = joblib.load("le1.pkl")
scaler = joblib.load("scaler.pkl")

# CLV segmentation function
def segment(clv, low=8000, high=15000):
    if clv <= low:
        return "Low", "Mitigate risk: Minimal offers; evaluate cost-to-serve"
    elif clv > high:
        return "High", "Priority retention: Offer premium loyalty/discount"
    else:
        return "Medium", "Growth opportunity: Upsell or cross-sell"

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    data = request.form

    # Convert input to DataFrame
    df = pd.DataFrame([{
        "Coverage": data['coverage'],
        "EmploymentStatus": data['employment'],
        "Income": float(data['income']),
        "Monthly Premium Auto": float(data['premium']),
        "Months Since Last Claim": float(data['claim']),
        "Months Since Policy Inception": float(data['policy_age']),
        "Number of Open Complaints": float(data['complaints']),
        "Number of Policies": float(data['policies']),
        "Total Claim Amount": float(data['total_claim'])
    }])

    # Encode categorical fields
    df["Coverage"] = oe.transform(df[["Coverage"]])
    df["EmploymentStatus"] = le1.transform(df["EmploymentStatus"])

    # Scale numeric values
    numeric_cols = [
        "Income", "Monthly Premium Auto", "Months Since Last Claim",
        "Months Since Policy Inception", "Number of Open Complaints",
        "Number of Policies", "Total Claim Amount"
    ]
    df_scaled = scaler.transform(df[numeric_cols])

    # Combine categorical + scaled numeric into DataFrame with column names
    x_input = pd.DataFrame(
        np.hstack([df[["Coverage","EmploymentStatus"]].values, df_scaled]),
        columns=["Coverage", "EmploymentStatus"] + numeric_cols
    )

    # Predict CLV
    clv_pred = gbr.predict(x_input)[0]  # extract scalar from array

    # Segment and action
    segment_label, action = segment(clv_pred)

    # Plot CLV bar chart
    colors = {"High": "green", "Medium": "orange", "Low": "red"}
    plt.figure(figsize=(5,3))
    plt.bar(["CLV"], [clv_pred], color=colors[segment_label])
    plt.title(f"{segment_label} Value Customer")
    plt.ylabel("Customer Lifetime Value")
    plt.ylim(0, max(clv_pred*1.2, 20000))  # dynamic y-limit

    # Save plot in static folder
    plot_path = os.path.join("static", "clv_plot.png")
    plt.savefig(plot_path)
    plt.close()

    return render_template(
        'result.html',
        clv=round(clv_pred, 2),
        segment=segment_label,
        action=action,
        plot=plot_path
    )

if __name__ == '__main__':
    app.run(debug=True)
