from fizzbuzz import fizzbuzz_function

def test_smoke():
    assert 2+2 == 4

def test_fizzbuzz_happy():
    assert fizzbuzz_function(9) == "Fizz"
    assert fizzbuzz_function(15) == "FizzBuzz"
    assert fizzbuzz_function(25) == "Buzz"

def test_fizzbuzz_unhappy():
    assert fizzbuzz_function(7) == 7
    assert fizzbuzz_function("seven") == None