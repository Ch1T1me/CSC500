def merge_sort(records, key):
    if len(records) <= 1: # base case: & already sorted
        return records
    
    mid = len(records) // 2 # midpoint
    left_half = merge_sort(records[:mid], key) # sort left half
    right_half = merge_sort(records[mid:], key) # sort right half

    return merge(left_half, right_half, key) # merge sorted halves

def merge(left, right, key):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right): # compare both halves
        if left[i][key] < right[j][key]: # choose smallest
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:]) # add remaining on left side
    sorted_list.extend(right[j:]) # add remaining on right side

    return sorted_list

patients = [
    {"id": 101, "name": "Roger Smith", "age": 32, "admission_date": "2025-02-04"},
    {"id": 102, "name": "Manwanki Doe", "age": 25, "admission_date": "2025-01-01"},
    {"id": 103,"name": "Johnny Lockwood", "age": 47, "admission_date": "2025-02-28"},

]

# implementation
sorted_patients = merge_sort(patients, "admission_date")
for patient in sorted_patients:
    print(patient)