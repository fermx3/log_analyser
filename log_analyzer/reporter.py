from collections import Counter

def print_report(counts: Counter, top_errors: list[tuple]) -> None:
    print("===== LOG SUMMARY =====\n")
    print("Log Levels:\n")

    for key, value in counts.items():
        print(f"    {key:<10}: {value:>5}")

    print("\nTop Errors:\n")

    for i, (message, count) in enumerate(top_errors, start=1):
        print(f"    {i}. {message:<30} ({count}x)")

    print("\n=======================")
