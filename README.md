# 🏦 Loan Approval Prediction App (ML-Based)

## 📌 Project Overview

This project predicts whether a loan application will be **approved or rejected** based on applicant details.
It uses a **Machine Learning model (Random Forest Classifier)** trained on historical loan data.

The application is deployed using **Streamlit**, allowing users to interact with the model in real-time.

---

## 🎯 Business Objective

Financial institutions need to assess loan applications efficiently.
This model helps:

* Reduce manual effort
* Improve decision consistency
* Identify risky applicants quickly

---

## ⚙️ Model Details

* Algorithm: Random Forest Classifier
* Type: Binary Classification
* Target Variable: Loan Status (Approved / Rejected)

---

## 📊 Input Features (User Inputs)

Please enter the following details carefully:

### 🔢 Numerical Inputs

| Feature            | Description                 | Unit                                 |
| ------------------ | --------------------------- | ------------------------------------ |
| Applicant Income   | Income of primary applicant | **Monthly income (in ₹)**            |
| Coapplicant Income | Income of co-applicant      | **Monthly income (in ₹)**            |
| Loan Amount        | Requested loan amount       | **in ₹ (thousands or dataset unit)** |
| Loan Amount Term   | Loan duration               | **in months**                        |
| Credit History     | Credit repayment history    | **1 = Good, 0 = Poor**               |

---

### 🧾 Categorical Inputs

| Feature       | Options                   |
| ------------- | ------------------------- |
| Gender        | Male / Female             |
| Married       | Yes / No                  |
| Dependents    | 0 / 1 / 2 / 3+            |
| Education     | Graduate / Not Graduate   |
| Self Employed | Yes / No                  |
| Property Area | Urban / Semiurban / Rural |

---

## ⚠️ Important Notes

* Income values should be **monthly**, as per dataset convention
* Loan amount and term should match realistic banking values
* Model predictions are **indicative**, not final financial decisions

---

## 🚀 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🌐 Live Demo

👉 (Add your Streamlit link here)

---

## 💻 GitHub Repository

👉 (Add your GitHub repo link here)

---

## 📈 Key Learnings

* End-to-end ML pipeline (data → model → deployment)
* Feature preprocessing & encoding
* Model deployment using Streamlit
* Handling real-world deployment challenges

---

## 👤 Author

MBA (Analytics) Student
Specialization: Data Analytics & Machine Learning

---

## ⭐ Future Improvements

* Add model explainability (SHAP / feature importance)
* Improve UI/UX
* Integrate real-time banking datasets
* Add API-based deployment
