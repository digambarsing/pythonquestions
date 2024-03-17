def find_largest_element(lst):
    """ if not lst:
        return None """
    max_element = lst[0]
    for element in lst:
        if element > max_element:
            max_element = element
    return max_element

# Example usage:
my_list = [10, 5, 20, 15, 8]
print("Largest element:", find_largest_element(my_list))
