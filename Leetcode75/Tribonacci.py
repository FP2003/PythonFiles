# Function to calculate the nth tribonacci number iteratively
def tribonacci(n: int) -> int:
    # Initialize tribonacci sequence values
    p1, p2, p3 = 1, 1, 0
    
    # Handle base cases
    if n == 0:
        return p3
    elif n == 1:
        return p2
    elif n == 2:
        return p1

    # Calculate tribonacci number iteratively
    output = 0
    for i in range(3, n+1):
        output = p1 + p2 + p3
        p3, p2, p1 = p2, p1, output
    return output

print(tribonacci(5))
