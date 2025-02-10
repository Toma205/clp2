import matplotlib.pyplot as plt
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temperatures = [22, 24, 19, 23, 25, 27, 26]

plt.figure(figsize=(8, 5))
plt.plot(days, temperatures, marker='o', linestyle='-', color='b', label="Temperature (°C)")
plt.title("Temperature Variations Over a Week")
plt.xlabel("Days of the Week")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)


plt.show()
