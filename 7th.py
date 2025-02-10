import pandas as pd

df = pd.read_csv("sales_data.csv")


df["Revenue"] = df["Units Sold"] * df["Price per Unit"]
total_revenue_per_product = df.groupby("Product")["Revenue"].sum().reset_index()

print(total_revenue_per_product)