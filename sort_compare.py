import time
import random

def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list
    
def insertion_sort(a_list):
    start = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value
    end = time.time()
    return a_list, end - start

def shell_sort(a_list):
    start = time.time()
    sublistcount = len(a_list) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gap_insertion_sort(a_list, startposition, sublistcount)
        sublistcount = sublistcount // 2
    end = time.time()
    return a_list, end - start

def gap_insertion_sort(a_list, start, gap):
    """Helper function for shell sort - not timed directly"""
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value

def python_sort(a_list):
    """
    Use Python built-in sort function
    """
    start = time.time()
    a_list.sort() 
    end = time.time()
    return a_list, end - start

def main():
    list_sizes = [500, 1000, 5000]
    trials = 100

    for the_size in list_sizes:
        print(f"\nList size: {the_size}")

        # Python Sort
        total_time = 0
        for i in range(trials):
            my_list = get_me_random_list(the_size)
            _, time_spent = python_sort(my_list)
            total_time += time_spent
        avg_time = total_time / trials
        print(f"Python sort took {avg_time:10.7f} seconds to run, on average")

        # Insertion Sort
        total_time = 0
        for i in range(trials):
            my_list = get_me_random_list(the_size)
            _, time_spent = insertion_sort(my_list)
            total_time += time_spent
        avg_time = total_time / trials
        print(f"Insertion sort took {avg_time:10.7f} seconds to run, on average")

        # Shell Sort
        total_time = 0
        for i in range(trials):
            my_list = get_me_random_list(the_size)
            _, time_spent = shell_sort(my_list)
            total_time += time_spent
        avg_time = total_time / trials
        print(f"Shell sort took {avg_time:10.7f} seconds to run, on average")

if __name__ == "__main__":
    main()