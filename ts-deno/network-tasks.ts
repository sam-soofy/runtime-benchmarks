// network-tasks.ts - Network I/O operations
import type { BenchmarkResult } from './types';

// Fetch multiple URLs concurrently
async function fetchConcurrent(count: number): Promise<void> {
  const urls = Array.from(
    { length: count },
    (_, i) => `https://jsonplaceholder.typicode.com/posts/${(i % 100) + 1}`
  );
  
  const promises = urls.map(url => 
    fetch(url).then(res => res.json())
  );
  
  await Promise.all(promises);
}

// Utility to measure async execution time
async function measureTime(fn: () => Promise<void>): Promise<number> {
  const start = performance.now();
  await fn();
  const end = performance.now();
  return end - start;
}

// Run network tasks: 4 rounds of 5 concurrent requests
export async function runNetworkTasks(): Promise<BenchmarkResult[]> {
  const results: BenchmarkResult[] = [];
  let totalFetchTime = 0;
  
  for (let round = 1; round <= 4; round++) {
    const fetchTime = await measureTime(() => fetchConcurrent(5));
    totalFetchTime += fetchTime;
    console.log(`  Round ${round}/4: ${fetchTime.toFixed(2)}ms`);
  }
  
  results.push({ phase: 'Network Operations (4x5)', durationMs: totalFetchTime });
  
  return results;
}