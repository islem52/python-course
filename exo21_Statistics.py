def length(lst):
    """Returns the number of elements in the list."""
    return len(lst)

def mean(lst):
    """Calculates the arithmetic mean of the list."""
    if not lst:
        return 0  
    return sum(lst) / len(lst)

def range_of_list(lst):
    """Returns the difference between max and min values in the list."""
    if not lst:
        return 0  
    return max(lst) - min(lst)

# Sample list for testing
numbers = [1, 2, 3, 4, 5]

# Testing the functions
print("Length:", length(numbers))  
print("Mean:", mean(numbers))        
print("Range:", range_of_list(numbers)) 
