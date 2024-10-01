import argparse
import random
import time

def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list
    
def insertion_sort(a_list):
    """Insertion sort implementation"""
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value

def shell_sort(a_list):
    """Shell sort implementation"""
    sublistcount = len(a_list) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gap_insertion_sort(a_list, startposition, sublistcount)
        sublistcount = sublistcount // 2

def gap_insertion_sort(a_list, start, gap):
    """Helper function for shell sort"""
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value

def python_sort(a_list):
    """
    Use Python built-in sorted function

    :param a_list:
    :return: the sorted list
    """
    return sorted(a_list)

def benchmark_sort_algorithm(algorithm, a_list):
    """Helper function to benchmark a sorting algorithm"""
    start = time.time()
    algorithm(a_list)
    return time.time() - start

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sorting algorithm comparison")
    parser.add_argument('--sizes', nargs='+', type=int, default=[500, 1000, 5000],
                        help='List of sizes to test with')
    parser.add_argument('--trials', type=int, default=100,
                        help='Number of trials per list size')
    
    args = parser.parse_args()

    list_sizes = args.sizes
    trials = args.trials

    for the_size in list_sizes:
        print(f"\nList size: {the_size}")

        # Python Sort
        total_time = 0
        for i in range(trials):
            my_list = get_me_random_list(the_size)
            total_time += benchmark_sort_algorithm(python_sort, my_list)
        avg_time = total_time / trials
        print(f"Python sort took{avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")

        # Insertion Sort
        total_time = 0
        for i in range(trials):
            my_list = get_me_random_list(the_size)
            total_time += benchmark_sort_algorithm(insertion_sort, my_list)
        avg_time = total_time / trials
        print(f"Insertion sort took{avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")

        # Shell Sort
        total_time = 0
        for i in range(trials):
            my_list = get_me_random_list(the_size)
            total_time += benchmark_sort_algorithm(shell_sort, my_list)
        avg_time = total_time / trials
        print(f"Shell sort took{avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")