# Read unsorted names from the file
with open("unsorted list.txt", "r") as read_file:
    unsorted_names = [line.strip() for line in read_file]

# Sort the names alphabetically
sorted_names = sorted(unsorted_names)

# Write the sorted names to a new file
with open("sorted list.txt", "w") as write_file:
    for name in sorted_names:
        write_file.write(name + "\n")

print("Sorting completed. Check the 'sortedlist.txt' file.")
