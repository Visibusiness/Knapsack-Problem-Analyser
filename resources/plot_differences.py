import json
import matplotlib.pyplot as plt
import os

# Load differences from JSON file
with open('../jsons/differences.json', 'r') as f:
    differences = json.load(f)

test_cases = list(range(1, 31))
difference = differences['differences']
ratios = differences['ratio']
weights = differences['weights']

# Print the differences to verify the data
# print("Differences:", differences)
s = 0
v = []
r2 = []
i = 0
while i < len(weights):
    count = 0
    s = 0
    j = i
    while j < len(weights) and weights[i] == weights[j]:
        s += ratios[j]
        j += 1
        count += 1
    v.append(weights[i])
    r2.append(s/count)
    i = j

# Plot the differences
plt.plot(v, r2, label='Ratio (Dynamic / Greedy)', marker='o', color='purple')
plt.ylim(92, 101)
plt.xlabel('Wieghts')
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