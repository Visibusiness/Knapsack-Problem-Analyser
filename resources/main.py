import subprocess
import sys
import os

# Create log directory if it doesn't exist
log_dir = '../log'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Create jsons directory if it doesn't exist
jsons_dir = '../jsons'
if not os.path.exists(jsons_dir):
    os.makedirs(jsons_dir)

# Create plots directory if it doesn't exist
plots_dir = '../plots'
if not os.path.exists(plots_dir):
    os.makedirs(plots_dir)

# Redirect stdout and stderr to a log file
log_file_path = os.path.join(log_dir, 'log_file.txt')
log_file = open(log_file_path, 'w')
sys.stdout = log_file
sys.stderr = log_file

# Run checker.py
subprocess.run(['python3', 'checker.py'])

# Run plot_differences.py
subprocess.run(['python3', 'plot_differences.py'])

# Run plot_values.py
subprocess.run(['python3', 'plot_values.py'])

# Run plot_comparison.py
subprocess.run(['python3', 'plot_comparison.py'])

# Close the log file
log_file.close()