import pandas as pd
from sklearn.linear_model import LogisticRegression
data = pd.DataFrame ({
    'Income': [25000, 40000, 350000, 50000, 75000, 60000, 90000, 20000],
    'Credit_Score': [500, 600, 580, 650, 700, 680, 720, 480],
    'Loan_Approved': [0, 0, 0, 1, 1, 1, 1, 0]
})
X = data[['Income', 'Credit_Score']]
y = data['Loan_Approved']
model = LogisticRegression()
model.fit(X,y)
income = float(input("Enter your monthly income (in thousand): "))
credit_Score = float(input("Enter your Credit Score: "))
prediction = model.predict([[income, credit_Score]])
result = "Approved" if prediction [0] == 1 else "Note Approved"
print(f"Loand Status: {result}")

