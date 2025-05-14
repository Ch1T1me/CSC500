# Memory blocks and process sizes
memory_blocks = [100, 500, 200, 300, 600]
process_sizes = [212, 417, 112, 426]

# Allocation result
allocation = [-1] * len(process_sizes)  # Initialize with -1 (unallocated)

# First-Fit Allocation
for i in range(len(process_sizes)):
    for j in range(len(memory_blocks)):
        if memory_blocks[j] >= process_sizes[i]:
            allocation[i] = j  # Allocate process i to block j
            memory_blocks[j] -= process_sizes[i]  # Reduce available memory in block
            break

# Display allocation results
print("Process No.\tProcess Size\tBlock Allocated")
for i in range(len(process_sizes)):
    if allocation[i] != -1:
        print(f"{i + 1}\t\t{process_sizes[i]}\t\t{allocation[i] + 1}")
    else:
        print(f"{i + 1}\t\t{process_sizes[i]}\t\tNot Allocated")
