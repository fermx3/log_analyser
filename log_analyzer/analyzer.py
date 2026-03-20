from collections import Counter

def count_by_level(entries: list[dict]) -> Counter:
    return Counter(entry["level"] for entry in entries)

def most_frequent_errors(entries: list[dict], n: int = 5) -> list[tuple]:
    return Counter(entry["message"] for entry in entries if entry["level"] == "ERROR")\
        .most_common(n)
