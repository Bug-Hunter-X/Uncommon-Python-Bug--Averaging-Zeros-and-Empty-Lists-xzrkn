def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

# Example usage
data = [10, 20, 30, 40, 50]
average = calculate_average(data)
print(f"Average: {average}")

data_empty = []
average_empty = calculate_average(data_empty)
print(f"Average of empty list: {average_empty}")

data_with_zero = [10, 0, 20, 0, 30]
average_with_zero = calculate_average(data_with_zero)
print(f"Average with zeros: {average_with_zero}")