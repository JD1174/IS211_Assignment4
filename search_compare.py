import time
import random

def get_me_random_list(n):
    """Generate list of n elements in random order"""
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list

def sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1
            
    end = time.time()
    return found, end - start

def ordered_sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1
                
    end = time.time()
    return found, end - start

def binary_search_iterative(a_list, item):
    start = time.time()
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
                
    end = time.time()
    return found, end - start
    
def binary_search_recursive(a_list, item):
    """
    Wrapper function to handle timing for the recursive call.
    """
    start = time.time()
    
    # Define the recursive logic inside so we don't reset the timer
    def recursive_logic(lst, trgt):
        if len(lst) == 0:
            return False
        else:
            midpoint = len(lst) // 2
            if lst[midpoint] == trgt:
                return True
            else:
                if trgt < lst[midpoint]:
                    return recursive_logic(lst[:midpoint], trgt)
                else:
                    return recursive_logic(lst[midpoint + 1:], trgt)

    found = recursive_logic(a_list, item)
    end = time.time()
    return found, end - start

def main():
    list_sizes = [500, 1000, 5000]
    item_to_search = 99999999  # Worst case: item not in list

    for size in list_sizes:
        print(f"\nList size: {size}")
        
        # Note: Ordered and Binary searches require sorted lists.
        # Handle the sorting inside the loop before calling the function.
        
        algorithms = [
            ('Sequential Search', sequential_search),
            ('Ordered Sequential Search', ordered_sequential_search),
            ('Binary Search (Iterative)', binary_search_iterative),
            ('Binary Search (Recursive)', binary_search_recursive)
        ]
        
        for name, algorithm in algorithms:
            total_time = 0

            for i in range(100):
                my_list = get_me_random_list(size)

                # Sort the list for algorithms that require it
                # Sort must be applied BEFORE calling the function so sorting time isn't included
                if 'Ordered' in name or 'Binary' in name:
                    my_list.sort()

                # Function now returns a tuple (found, time)
                found, time_spent = algorithm(my_list, item_to_search)
                total_time += time_spent

            avg_time = total_time / 100
            print(f"{name} took {avg_time:10.7f} seconds to run, on average")

if __name__ == "__main__":
    main()