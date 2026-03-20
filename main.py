import re
import logging
from collections import Counter
import argparse

pattern = re.compile(
    r"(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) "
    r"(?P<level>ERROR|WARNING|INFO) "
    r"(?P<message>.*)"
)

def parse_line(line: str) -> dict | None:
    match = pattern.search(line)

    if match is None:
        return None

    return match.groupdict()

def parse_file(filepath: str) -> list[dict]:
    logs_list = []
    try:
        with open(filepath, "r") as logs:
            for line in logs:
                parsed = parse_line(line)
                if parsed:
                    logs_list.append(parsed)
        return logs_list
    except FileNotFoundError:
        logging.warning("File not found: %s", filepath)
        return []

def count_by_level(entries: list[dict]) -> Counter:
    return Counter(entry["level"] for entry in entries)

def most_frequent_errors(entries: list[dict], n: int = 5) -> list[tuple]:
    return Counter(entry["message"] for entry in entries if entry["level"] == "ERROR")\
        .most_common(n)

def print_report(counts: Counter, top_errors: list[tuple]) -> None:
    print("===== LOG SUMMARY =====\n")
    print("Log Levels:\n")

    for key, value in counts.items():
        print(f"    {key:<10}: {value:>5}")

    print("\nTop Errors:\n")

    for i, (message, count) in enumerate(top_errors, start=1):
        print(f"    {i}. {message:<30} ({count}x)")

    print("\n=======================")

def main():
    parser = argparse.ArgumentParser(description="Log analyzer")
    parser.add_argument(
        "filepath",
        type=str,
        help="Path to the log file to analyze"
        )

    args = parser.parse_args()

    parsed_file = parse_file(args.filepath)
    counted_types = count_by_level(parsed_file)
    counted_errors = most_frequent_errors(parsed_file)

    print_report(counted_types, counted_errors)


if __name__ == "__main__":
    main()
