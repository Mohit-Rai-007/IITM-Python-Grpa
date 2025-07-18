def is_palindrome(n: int) -> bool:
    '''Checks if an integer is a palindrome.

    Arguments:
    n: int - the integer to check

    Return:
    bool - True if the integer is a palindrome, False otherwise
    '''
    subscriptable=str(n)
    
    return subscriptable==subscriptable[::-1]