import os
import subprocess

algorithms = {
    1: ("branch_bound", "Branch/Bound Algorithm"),
    2: ("zero-one_hidden_counting", "Zero-One hidden counting algorithm"),
    3: ("cutting_plane", "Cutting plane algorithm"),
    4: ("rapson", "Raphson method"),
    5: ("direct_search", "Direct search method"),
    6: ("gradient", "Gradient method"),
    7: ("discrete", "Discrete programming"),
    8: ("quadratic", "Quadratic programming"),
    9: ("geometric", "Geometric programming"),
    10: ("stochastic", "Stochastic programming"),
    11: ("linear_combinations", "Linear combinations method"),
    12: ("sumt", "SUMT algorithm")
}

def print_algorithms():
    print("Algorithms:")
    print("-----------------")
    for key, value in algorithms.items():
        print(f"{key}. {value[1]} ({value[0]})")

def create_branch(branch_name):
    try:
        # Run the Git command to create a new branch
        subprocess.run(["git", "checkout", "-b", branch_name], check=True)
        print(f"\033[92m Branch '{branch_name}' created successfully. \033[00m")
    except subprocess.CalledProcessError as e:
        print(f"\033[91m Error occurred: {e} \033[00m")

def create_project(selected_algorithm):
    name, description = algorithms[selected_algorithm]

    if not os.path.exists(name):
        os.makedirs(name)

    with open(os.path.join(name, "README.md"), "w") as f:
        f.write(f"# {description}\n\n # Problem Statement\n\n # Algorithm Description\n\n # Implementation\n\n # Test Cases\n\n # References\n\n # Author\n\n # License\n\n")

    with open(os.path.join(name, "algorithm.py"), "w") as f:
        f.write(f"def {name}():\n    # Implement your algorithm here\n    pass\n\n\n")

    with open(os.path.join(name, "test_algorithm.py"), "w") as f:
        f.write(f"import unittest\nfrom algorithm import {name}\n\nclass TestAlgorithm(unittest.TestCase):\n\n    def test_{name}(self):\n        # Add tests for the function {name}()\n        {name}()\n\nif __name__ == \"__main__\":\n    unittest.main()\n")

    create_branch(name)

if __name__ == "__main__":
    print_algorithms()

    selected_algorithm = int(input("Please choose an algorithm: "))
    if selected_algorithm not in algorithms:
        print("\033[91m \nInvalid choice. Please select a valid algorithm.\033[00m")
        exit(1)

    create_project(selected_algorithm)



