"""
file_tasks.py - File I/O operations
"""

import os
import re
from typing import List


def search_csv_file(file_path: str, search_word: str) -> None:
    """Search for a word in CSV file and write results"""

    # Check if file exists
    if not os.path.exists(file_path):
        message = f"CSV file not found: {file_path}\nSkipping CSV search."
        print(f"  ⚠️  {message}")
        with open("search_results.txt", "w") as f:
            f.write(message)
        return

    # Read the entire CSV file
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Count occurrences of the search word (case-insensitive)
    pattern = re.compile(search_word, re.IGNORECASE)
    matches = pattern.findall(content)
    count = len(matches)

    # Prepare result message
    if count > 0:
        result_message = f'Found {count} matches for "{search_word}"'
    else:
        result_message = f'No matches found for "{search_word}"'

    # Write results to file
    with open("search_results.txt", "w") as f:
        f.write(result_message)

    print(f"  ✓ {result_message}")


def read_csv_lines(file_path: str) -> List[str]:
    """Read lines from CSV file"""
    if not os.path.exists(file_path):
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    return lines
