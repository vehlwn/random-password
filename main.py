import string
import argparse
import random


def positive_integer_validator(s: str, msg: str) -> int:
    value = int(s)
    if value <= 0:
        raise argparse.ArgumentTypeError(msg)
    return value


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-a", "--ascii-lowercase", help="abcdef...", action="store_true",
    )
    parser.add_argument(
        "-A", "--ascii-uppercase", help="ABCDEF...", action="store_true",
    )
    parser.add_argument(
        "-d", "--digits", help="12345...", action="store_true",
    )
    parser.add_argument(
        "-l",
        "--length",
        help="length of a generated string",
        type=lambda s: positive_integer_validator(
            s, "length must be positive integer"
        ),
        default=4,
    )
    parser.add_argument(
        "-n",
        "--number",
        help="generate specified number of strings",
        type=lambda s: positive_integer_validator(
            s, "number must be positive integer"
        ),
        default=5,
    )
    args = parser.parse_args()

    DEFAULT_SYMBOLS = string.digits
    symbols = ""
    if args.ascii_lowercase:
        symbols += string.ascii_lowercase
    if args.ascii_uppercase:
        symbols += string.ascii_uppercase
    if args.digits:
        symbols += string.digits
    if not symbols:
        symbols = DEFAULT_SYMBOLS

    for i in range(args.number):
        password = "".join(random.choices(symbols, k=args.length))
        print(password)
