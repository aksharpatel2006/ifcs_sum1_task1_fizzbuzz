from fizzbuzz import fizzbuzz_function # Importing the fizzbuzz function

def test_smoke(): # Smoke test
    assert 2+2 == 4

def test_fizzbuzz_happy(): # Test function to check for "Fizz", "Buzz" or "FizzBuzz" outputs
    # The assertions below check if outputs of the function match our expected results (via the comparison operator)
    assert fizzbuzz_function(9) == "Fizz"
    assert fizzbuzz_function(15) == "FizzBuzz"
    assert fizzbuzz_function(25) == "Buzz"
    assert fizzbuzz_function(27) == "Fizz"

def test_fizzbuzz_boring(): # Test function to check if outputs are the same as inputs
     # The assertions below check if outputs of the function match our expected results (via the comparison operator)
    assert fizzbuzz_function(7) == 7
    assert fizzbuzz_function(14) == 14
    assert fizzbuzz_function(19) == 19