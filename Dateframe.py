import pandas as pd

data = {
    'Name': ['Asha', 'Babu', 'Ravi', 'Meena'],
    'Maths': [85, 90, 75, 88],
    'Science': [80, 78, 92, 85]
}

df = pd.DataFrame(data)
print(df)
