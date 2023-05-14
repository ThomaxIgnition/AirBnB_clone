def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    """
    if not numbers:
        return None

    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    return average


def print_statistics(numbers):
    """
    Print statistics for a list of numbers.
    """
    if not numbers:
        print("No numbers provided.")
        return

    minimum = min(numbers)
    maximum = max(numbers)
    average = calculate_average(numbers)

    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")
    print(f"Average: {average}")


if __name__ == "__main__":
    number_list = [2, 4, 6, 8, 10]
    print_statistics(number_list)
