def count_occurrences(lst, element):
    return lst.count(element)

# Ask the user for a list of elements
elements = input("Enter a list of elements separated by spaces: ").split()

# Ask the user for the element to count
element = input("Enter the element to count: ")

# Count the occurrences of the element
occurrences = count_occurrences(elements, element)
print(f"The element '{element}' occurs {occurrences} times in the list.")
