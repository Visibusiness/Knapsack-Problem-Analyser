import json
import matplotlib.pyplot as plt
import os

# Load values from JSON file
with open('../jsons/values.json', 'r') as f:
    values = json.load(f)

test_cases = list(range(1, 31))
dynamic_values = values['dynamic']
greedy_values = values['greedy']

# Print the values to verify the data
# print("Dynamic values:", dynamic_values)
# print("Greedy values:", greedy_values)

# Plot the values
plt.plot(test_cases, dynamic_values, 'g--o', label='Dynamic')
plt.plot(test_cases, greedy_values, 'r--o', label='Greedy')

plt.xlabel('Test Case')
plt.ylabel('Result Value')
plt.title('Comparison of Dynamic and Greedy Results')
plt.legend()
plt.grid(True)

# Adjust layout and save the plot as an image file
plt.tight_layout()

plots_folder = '../plots'
if not os.path.exists(plots_folder):
    os.makedirs(plots_folder)

plt.savefig(os.path.join(plots_folder, 'knapsack_values.png'))