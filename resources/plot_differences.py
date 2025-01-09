import json
import matplotlib.pyplot as plt
import os

# Load differences from JSON file
with open('../jsons/differences.json', 'r') as f:
    differences = json.load(f)

test_cases = list(range(1, 31))

# Print the differences to verify the data
# print("Differences:", differences)

# Plot the differences
plt.plot(test_cases, differences, label='Difference (Dynamic - Greedy)', marker='o', color='purple')

plt.xlabel('Test Case')
plt.ylabel('Difference in Result')
plt.title('Difference between Dynamic and Greedy Results')
plt.legend()
plt.grid(True)

# Adjust layout and save the plot as an image file
plt.tight_layout()

plots_folder = '../plots'
if not os.path.exists(plots_folder):
    os.makedirs(plots_folder)

plt.savefig(os.path.join(plots_folder, 'knapsack_differences.png'))