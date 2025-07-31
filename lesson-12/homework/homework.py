# Homework:

# Exercise 1: Threaded Prime Number Checker

# Write a Python program that checks whether a given range of numbers contains prime numbers. Divide the range among multiple threads to parallelize the prime checking process. Each thread should be responsible for checking a subset of the range, and the main program should print the list of prime numbers found.
import threading

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

# Thread worker function
def check_primes(start, end, result_list):
    for num in range(start, end):
        if is_prime(num):
            result_list.append(num)

# Main function
def main():
    start_range = int(input("Enter start of range: "))
    end_range = int(input("Enter end of range: "))
    num_threads = int(input("Enter number of threads: "))

    thread_list = []
    primes_found = []  # Shared list
    lock = threading.Lock()

    # Split the range into roughly equal parts for each thread
    chunk_size = (end_range - start_range) // num_threads

    for i in range(num_threads):
        sub_start = start_range + i * chunk_size
        # Last thread takes the rest of the range
        sub_end = end_range if i == num_threads - 1 else sub_start + chunk_size
        
        # Wrap the result list with a lock to avoid thread-safety issues
        thread = threading.Thread(target=lambda s=sub_start, e=sub_end: 
                                  [lock.acquire() or check_primes(s, e, primes_found) or lock.release()])
        thread_list.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in thread_list:
        thread.join()

    # Sort results because threads may finish in random order
    primes_found.sort()
    print("\nPrime numbers in the range:")
    print(primes_found)

if __name__ == "__main__":
    main()


# Exercise 2: Threaded File Processing

# Write a program that reads a large text file containing lines of text. Implement a threaded solution to count the occurrence of each word in the file. Each thread should process a portion of the file, and the main program should display a summary of word occurrences across all threads.

import threading
from collections import Counter

def count_words(lines, result_list, lock):
    local_counter = Counter()
    for line in lines:
        words = line.strip().lower().split()
        words = [word.strip('.,!?;:"()[]{}') for word in words]
        local_counter.update(words)
    
    with lock:
        result_list.append(local_counter)

def main():
    filename = input("Enter the filename (e.g., largefile.txt): ")
    num_threads = int(input("Enter number of threads to use: "))

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            all_lines = f.readlines()
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return

    total_lines = len(all_lines)
    chunk_size = total_lines // num_threads

    threads = []
    partial_results = []
    lock = threading.Lock()

    # Create and start threads
    for i in range(num_threads):
        start = i * chunk_size
        end = total_lines if i == num_threads - 1 else (i + 1) * chunk_size
        thread_lines = all_lines[start:end]
        thread = threading.Thread(target=count_words, args=(thread_lines, partial_results, lock))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Combine all partial Counters
    final_counter = Counter()
    for counter in partial_results:
        final_counter.update(counter)

    # Display the word count summary (top 20)
    print("\nTop 20 most common words:")
    for word, count in final_counter.most_common(20):
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
