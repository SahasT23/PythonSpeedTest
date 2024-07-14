import multiprocessing as mp 
import time
import math
import psutil
import os

results_a = []
results_b = []
results_c = []

def make_calculation_one(numbers):
    for number in numbers:
        results_a.append(math.sqrt(number ** 3))

def make_calculation_two(numbers):
    for number in numbers:
        results_b.append(math.sqrt(number ** 4))

def make_calculation_three(numbers):
    for number in numbers:
        results_c.append(math.sqrt(number ** 5))

def memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 * 1024)  # Convert bytes to MB

if __name__ == '__main__':
    
    number_list = list(range(1000000))

    p1 = mp.Process(target=make_calculation_one, args=(number_list,))
    p2 = mp.Process(target=make_calculation_two, args=(number_list,))
    p3 = mp.Process(target=make_calculation_three, args=(number_list,))

    print(f"Memory usage before multiprocessing: {memory_usage():.2f} MB")

    start = time.time()
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    end = time.time()

    print(f"Memory usage after multiprocessing: {memory_usage():.2f} MB")
    print(f"Time taken for multiprocessing: {end-start:.2f} seconds")

    temp_a = results_a[:]
    temp_b = results_b[:]
    temp_c = results_c[:]

    start = time.time()
    make_calculation_one(number_list)
    make_calculation_two(number_list)
    make_calculation_three(number_list)
    end = time.time()

    print(f"Memory usage after sequential processing: {memory_usage():.2f} MB")
    print(f"Time taken for sequential processing: {end-start:.2f} seconds")

    print(temp_a == results_a)
    print(temp_b == results_b)
    print(temp_c == results_c)
