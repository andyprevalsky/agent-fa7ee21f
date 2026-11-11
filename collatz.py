"""Compute and print the Collatz sequence starting from 27."""

START = 27


def collatz_sequence(n: int) -> list[int]:
    """Return the Collatz sequence from n down to and including 1."""
    if n < 1:
        raise ValueError("n must be a positive integer")
    sequence = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence


def verify(sequence: list[int], steps: int, start: int) -> None:
    """Assert the sequence starts at start, ends at 1, and follows the rule."""
    assert sequence[0] == start, f"first value {sequence[0]} != {start}"
    assert sequence[-1] == 1, f"final value {sequence[-1]} != 1"
    for prev, curr in zip(sequence, sequence[1:]):
        expected = prev // 2 if prev % 2 == 0 else 3 * prev + 1
        assert curr == expected, f"bad transition {prev} -> {curr}, expected {expected}"
    assert 1 not in sequence[:-1], "1 reached before the final value"
    assert steps == len(sequence) - 1, f"steps {steps} != len(sequence) - 1"


def main() -> None:
    sequence = collatz_sequence(START)
    steps = len(sequence) - 1
    verify(sequence, steps, START)
    for value in sequence:
        print(value)
    print(f"Total steps: {steps}")


if __name__ == "__main__":
    main()
