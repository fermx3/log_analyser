import re
import logging
from collections import Counter

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
