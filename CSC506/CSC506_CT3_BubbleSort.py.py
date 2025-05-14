def bubble_sort(records, key):
    n = len(records) # length of records
    for i in range(n): # number of passes
        swapped = False # track swaps
        for j in range(0, n-i-1): # comparisons are adjacent
            if records[j][key] > records[j+1][key]: # swap to correct order
                records[j], records[j+i] = records[j+i], records[j]
                swapped = True
        if not swapped:
            break
    return records

patients = [
    {"id": 101, "name": "Roger Smith", "age": 32, "admission_date": "2025-02-04"},
    {"id": 102, "name": "Manwanki Doe", "age": 25, "admission_date": "2025-01-01"},
    {"id": 103,"name": "Johnny Lockwood", "age": 47, "admission_date": "2025-02-28"},

]

sorted_patients = bubble_sort(patients, "age")
for patient in sorted_patients:
    print(patient)