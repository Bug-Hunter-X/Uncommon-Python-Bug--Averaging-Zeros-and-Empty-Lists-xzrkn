def calculate_average(numbers):
    if not numbers:
        raise ValueError("Cannot calculate average of an empty list.")
    if all(x == 0 for x in numbers):
        raise ValueError("Cannot calculate average of a list with only zeros.")
    return sum(numbers) / len(numbers)

# Example usage
data = [10, 20, 30, 40, 50]
average = calculate_average(data)
print(f"Average: {average}")

try:
    data_empty = []
    average_empty = calculate_average(data_empty)
    print(f"Average of empty list: {average_empty}")
except ValueError as e:
    print(f"Error for empty list: {e}")

try:
    data_with_zero = [10, 0, 20, 0, 30]
    average_with_zero = calculate_average(data_with_zero)
    print(f"Average with zeros: {average_with_zero}")
except ValueError as e:
    print(f"Error for list with only zeros: {e}")

try:
    data_all_zeros = [0,0,0,0,0]
    average_all_zeros = calculate_average(data_all_zeros)
    print(f"Average of all zeros: {average_all_zeros}")
except ValueError as e:
    print(f"Error for list with all zeros: {e}")
