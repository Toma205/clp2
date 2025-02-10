import matplotlib.pyplot as plt

regions = ["North", "South", "East", "West", "Central"]
sales_revenue = [50, 75, 60, 90, 65]

plt.figure(figsize=(8, 5))
plt.bar(regions, sales_revenue, color=['blue', 'green', 'red', 'purple', 'orange'])
plt.title("Sales Revenue Across Different Regions")
plt.xlabel("Regions")
plt.ylabel("Sales Revenue (in $1000s)")
plt.grid(axis='y', linestyle='--', alpha=0.7)


plt.show()
