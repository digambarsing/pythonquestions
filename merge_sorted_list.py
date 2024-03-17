def merge_sorted_lists(lst1, lst2):
    merged_list = []
    i, j = 0, 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged_list.append(lst1[i])
            i += 1
        else:
            merged_list.append(lst2[j])
            j += 1
    merged_list.extend(lst1[i:])
    merged_list.extend(lst2[j:])
    return merged_list

# Example usage:
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
print("Merged sorted list:", merge_sorted_lists(list1, list2))
