def primes_cached(f):
    """
    Decorator for gen_primes function.
    :param f:
    :return:
    """
    f.cache = {}
    f.primes = []
    f.pos = 1
    return f

@primes_cached
def gen_primes():
    """
    Generator returning prime numbers.
    """
    for prime in gen_primes.primes:
        yield prime
    gen_primes.pos += 1
    while True:
        if gen_primes.pos not in gen_primes.cache:
            gen_primes.primes.append(gen_primes.pos)
            yield gen_primes.pos
            gen_primes.cache[gen_primes.pos * gen_primes.pos] = [gen_primes.pos]
        else:
            for p in gen_primes.cache[gen_primes.pos]:
                gen_primes.cache.setdefault(p + gen_primes.pos, []).append(p)
            del gen_primes.cache[gen_primes.pos]
        gen_primes.pos += 1

def get_primes_in_range(start: int, stop: int):
    """
    Generator returning primes p such that start <= p < stop.
    :param start:
    :param stop:
    :return:
    """
    for prime in gen_primes():
        if prime >= stop:
            break
        if prime >= start:
            yield prime