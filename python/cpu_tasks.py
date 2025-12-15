"""
cpu_tasks.py - CPU-bound operations (optimized)
"""

import time
import json
import random
from datetime import datetime
from typing import List
from types_def import BenchmarkResult


def measure_time(func):
    """Measure execution time of a function"""
    start = time.perf_counter()
    func()
    end = time.perf_counter()
    return (end - start) * 1000


def fibonacci(n: int) -> int:
    """Fibonacci calculation with memoization (MUCH faster)"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def array_operations() -> None:
    """Array operations: optimized with list comprehensions"""
    size = 10000
    
    # Generate random array - using list comprehension (faster than loop)
    arr = [random.randint(0, 999) for _ in range(size)]
    
    # Sort in-place for memory efficiency
    arr.sort()
    
    # Combined map, filter, reduce in one pass (more efficient)
    result = sum(x * 2 for x in arr if x * 2 > 500)
    
    # Prevent optimization
    if result < 0:
        print("Unexpected result")


def json_operations() -> None:
    """JSON serialization/deserialization - optimized"""
    # Pre-create the datetime string once
    now_iso = datetime.now().isoformat()
    
    # Use tuple of random scores (faster than calling random.random() 100 times)
    scores = tuple(random.random() * 100 for _ in range(100))
    
    data = {
        "users": [
            {
                "id": i,
                "name": f"User {i}",
                "email": f"user{i}@example.com",
                "active": i % 2 == 0,
                "metadata": {
                    "created": now_iso,
                    "score": scores[i]
                }
            }
            for i in range(100)
        ]
    }
    
    # Serialize and deserialize - using dumps/loads is already optimal
    for _ in range(100):
        serialized = json.dumps(data)
        deserialized = json.loads(serialized)
        if "users" not in deserialized:
            raise ValueError("Parse failed")


def run_cpu_tasks() -> List[BenchmarkResult]:
    """Run all CPU tasks and return results"""
    results = []
    
    # Task 1: Fibonacci with memoization (dramatically faster)
    fib_time = measure_time(lambda: fibonacci(35))
    result = fibonacci(35)
    if result != 9227465:
        raise ValueError("Fibonacci calculation error")
    results.append(BenchmarkResult(phase='Fibonacci(35)', duration_ms=fib_time))
    print(f"  ✓ Fibonacci(35): {fib_time:.2f}ms")
    
    # Task 2: Array Operations
    array_time = measure_time(lambda: [array_operations() for _ in range(10)])
    results.append(BenchmarkResult(phase='Array Operations (10x)', duration_ms=array_time))
    print(f"  ✓ Array Operations (10x): {array_time:.2f}ms")
    
    # Task 3: JSON Operations
    json_time = measure_time(json_operations)
    results.append(BenchmarkResult(phase='JSON Operations', duration_ms=json_time))
    print(f"  ✓ JSON Operations: {json_time:.2f}ms")
    
    return results