"""An example project to test failing tests."""


def double(x: float) -> int:
    return 3 * x


if __name__ == "__main__":
    print(f"double(2) is {double(2)}.")
