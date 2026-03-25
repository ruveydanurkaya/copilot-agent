import json

def calculate_total(value):
    """Calculate the total with a 15% increase."""
    return value * 1.15

def format_total(value):
    """Format the total value as a string."""
    return f"Total: {value:.2f}"

def log_results(results, filename="log.txt"):
    """Log the results to a file in JSON format."""
    with open(filename, "a") as f:
        f.write(json.dumps(results) + "\n")

def process_data(data):
    """Process a list of data, calculate totals, and log results.

    Args:
        data (list): A list of numeric values to process.

    Returns:
        list: A list of calculated totals.
    """
    results = []
    for value in data:
        total = calculate_total(value)
        print(format_total(total))
        results.append(total)

    log_results(results)
    return results