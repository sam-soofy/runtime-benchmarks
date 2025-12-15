// cpu-tasks.ts - CPU-bound operations
import type { BenchmarkResult, User } from './types';

// Utility to measure execution time
function measureTime(fn: () => void): number {
  const start = performance.now();
  fn();
  const end = performance.now();
  return end - start;
}

// Fibonacci calculation (recursive)
export function fibonacci(n: number): number {
  if (n <= 1) return n;
  return fibonacci(n - 1) + fibonacci(n - 2);
}

// Array operations: sort, map, filter, reduce
export function arrayOperations(): void {
  const size = 10000;
  
  // Generate random array
  const arr = Array.from({ length: size }, () => Math.floor(Math.random() * 1000));
  
  // Sort
  const sorted = [...arr].sort((a, b) => a - b);
  
  // Map, filter, reduce
  const result = sorted
    .map(x => x * 2)
    .filter(x => x > 500)
    .reduce((acc, val) => acc + val, 0);
  
  // Prevent optimization
  if (result < 0) console.log("Unexpected result");
}

// JSON serialization/deserialization
export function jsonOperations(): void {
  const data = {
    users: Array.from({ length: 100 }, (_, i): User => ({
      id: i,
      name: `User ${i}`,
      email: `user${i}@example.com`,
      active: i % 2 === 0,
      metadata: {
        created: new Date().toISOString(),
        score: Math.random() * 100
      }
    }))
  };
  
  // Serialize and deserialize multiple times
  for (let i = 0; i < 100; i++) {
    const serialized = JSON.stringify(data);
    const deserialized = JSON.parse(serialized);
    if (!deserialized.users) throw new Error("Parse failed");
  }
}

// Run all CPU tasks and return results
export async function runCpuTasks(): Promise<BenchmarkResult[]> {
  const results: BenchmarkResult[] = [];
  
  // Task 1: Fibonacci
  const fibTime = measureTime(() => {
    const result = fibonacci(35);
    if (result !== 9227465) throw new Error("Fibonacci calculation error");
  });
  results.push({ phase: 'Fibonacci(35)', durationMs: fibTime });
  console.log(`  ✓ Fibonacci(35): ${fibTime.toFixed(2)}ms`);
  
  // Task 2: Array Operations
  const arrayTime = measureTime(() => {
    for (let i = 0; i < 10; i++) {
      arrayOperations();
    }
  });
  results.push({ phase: 'Array Operations (10x)', durationMs: arrayTime });
  console.log(`  ✓ Array Operations (10x): ${arrayTime.toFixed(2)}ms`);
  
  // Task 3: JSON Operations
  const jsonTime = measureTime(() => {
    jsonOperations();
  });
  results.push({ phase: 'JSON Operations', durationMs: jsonTime });
  console.log(`  ✓ JSON Operations: ${jsonTime.toFixed(2)}ms`);
  
  return results;
}