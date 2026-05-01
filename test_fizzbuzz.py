from program import fizzbuzz

def test_smoke():
    assert 2+2 == 4

def test_fizzbuzz_happy():
    assert fizzbuzz(3) == "Fizz"

def test_fizzbuzz_unhappy():
    assert fizzbuzz("String") == None
