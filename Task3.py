# Step 1: Read the number of input lines
n = int(input())

# Step 2: Create an empty set to store unique elements
unique_elements = set()

# Step 3: Loop over the input and process each chemical compound
for _ in range(n):
    elements = input().split()  # Split the line into elements
    unique_elements.update(elements)  # Add all elements to the set (ignores duplicates)

# Step 4: Print the unique elements
for element in unique_elements:
    print(element)  # Print each unique element
