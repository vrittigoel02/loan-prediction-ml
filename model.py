import pandas as pd
import joblib

model = joblib.load("model.pkl")
columns = joblib.load("columns.pkl")

def preprocess(input_dict):
    df = pd.DataFrame([input_dict])

    # Fix Dependents
    df["Dependents"] = df["Dependents"].replace("3+", 3).astype(int)

    # Mapping
    df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})
    df['Married'] = df['Married'].map({'Yes': 1, 'No': 0})
    df['Education'] = df['Education'].map({'Graduate': 1, 'Not Graduate': 0})
    df['Self_Employed'] = df['Self_Employed'].map({'Yes': 1, 'No': 0})
    df['Property_Area']= df['Property_Area'].map({'Urban': 1 , 'Rural': 2 , 'Semiurban': 3})

    # 🔥 FIX: align columns
    df = df.reindex(columns=columns, fill_value=0)

    return df

def predict(input_dict):
    df = preprocess(input_dict)
    return model.predict(df)[0]
