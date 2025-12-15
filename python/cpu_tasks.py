"""
cpu_tasks.py - CPU-bound operations
"""

import time
import json
import random
from datetime import datetime
from typing import List
from types_def import BenchmarkResult, User


def measure_time(func):
    """Measure execution time of a function"""
    start = time.perf_counter()
    func()
    end = time.perf_counter()
    return (end - start) * 1000


def fibonacci(n: int) -> int:
    """Fibonacci calculation (recursive)"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def array_operations() -> None:
    """Array operations: sort, map, filter, reduce"""
    size = 10000

    # Generate random array
    arr = [random.randint(0, 999) for _ in range(size)]

    # Sort
    sorted_arr = sorted(arr)

    # Map, filter, reduce
    result = sum(x for x in (x * 2 for x in sorted_arr) if x > 500)

    # Prevent optimization
    if result < 0:
        print("Unexpected result")


def json_operations() -> None:
    """JSON serialization/deserialization"""
    data = {
        "users": [
            {
                "id": i,
                "name": f"User {i}",
                "email": f"user{i}@example.com",
                "active": i % 2 == 0,
                "metadata": {
                    "created": datetime.now().isoformat(),
                    "score": random.random() * 100,
                },
            }
            for i in range(100)
        ]
    }

    # Serialize and deserialize multiple times
    for _ in range(100):
        serialized = json.dumps(data)
        deserialized = json.loads(serialized)
        if "users" not in deserialized:
            raise ValueError("Parse failed")


def run_cpu_tasks() -> List[BenchmarkResult]:
    """Run all CPU tasks and return results"""
    results = []

    # Task 1: Fibonacci
    fib_time = measure_time(lambda: None)  # Start measurement
    result = fibonacci(35)
    fib_time = measure_time(lambda: fibonacci(35))
    if result != 9227465:
        raise ValueError("Fibonacci calculation error")
    results.append(BenchmarkResult(phase="Fibonacci(35)", duration_ms=fib_time))
    print(f"  ✓ Fibonacci(35): {fib_time:.2f}ms")

    # Task 2: Array Operations
    array_time = measure_time(lambda: [array_operations() for _ in range(10)])
    results.append(
        BenchmarkResult(phase="Array Operations (10x)", duration_ms=array_time)
    )
    print(f"  ✓ Array Operations (10x): {array_time:.2f}ms")

    # Task 3: JSON Operations
    json_time = measure_time(json_operations)
    results.append(BenchmarkResult(phase="JSON Operations", duration_ms=json_time))
    print(f"  ✓ JSON Operations: {json_time:.2f}ms")

    return results
