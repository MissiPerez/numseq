def is_prime(num):
    """returns a list of all primes less than the number"""
    if num >= 2:
        for x in range(2, num):
            if not (num % x):
                return False
    else:
        return False
    return True


def primes(num):
    """returns a boolean indicating whether the number is prime"""
    prime_list = []
    for number in range(num):
        if is_prime(number):
            prime_list.append(number)
    return prime_list
