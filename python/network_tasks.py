"""
network_tasks.py - Network I/O operations
"""

import asyncio
import time
from typing import List
from types_def import BenchmarkResult

try:
    import aiohttp

    HAS_AIOHTTP = True
except ImportError:
    HAS_AIOHTTP = False
    import urllib.request
    import json as json_lib


async def fetch_concurrent_aiohttp(count: int) -> None:
    """Fetch multiple URLs concurrently using aiohttp"""
    urls = [
        f"https://jsonplaceholder.typicode.com/posts/{(i % 100) + 1}"
        for i in range(count)
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [session.get(url) for url in urls]
        responses = await asyncio.gather(*tasks)

        # Read JSON from responses
        for response in responses:
            await response.json()
            response.close()


def fetch_concurrent_urllib(count: int) -> None:
    """Fetch multiple URLs using urllib (fallback)"""
    urls = [
        f"https://jsonplaceholder.typicode.com/posts/{(i % 100) + 1}"
        for i in range(count)
    ]

    for url in urls:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            json_lib.loads(data)


async def fetch_concurrent(count: int) -> None:
    """Fetch multiple URLs concurrently"""
    if HAS_AIOHTTP:
        await fetch_concurrent_aiohttp(count)
    else:
        # Fallback to synchronous (not truly concurrent, but functional)
        fetch_concurrent_urllib(count)


async def measure_time_async(func, *args) -> float:
    """Measure execution time of async function"""
    start = time.perf_counter()
    await func(*args)
    end = time.perf_counter()
    return (end - start) * 1000


async def run_network_tasks() -> List[BenchmarkResult]:
    """Run network tasks: 4 rounds of 5 concurrent requests"""
    results = []
    total_fetch_time = 0.0

    for round_num in range(1, 5):
        fetch_time = await measure_time_async(fetch_concurrent, 5)
        total_fetch_time += fetch_time
        print(f"  Round {round_num}/4: {fetch_time:.2f}ms")

    results.append(
        BenchmarkResult(phase="Network Operations (4x5)", duration_ms=total_fetch_time)
    )

    return results
