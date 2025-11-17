def power_2(n: int) -> int:
    """Compute power of 2"""
    if n == 0:
        return 1
    else:
        rest = power_2(n - 1)
        return 2 * rest


if __name__ == '__main__':
    print(power_2(0))
    print(power_2(1))
    print(power_2(3))
    print(power_2(5))
