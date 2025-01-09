import os
import shutil
import time
import json
import logging

# Configure logging
log_dir = '../log'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
logging.basicConfig(filename=os.path.join(log_dir, 'log_file.txt'), level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def compare_outputs(file1, file2):
    with open(file1) as f1, open(file2) as f2:
        line1 = f1.readline()
        line2 = f2.readline()
        if line1 != line2:
            return False
    return True

def get_first_line_value(file):
    with open(file) as f:
        return int(f.readline().strip())

def compile_programs():
    bin_dir = '../bin'
    if not os.path.exists(bin_dir):
        os.makedirs(bin_dir)
    os.system(f"g++ dynamic.cpp -o {bin_dir}/dynamic")
    os.system(f"g++ greedy.cpp -o {bin_dir}/greedy")
    os.system(f"g++ bruteforce.cpp -o {bin_dir}/bruteforce")

def run_tests():
    out_folder = '../out'
    if os.path.exists(out_folder):
        shutil.rmtree(out_folder)
    os.makedirs(out_folder)

    json_folder = '../jsons'
    if not os.path.exists(json_folder):
        os.makedirs(json_folder)

    dynamic_times = []
    greedy_times = []
    bruteforce_times = []
    dynamic_values = []
    greedy_values = []
    differences = []

    for i in range(1, 31):
        input_file = f"../in/test{str(i)}.in"
        dynamic_out = f"../out/test{str(i)}_dynamic.out"
        greedy_out = f"../out/test{str(i)}_greedy.out"

        start_time = time.time()
        os.system(f"../bin/dynamic < {input_file} > {dynamic_out}")
        dynamic_times.append(time.time() - start_time)

        start_time = time.time()
        os.system(f"../bin/greedy < {input_file} > {greedy_out}")
        greedy_times.append(time.time() - start_time)

        if i <= 10:
            brute_out = f"../out/test{str(i).zfill(2)}_bruteforce.out"
            start_time = time.time()
            os.system(f"../bin/bruteforce < {input_file} > {brute_out}")
            bruteforce_times.append(time.time() - start_time)

        # Compare dynamic and greedy outputs
        if not compare_outputs(dynamic_out, greedy_out):
            logging.warning(f"Mismatch on test {i} between dynamic and greedy solutions!")

        # Get the values from the first line of the output files
        dynamic_value = get_first_line_value(dynamic_out)
        greedy_value = get_first_line_value(greedy_out)
        dynamic_values.append(dynamic_value)
        greedy_values.append(greedy_value)
        differences.append(dynamic_value - greedy_value)

    # Save times to a JSON file
    with open(f'{json_folder}/times.json', 'w') as f:
        json.dump({
            'dynamic': dynamic_times,
            'greedy': greedy_times,
            'bruteforce': bruteforce_times
        }, f)

    # Save values to a separate JSON file
    with open(f'{json_folder}/values.json', 'w') as f:
        json.dump({
            'dynamic': dynamic_values,
            'greedy': greedy_values
        }, f)

    # Save differences to a separate JSON file
    with open(f'{json_folder}/differences.json', 'w') as f:
        json.dump(differences, f)

def main():
    compile_programs()
    run_tests()

if __name__ == "__main__":
    main()