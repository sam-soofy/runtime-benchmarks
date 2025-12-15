"""
file_tasks.py - File I/O operations (optimized)
"""

import os
import re
import mmap
from typing import List


# Pre-compile regex pattern for reuse (much faster)
_pattern_cache = {}


def get_compiled_pattern(search_word: str):
    """Get or create compiled regex pattern"""
    if search_word not in _pattern_cache:
        _pattern_cache[search_word] = re.compile(search_word.encode(), re.IGNORECASE)
    return _pattern_cache[search_word]


def search_csv_file(file_path: str, search_word: str) -> None:
    """Search for a word in CSV file using memory mapping (faster for large files)"""
    
    # Check if file exists
    if not os.path.exists(file_path):
        message = f"CSV file not found: {file_path}\nSkipping CSV search."
        print(f"  ⚠️  {message}")
        with open('search_results.txt', 'w') as f:
            f.write(message)
        return
    
    # Use memory-mapped file for better performance on large files
    with open(file_path, 'r+b') as f:
        # Memory map the file
        with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mmapped_file:
            # Get pre-compiled pattern
            pattern = get_compiled_pattern(search_word)
            
            # Find all matches using compiled pattern on binary data
            matches = pattern.findall(mmapped_file)
            count = len(matches)
    
    # Prepare result message
    if count > 0:
        result_message = f'Found {count} matches for "{search_word}"'
    else:
        result_message = f'No matches found for "{search_word}"'
    
    # Write results to file (buffered write is already efficient)
    with open('search_results.txt', 'w') as f:
        f.write(result_message)
    
    print(f"  ✓ {result_message}")


def read_csv_lines(file_path: str) -> List[str]:
    """Read lines from CSV file efficiently"""
    if not os.path.exists(file_path):
        return []
    
    # Read file in one go and split (faster than line-by-line for small-medium files)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Filter empty lines in one pass
    return [line for line in content.split('\n') if line.strip()]