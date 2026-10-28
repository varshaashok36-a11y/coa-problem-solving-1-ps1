BITS = 8
MASK = (1 << BITS) - 1


def to_bin(value):
    """Format a value as an 8-bit binary string."""
    return format(value & MASK, f"0{BITS}b")


def logical_left_shift(value, positions):
    """Logical left shift: zeros enter from the right, MSBs are discarded."""
    steps = []
    v = value & MASK
    for i in range(1, positions + 1):
        v = (v << 1) & MASK
        steps.append((i, v))
    return v, steps


def logical_right_shift(value, positions):
    """Logical right shift: zeros enter from the left (no sign extension)."""
    steps = []
    v = value & MASK
    for i in range(1, positions + 1):
        v = v >> 1
        steps.append((i, v))
    return v, steps


def print_shift(title, original, result, steps, direction):
    print(f"\n{title}")
    print(f"  Original : {to_bin(original)}  ({original})")
    print(f"  Step-by-step ({direction}):")
    for i, v in steps:
        print(f"    Step {i}: {to_bin(v)}")
    print(f"  Final 8-bit result : {to_bin(result)}  ({result})")


def run_q2():
    print("\n" + "=" * 60)
    print("Q2: Logical Shift Operations on 8-bit Binary Numbers")
    print("=" * 60)

    # a) Logical left shift of 10110110 by 2 positions
    a_orig = 0b10110110
    a_res, a_steps = logical_left_shift(a_orig, 2)
    print_shift("a) Logical left shift of 10110110 by 2 positions",
                a_orig, a_res, a_steps, "left")
    expected_a = 0b11011000
    print(f"  Verified : {'PASS' if a_res == expected_a else 'FAIL'} "
          f"(manual result: {to_bin(expected_a)})")

    # b) Logical right shift of 11010100 by 2 positions
    b_orig = 0b11010100
    b_res, b_steps = logical_right_shift(b_orig, 2)
    print_shift("b) Logical right shift of 11010100 by 2 positions",
                b_orig, b_res, b_steps, "right")
    expected_b = 0b00110101
    print(f"  Verified : {'PASS' if b_res == expected_b else 'FAIL'} "
          f"(manual result: {to_bin(expected_b)})")


if __name__ == "__main__":
    run_q2()