import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, KFold
from sklearn.preprocessing import StandardScaler
import glob

df_name = glob.glob("./regression/data/*regression.csv")[0]

df = pd.read_csv(df_name)

X = df[['lr', 'Lutidine', 'SiH', 'Time']]
y = df['yield']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

rf_model = RandomForestClassifier(n_estimators=100, random_state=0)

cv = KFold(n_splits=5, shuffle=True, random_state=0)

scores = cross_val_score(rf_model, X_scaled, y, cv=cv, scoring='r2')

rf_model.fit(X_scaled, y)

input_lr = input("lr = ")
input_Lutidine = input("Lutidine = ")
input_SiH = input("SiH = ")
input_Time = input("Time = ")

input_lr = float(input_lr)
input_Lutidine = float(input_Lutidine)
input_SiH = float(input_SiH)
input_Time = float(input_Time)

new_data = pd.DataFrame([[input_lr, input_Lutidine, input_SiH, input_Time]], 
                        columns=['lr', 'Lutidine', 'SiH', 'Time'])

input_scaled = scaler.transform(new_data)

predicted_yield = rf_model.predict(input_scaled)

final_prediction = predicted_yield[0]

print(f"入力条件:")
print(new_data)
print(f"\n予測される収率: {final_prediction:.2f} %")
