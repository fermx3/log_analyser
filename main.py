import argparse

from log_analyzer.parser import parse_file
from log_analyzer.analyzer import count_by_level, most_frequent_errors
from log_analyzer.reporter import print_report

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
