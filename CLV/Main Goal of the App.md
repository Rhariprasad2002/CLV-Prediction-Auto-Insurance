Main Goal of the App

The Customer Lifetime Value (CLV) Prediction App is designed to:

Predict the expected revenue a customer will generate over their entire relationship with an auto insurance company.

Identify high-value, medium-value, and low-value customers, so the company can:

Focus on retention strategies for high-value customers.

Offer growth opportunities for medium-value customers.

Mitigate risk for low-value customers (reduce losses).

This helps the company make data-driven marketing, pricing, and retention decisions.

2. How the App Works

User Input:

Users (insurance staff or analysts) enter customer details in the app.

Data Processing:

Categorical values (Coverage, Employment Status) are encoded into numbers for the model.

Numeric values (Income, Premium, Policies, etc.) are scaled to match the model’s training scale.

Prediction:

The trained regression model predicts a numeric CLV based on the input features.

Customer Classification:

CLV is categorized as Low, Medium, or High Value to help make business decisions.

3. Columns (Features) Explained
Column	Type	Description	Effect on CLV
Coverage	Categorical	Type of insurance coverage: Basic, Extended, Premium	Higher coverage → higher premium → higher CLV
Employment Status	Categorical	Customer’s work status (Employed, Disabled, Retired, etc.)	Employed → higher income → higher CLV; Disabled → lower CLV
Annual Income	Numeric	Customer’s yearly income	Higher income → more ability to pay premiums → higher CLV
Monthly Premium Auto	Numeric	Monthly premium paid for auto insurance	Higher premium → directly increases CLV
Months Since Last Claim	Numeric	Time since last insurance claim	Longer duration since last claim → lower risk → higher CLV
Months Since Policy Inception	Numeric	How long customer has held the policy	Longer tenure → more stable revenue → higher CLV
Number of Open Complaints	Numeric	Current unresolved complaints	More complaints → negative experience → lower CLV
Number of Policies	Numeric	Number of active insurance policies	More policies → higher total revenue → higher CLV
Total Claim Amount	Numeric	Total claims filed in the past	Higher claims → higher risk → may reduce CLV
4. Why Some Predictions May Seem Off

CLV is calculated based on historical data patterns.

If a customer has extreme numeric values (very high premiums or many policies), the predicted CLV can be disproportionately high.

Classification thresholds (Low/Medium/High) also affect interpretation.

5. Main Takeaways

Goal: Predict how valuable a customer is to the insurance company.

Input Features: Coverage, Employment, Income, Premiums, Claims, Policies, Complaints, Tenure.

Output: CLV (numeric) + Classification (Low/Medium/High).

Use Case: Helps business focus retention and growth strategies based on predicted value.

If you want, I can also draw a simple diagram showing the workflow of your app from input → preprocessing → prediction → classification, which makes it very easy to explain to others.

Do you want me to do that?

You said:
yes