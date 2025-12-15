#!/usr/bin/env python3
"""
main.py - Entry point for Python Benchmark
"""

import sys
import time
from typing import List
from cpu_tasks import run_cpu_tasks
from network_tasks import run_network_tasks
from file_tasks import search_csv_file
from types_def import BenchmarkResult


def measure_time(func, *args):
    """Utility to measure execution time"""
    start = time.perf_counter()
    result = func(*args)
    end = time.perf_counter()
    duration_ms = (end - start) * 1000
    return result, duration_ms


async def run_benchmark():
    """Main benchmark orchestrator"""
    results: List[BenchmarkResult] = []
    total_start = time.perf_counter()

    print("🚀 Starting Benchmark (Python Runtime)")
    print("=" * 50)

    # Phase 1: CPU-bound operations
    print("\n💻 CPU Operations:")
    cpu_results = run_cpu_tasks()
    results.extend(cpu_results)

    # Phase 2: File operations (CSV search)
    print("\n📁 File Operations:")
    csv_file = "./data.csv"
    search_word = sys.argv[1] if len(sys.argv) > 1 else "example"

    _, file_time = measure_time(search_csv_file, csv_file, search_word)
    results.append(BenchmarkResult(phase="CSV Search & Write", duration_ms=file_time))
    print(f"✓ CSV Search & Write: {file_time:.2f}ms")

    # Phase 3: Network operations
    print("\n📡 Network Operations:")
    network_results = await run_network_tasks()
    results.extend(network_results)

    # Calculate totals
    total_end = time.perf_counter()
    total_time = (total_end - total_start) * 1000

    cpu_time = sum(r.duration_ms for r in cpu_results)
    network_time = sum(r.duration_ms for r in network_results)

    print("\n" + "=" * 50)
    print("📊 Summary:")
    print(f"   Total Execution Time: {total_time:.2f}ms")
    print(f"   CPU Operations: {cpu_time:.2f}ms")
    print(f"   File Operations: {file_time:.2f}ms")
    print(f"   Network Operations: {network_time:.2f}ms")
    print("=" * 50)


if __name__ == "__main__":
    import asyncio

    try:
        asyncio.run(run_benchmark())
    except Exception as err:
        print(f"❌ Benchmark failed: {err}")
        sys.exit(1)
