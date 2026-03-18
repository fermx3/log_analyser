import re

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
