# Log Analyzer

## Description
This tool parses a log file and generates a summary report
with log level counts and the most frequent error messages.

## Requirements
Python 3.10+ (no external dependencies)

## Installation
1. Clone the repository
    git clone https://github.com/tu-usuario/log-analyzer.git

2. Navigate to the project folder
    cd log-analyzer

## Usage
To use it you have to call main.py and pass the filepath as an argument

Example:
`python main.py logs/sample.log`

## Output Example

```
===== LOG SUMMARY =====

Log Levels:

    ERROR     :     4
    INFO      :     5
    WARNING   :     3

Top Errors:

    1. Database connection failed     (3x)
    2. Database connection            (1x)

=======================
```
