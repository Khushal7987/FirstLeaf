def binary_search(data_list, target):
    low = 0
    high = len(data_list) - 1
    
    while low <= high:
        # Calculate the middle index (using integer division)
        mid = (low + high) // 2
        
        if data_list[mid] == target:
            return mid  # Target found!
        elif data_list[mid] < target:
            # Target is in the upper half, discard the lower half
            low = mid + 1
        else:
            # Target is in the lower half, discard the upper half
            high = mid - 1
            
    return -1 # Target not found

# --- Example Usage ---
sorted_data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target_val = 23

index = binary_search(sorted_data, target_val)
print(f"Target {target_val} found at index: {index}") # Output: 5
