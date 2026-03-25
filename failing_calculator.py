def average_ratios(numbers):
    """Calculate the average of ratios, avoiding division by zero.

    Args:
        numbers (list): A list of numeric values.

    Returns:
        float: The average of the ratios.

    Raises:
        ValueError: If the list is empty or contains only zeros.
    """
    if not numbers:
        raise ValueError("The input list is empty.")

    total = 0
    count = 0

    for number in numbers:
        if number == 0:
            print("Warning: Skipping division by zero.")
            continue
        total += 100 / number
        count += 1

    if count == 0:
        raise ValueError("All numbers were zero, cannot calculate average.")

    return total / count

if __name__ == "__main__":
    try:
        print(average_ratios([10, 5, 0]))
    except ValueError as e:
        print(f"Error: {e}")