BITS = 8
MASK = (1 << BITS) - 1
SIGN_BIT = 1 << (BITS - 1)


def to_twos_complement(n):
    """Convert a signed decimal integer (-128..127) to an 8-bit 2's complement value."""
    if not -(1 << (BITS - 1)) <= n <= (1 << (BITS - 1)) - 1:
        raise ValueError(f"{n} is out of the 8-bit signed range (-128 to 127)")
    return n & MASK


def from_twos_complement(value):
    """Convert an 8-bit 2's complement value back to a signed decimal integer."""
    return value - (1 << BITS) if value & SIGN_BIT else value


def to_bin(value):
    """Format an 8-bit value as a binary string."""
    return format(value & MASK, f"0{BITS}b")


def signed_add(a, b):
    """Add two signed 8-bit integers using 2's complement and detect overflow."""
    x = to_twos_complement(a)
    y = to_twos_complement(b)

    raw_sum = x + y
    result = raw_sum & MASK                    # discard carry out of bit 7
    signed_result = from_twos_complement(result)

    # Overflow: both operands have the same sign, but the result's sign differs.
    overflow = (a >= 0) == (b >= 0) and (signed_result >= 0) != (a >= 0)

    return x, y, result, signed_result, overflow


def run_q1():
    print("=" * 60)
    print("Q1: Signed 8-bit Arithmetic using 2's Complement")
    print("=" * 60)

    cases = [
        ("a) (25 + (+18))",    25,  18),
        ("b) ((-25) + (-18))", -25, -18),
    ]

    for label, a, b in cases:
        x, y, result, signed_result, overflow = signed_add(a, b)
        expected = a + b

        print(f"\n{label}")
        print(f"  Operand 1 : {a:>4} -> {to_bin(x)}")
        print(f"  Operand 2 : {b:>4} -> {to_bin(y)}")
        print(f"  Binary sum: {to_bin(result)}  (carry out discarded)")
        print(f"  Decimal   : {signed_result}")
        print(f"  Overflow  : {'YES' if overflow else 'NO'}")
        status = "PASS" if signed_result == expected and not overflow else "FAIL"
        print(f"  Verified  : {status} (expected {expected})")


if __name__ == "__main__":
    run_q1()