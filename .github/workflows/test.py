import sys
sys.path.append("/home/runner/work/python-course/python-course")

from task import is_prime, primes, checksum, pipeline

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(1) == False
    assert is_prime(4) == False

def test_primes():
    assert len(primes(1000)) == 1000
    assert len(primes(50)) == 50

def test_checksum():
    assert checksum([1, 2, 6, 24]) == 6012369

def test_pipeline():
    assert pipeline() == 7785816