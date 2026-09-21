import time #Time module for python

def load_words(filename):
    """
    Loads a sorted words list from a file.

    Args:
        filename: The path to the file containing the words.  Each word is 
                  expected to be on a separate line.

    Returns:
        A sorted list of strings, where each string is a word read from the file.
    """
    with open(filename, 'r') as f:
        return sorted([word.strip().lower() for word in f])


def linear_search(sorted_words, word):
    """
    Performs a linear search on a list of words to find the index of a specific word.

    Args:
        sorted_words: A list of strings (words).  While the list name suggests it's sorted,
                      linear search works on unsorted lists as well, though it's generally
                      less efficient for sorted data.
        word: The string (word) to search for.

    Returns:
        The index of the word in the list if found. Returns -1 if the word is not found.
    """
    for i in range(len(sorted_words)):
        if sorted_words[i] == word:
            return i
    return -1


def linear_search_prefix(sorted_words, prefix):
    """
    Performs a linear search on a sorted list of words to find the 
    start and end indices (inclusive) of the range of words that start with a 
    given prefix.

    Args:
        sorted_words: A sorted list of strings (words).
        prefix: The prefix string to search for.

    Returns:
        A tuple containing the start and end indices (inclusive) of the range 
        of words starting with the prefix. Returns (-1, -1) if no words 
        with the given prefix are found.
    """
    # Part 1 - Implement!

    #Initilized trackers to not found state (-1)
    start_index = -1
    end_index = -1


    # Loop through the list, getting both the index (i) and the string (word)
    for i, word in enumerate(sorted_words):
        if word.startswith(prefix):
            if start_index == -1:
                start_index = i
            end_index = i
            
        
    return (start_index, end_index)


def binary_search(sorted_words, word):
    """
    Performs a binary search on a sorted list of words to find the index of a specific word.

    Args:
        sorted_words: A sorted list of strings (words).
        word: The string (word) to search for.

    Returns:
        The index of the word in the sorted list if found.  Returns -1 if the word is not found.
    """
    low = 0
    high = len(sorted_words) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_words[mid] == word:
            return mid
        elif sorted_words[mid] < word:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def binary_search_prefix(sorted_words, prefix):
    """
    Given a sorted list of words and a prefix, returns the start and end indices
    (inclusive) of the sublist of words that start with that prefix using 
    a modified binary search approach.

    Args:
        sorted_words: A sorted list of strings (words).
        prefix: The prefix string to search for.

    Returns:
        A tuple containing the start and end indices (inclusive) of the range 
        of words that start with the given prefix. Returns (-1, -1) if no words 
        with the prefix are found.
    """
    # Part 2 - Implement!

    #Binary search
    low1 = 0
    high1 = len(sorted_words) - 1

    start = -1

    #Find the beginning of the indices
    while low1 <= high1:
        mid1 = (low1 + high1) // 2
        if sorted_words[mid1].startswith(prefix):
            start = mid1
            high1 = mid1 - 1     # Start looking to the left for the low end of the indices
        elif sorted_words[mid1] < prefix:
            low1 = mid1 + 1
        else:
            high1 = mid1 - 1 

    low2 = 0
    high2 = len(sorted_words) - 1
    end = -1

    # Find the end of the indices
    while low2 <= high2:
        mid2 = (low2 + high2)//2
        if sorted_words[mid2].startswith(prefix):
            end = mid2
            low2 = mid2 + 1  #Start looking to the right for the high end of the indices
        elif sorted_words[mid2] < prefix:
            low2 = mid2 + 1
        else:
            high2 = mid2 - 1

    return (start, end)


def main():
    # Load a list of ~300k words.
    # Feel free to use a shorter list for debugging!
    word_list = load_words('words.txt')

    prefix = input('Enter prefix to challenge: ')

    # Part 3 - time these to determine which is faster (use python time module)
    # Choose which algorithm to use

    start_time_linear = time.perf_counter()
    start, end = linear_search_prefix(word_list, prefix)
    end_time_linear = time.perf_counter()

    start_time_binary = time.perf_counter()
    start, end = binary_search_prefix(word_list, prefix)
    end_time_binary = time.perf_counter()

    # Calculate durations
    linear_duration = end_time_linear - start_time_linear
    binary_duration = end_time_binary - start_time_binary

    print(f'Result: ({start}, {end})')
    print(f'Linear time: {linear_duration:.8f} seconds')
    print(f'Binary time: {binary_duration:.8f} seconds')

    if start == -1:
        print(f'{prefix} is not a prefix of any word!')
        return
    
    valid_range = word_list[start:end+1]
    print(f'{prefix} is the prefix of these words: {valid_range}')


main()
