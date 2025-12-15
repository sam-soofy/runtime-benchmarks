// main.ts - Entry point for Bun Runtime Benchmark
import { runCpuTasks } from './cpu-tasks';
import { runNetworkTasks } from './network-tasks';
import { searchCsvFile } from './file-tasks';
import type { BenchmarkResult } from './types';

// Utility to measure execution time
export function measureTime(fn: () => Promise<void> | void): Promise<number> {
  return new Promise(async (resolve) => {
    const start = performance.now();
    await fn();
    const end = performance.now();
    resolve(end - start);
  });
}

// Main benchmark orchestrator
async function runBenchmark(): Promise<void> {
  const results: BenchmarkResult[] = [];
  const totalStart = performance.now();
  
  console.log("🚀 Starting Benchmark (Bun Runtime)");
  console.log("=".repeat(50));
  
  // Phase 1: CPU-bound operations
  console.log("\n💻 CPU Operations:");
  const cpuResults = await runCpuTasks();
  results.push(...cpuResults);
  
  // Phase 2: File operations (CSV search)
  console.log("\n📁 File Operations:");
  const csvFile = './data.csv';
  const searchWord = process.argv[2] || 'example';
  
  const fileTime = await measureTime(async () => {
    await searchCsvFile(csvFile, searchWord);
  });
  results.push({ phase: 'CSV Search & Write', durationMs: fileTime });
  console.log(`✓ CSV Search & Write: ${fileTime.toFixed(2)}ms`);
  
  // Phase 3: Network operations
  console.log("\n📡 Network Operations:");
  const networkResults = await runNetworkTasks();
  results.push(...networkResults);
  
  // Calculate totals
  const totalEnd = performance.now();
  const totalTime = totalEnd - totalStart;
  const cpuTime = cpuResults.reduce((sum, r) => sum + r.durationMs, 0);
  const networkTime = networkResults.reduce((sum, r) => sum + r.durationMs, 0);
  
  console.log("\n" + "=".repeat(50));
  console.log("📊 Summary:");
  console.log(`   Total Execution Time: ${totalTime.toFixed(2)}ms`);
  console.log(`   CPU Operations: ${cpuTime.toFixed(2)}ms`);
  console.log(`   File Operations: ${fileTime.toFixed(2)}ms`);
  console.log(`   Network Operations: ${networkTime.toFixed(2)}ms`);
  console.log("=".repeat(50));
}

// Run the benchmark
runBenchmark().catch(err => {
  console.error("❌ Benchmark failed:", err);
  process.exit(1);
});