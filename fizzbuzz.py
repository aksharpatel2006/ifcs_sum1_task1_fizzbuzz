#FizzBuzz program
def fizzbuzz_function(num): # FizzBuzz function
    """
    This function checks if the input value is a multiple of 3, 5 or both 3 & 5.
    If the number is a multiple of 3, the function returns "Fizz"
    If the number is a multiple of 5, the function returns "Buzz"
    If the number is a multiple of both 3 & 5, the function returns "FizzBuzz"
    If the number is NOT a multiple of any of these values, the function returns the input value
    """
    if num % 3 == 0 and num % 5 == 0: # Checks if num is a multiple of both 3 and 5
        return "FizzBuzz"
    elif num % 3 == 0: # Checks if num is a multiple of 3
        return "Fizz"
    elif num % 5 == 0: # Checks if num is a multiple of both 5
        return "Buzz"
    else: # If the number is NOT a multiple of any of these values, the function returns the input value
        return num