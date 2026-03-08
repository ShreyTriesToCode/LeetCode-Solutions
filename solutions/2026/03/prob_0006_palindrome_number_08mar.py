def isPalindrome(x: int) -> bool:
    """
    Approach: Reverse the integer and compare with the original number.
    Time Complexity: O(log(n))
    Space Complexity: O(1)
    """
    # Convert integer to string
    str_x = str(x)
    
    # Reverse the string
    reversed_str_x = str_x[::-1]
    
    # Compare the original string with the reversed string
    return str_x == reversed_str_x

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(isPalindrome(121))  # Expected: True
    print(isPalindrome(123))  # Expected: False