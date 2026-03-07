def reverseInteger(x: int) -> int:
    """
    Approach: We will use the mathematical property of two's complement to reverse the integer.
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    # Convert the integer to a string to easily reverse it
    str_x = str(x)
    
    # Check if the reversed integer is negative
    if str_x[0] == '-':
        # If it's negative, remove the negative sign, reverse the string, and add the negative sign back
        return -int(str_x[1:][::-1])
    else:
        # If it's positive, simply reverse the string
        return int(str_x[::-1])