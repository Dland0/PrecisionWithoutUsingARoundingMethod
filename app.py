import argparse


def calc_precision_number(num1: str, num2: str, precision: int) -> str:
    calc_number: int = int(num1.replace(",", "")) + int(num2.replace(",", ""))
    calc_number_str: str = str(calc_number)
    print(f"Input Sum = {calc_number_str}")

    if precision == 0:
        return "0"

    if len(calc_number_str) <= precision:
        return calc_number_str

    split_number_start: str = calc_number_str[:precision]
    split_number_end: str = calc_number_str[precision:]

    new_start: int = int(split_number_start) + 1
    new_end = "0" * len(split_number_end)

    high_round: str = str(new_start) + new_end
    low_round: str = split_number_start + new_end

    print(f"Low Round = {low_round} | High Round = {high_round}")

    high_diff: int = int(high_round) - calc_number
    low_diff: int = calc_number - int(low_round)

    print(f"{low_diff =} | {high_diff =}")

    return low_round if high_diff > low_diff else high_round


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate precision number.")
    parser.add_argument("--num1", type=str, required=True, help="First number as a string")
    parser.add_argument("--num2", type=str, required=True, help="Second number as a string")
    parser.add_argument(
        "--precision", type=int, required=True, help="Precision for the calculation"
    )

    args = parser.parse_args()

    result: str = calc_precision_number(num1=args.num1, num2=args.num2, precision=args.precision)
    print(f"Precision Number = {result}")
