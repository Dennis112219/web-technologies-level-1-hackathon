def fibonacci(n):
    """
    This function generates the Fibonacci sequence up to a specified term n using iteration.

    Args:
        n: The number of terms in the Fibonacci sequence.

    Returns:
        A list containing the Fibonacci sequence up to n terms.
    """
    if n <= 1:
        return n  # Base case: return n if n is 0 or 1
    else:
        fibonacci_sequence = [0, 1]  # Initialize the sequence with the first two terms
        a, b = 0, 1  # Initialize variables a and b
        for _ in range(2, n):
            c = a + b  # Calculate the next term
            fibonacci_sequence.append(c)  # Add the next term to the sequence
            a, b = b, c  # Update values of a and b for the next iteration
        return fibonacci_sequence

# Get the number of terms from the user
num_terms = int(input("Enter the number of terms: "))

# Generate the Fibonacci sequence
fibonacci_sequence = fibonacci(num_terms)

# Print the Fibonacci sequence
print(fibonacci_sequence)
