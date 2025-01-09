import json
import matplotlib.pyplot as plt
import os

# Load values from JSON file
with open('../jsons/values.json', 'r') as f:
    values = json.load(f)

# Load differences from JSON file
with open('../jsons/differences.json', 'r') as f:
    differences = json.load(f)

test_cases = list(range(1, 31))
dynamic_values = values['dynamic']
greedy_values = values['greedy']

# Print the values to verify the data
# print("Dynamic values:", dynamic_values)
# print("Greedy values:", greedy_values)
# print("Differences:", differences)

# Create subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# Plot the values
ax1.plot(test_cases, dynamic_values, label='Dynamic', marker='o', color='blue')
ax1.plot(test_cases, greedy_values, label='Greedy', marker='o', color='green')
ax1.set_xlabel('Test Case')
ax1.set_ylabel('Result Value')
ax1.set_title('Comparison of Dynamic and Greedy Results')
ax1.legend()
ax1.grid(True)

# Plot the differences
ax2.plot(test_cases, differences, label='Difference (Dynamic - Greedy)', marker='o', color='purple')
ax2.set_xlabel('Test Case')
ax2.set_ylabel('Difference in Result')
ax2.set_title('Difference between Dynamic and Greedy Results')
ax2.legend()
ax2.grid(True)

# Adjust layout and save the plot as an image file
plt.tight_layout()

plots_folder = '../plots'
if not os.path.exists(plots_folder):
    os.makedirs(plots_folder)

plt.savefig(os.path.join(plots_folder, 'knapsack_combined.png'))