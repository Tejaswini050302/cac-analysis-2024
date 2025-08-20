import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('../data/cac_quarterly.csv')

# Calculate average
average_cac = df['CAC'].mean()
print(f"Average CAC: {average_cac:.2f}")  # Should print 230.37

# Plot trend
plt.figure(figsize=(8,5))
plt.plot(df['Quarter'], df['CAC'], marker='o', linestyle='-', color='blue', label='CAC')
plt.axhline(y=150, color='red', linestyle='--', label='Industry Target')
plt.title('Quarterly Customer Acquisition Cost (CAC) - 2024')
plt.xlabel('Quarter')
plt.ylabel('CAC')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('../visuals/cac_trend.png')
plt.show()
