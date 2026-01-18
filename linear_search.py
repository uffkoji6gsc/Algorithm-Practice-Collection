import time
import random

def linear_search(data_list, target):
    """Perform a linear search for the target in data_list."""
    for index, element in enumerate(data_list):
        if element == target:
            return index
    return -1

def run_performance_test():
    print("--- Starting Algorithm Performance Test ---")
    test_data = [random.randint(1, 10000) for _ in range(5000)]
    target_value = random.choice(test_data)
    
    start_time = time.time()
    result = linear_search(test_data, target_value)
    end_time = time.time()
    
    if result != -1:
        print(f"Target {target_value} found at index: {result}")
    else:
        print("Target not found.")
    
    print(f"Execution time: {end_time - start_time:.6f} seconds")
    print("-------------------------------------------")

if __name__ == "__main__":
    run_performance_test()
