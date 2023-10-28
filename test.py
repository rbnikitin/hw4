from dz4 import checksum, is_prime, primes, pipeline, random

def test_is_prime():
    assert is_prime(7) and not is_prime(8)

def test_primes():
    assert len(primes(1000)) == 1000

def test_checksum():
    t_primes=primes(1000)
    random.Random(100).shuffle(t_primes)
    assert checksum(t_primes) == 7785816

def test_pipeline():
    assert pipeline() == 7785816

#test_is_prime()
#test_primes()
#test_checksum()
#test_pipeline()
print("OK")
