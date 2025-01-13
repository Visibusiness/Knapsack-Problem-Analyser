import random
import os

def generate_tests(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    def generate_test(filename, num_objects, capacity, identical=False, special_case=False):
        with open(filename, "w") as f:
            f.write(f"{num_objects} {capacity}\n")
            weights = []
            profits = []
            if identical:  # Toate obiectele identice
                weight = random.randint(1, capacity // 5)
                profit = random.randint(1, 100)
                weights = [weight] * num_objects
                profits = [profit] * num_objects
            else:
                for _ in range(num_objects):
                    weight = random.randint(1, capacity // 5)
                    profit = random.randint(1, 100)
                    if special_case and random.random() < 0.3:
                        # Creează scenarii speciale pentru diferențe între greedy și dinamic
                        profit = weight * 2 + random.randint(1, 10)
                    weights.append(weight)
                    profits.append(profit)
            for w, p in zip(weights, profits):
                f.write(f"{w} {p}\n")
    
    # Primele 10 teste
    for i in range(1, 6):  # Primele 5 teste, 10 obiecte
        generate_test(f"{directory}/test{i}.in", num_objects=10, capacity=25)
    for i in range(6, 10):  # Următoarele 4 teste, 15 obiecte
        generate_test(f"{directory}/test{i}.in", num_objects=15, capacity=50)
    generate_test(f"{directory}/test10.in", num_objects=15, capacity=50, identical=True)

    # Ultimele 20 teste - cazuri speciale
    for i, num_objects in zip(range(11, 31), [20, 20, 20, 20, 20, 30, 30, 30, 30, 30, 
                                               50, 50, 50, 50, 50, 100, 100, 150, 150, 150]):
        generate_test(f"{directory}/test{i}.in", num_objects=num_objects, capacity = 100 + (i-11)*10, special_case=True)

    print(f"Generated 30 tests in {directory}.")

# Configurația generării testelor
output_directory = "../knapsack_tests"
generate_tests(output_directory)
