def square(n):
    """returns the square of the number"""
    return n * n


def cube(n):
    """returns the cube of the number"""
    return n*n*n


def triangle(n):
    """returns the triangle of the number"""
    sum = 0
    for i in range(n, 0, -1):
        sum = sum + 1
    return sum
