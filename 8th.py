import pandas as pd

df = pd.read_csv("data.csv")

df_filled = df.fillna(df.mean(numeric_only=True))

print(df_filled)