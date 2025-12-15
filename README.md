# Language & Runtime Benchmark Suite

A comprehensive benchmarking suite to compare TypeScript (Bun & Deno) vs Go vs Python for real-world applications with modular architecture and file I/O operations.

🤔 For a long time, I was considering switching to GoLang for some projects, but since Deno and TypeScript, I wasn't as sure. Each time I ran Next.js projects with Deno, I was happier—it was faster to run, compile, load pages (faster than both Bun and Node.js), and recompile changes during development.

📊 So I decided to create this benchmark suite testing CPU, I/O operations, startup time, and resource usage across 4 runtimes in 3 languages. I hope these results help you make data-driven decisions about which runtime fits your needs.

🐍 **Python benchmarks included** with multiple optimized runs to ensure fair comparison. Note that **network I/O performance varies significantly** due to external API latency and our network connectivity, so results may differ between runs. Network benchmarks are susceptible to connectivity fluctuations—focus on CPU and file I/O metrics for deterministic comparisons. Python excels in memory efficiency but faces challenges with startup time and recursive CPU tasks.

📝 **Code Complexity Matters:** Beyond raw performance, I wanted to understand **developer experience and code maintainability** across languages. This benchmark also tracks **lines of code (LOC)** for the same functionality—showing how verbose or concise each language is. Less code is often easier to maintain, debug, and understand. TypeScript/JavaScript's conciseness shines here, while Go and Python require more verbosity for the same logic. The comparison helps you decide: do you prioritize performance, speed of development, or a balance of both?

⚠️ **Disclaimer:** I can't guarantee accuracy yet—I'm new to Go and used AI to accelerate development. In the future, I'll review and refine the code. Meanwhile, feel free to run these benchmarks yourself and share your results!

🐦 Follow me on X: [@EliteATT](https://x.com/EliteATT)

## 🎯 Quick Results Summary

**Averaged across 3 runs:**

| Metric | Bun | Deno | Go | Python |
|--------|-----|------|-----|--------|
| **Total Time** | 2619.5ms | 2257.5ms | 2584.2ms | 6124.1ms |
| **CPU Operations** | 108.7ms | 137.0ms | 86.3ms | 1375.4ms |
| **File I/O** | 12.1ms | 31.4ms | 262.8ms | 43.1ms |
| **Network (20 reqs)** | 2497.0ms | 2088.3ms | 2235.2ms | 3418.4ms |
| **Memory Peak** | 77.6 MB | 81.3 MB | 26.9 MB | 47.9 MB |
| **Startup Overhead** | ~130ms | ~70ms | ~580ms* | ~130ms |
| **Lines of Code** | 248 | 263 | 382 | 358 |

**Key Takeaways:**

- 🏆 **Deno**: Fastest overall execution (2257.5ms) with good startup and exceptional I/O tasks, concise TypeScript code (263 LOC), but not most efficient and fastest on CPU and memory heavy tasks
- ⚡ **Bun**: Fastest CPU operations (108.7ms), most concise code (248 LOC), best overall balance of performance and brevity, but not the best heavy network tasks (maybe can be better in a more Bun way of things) and not the fastest startup
- 💾 **Go**: Best memory efficiency (26.9 MB) and CPU performance, but most verbose code (382 LOC) and slowest file I/O (262.8ms)*
- 🐍 **Python**: Strong file I/O performance (43.1ms) with moderate code length (358 LOC), but slowest in CPU-bound recursion

*- Go's startup overhead includes binary compilation (not with the "run.sh" which should use the already compiled binary); JIT runtimes show runtime initialization cost

## 📋 Overview

This benchmark tests:

- **Module Loading**: Multiple files imported at startup
- **CPU-bound operations**: Fibonacci, array operations, JSON processing
- **File I/O**: Reading large CSV files, string searching, writing results
- **Network I/O**: 20 concurrent HTTP requests (5 requests × 4 rounds)
- **Memory usage**: Peak memory consumption
- **Total execution time**: End-to-end performance
- **Code complexity**: Lines of code needed for clean, typed, idiomatic implementations

## 📐 Code Metrics

Beyond performance, code verbosity matters for maintainability and development speed. Here's how each language compares in lines of code for identical functionality (all implementations use proper typing and follow language conventions):

**Command to count lines:**

```bash
echo "📊 Lines of Code Count" && echo && echo "TypeScript (Bun):" && find ts-bun -name "*.ts" -not -path "*/node_modules/*" -type f -exec wc -l {} + && echo && echo "TypeScript (Deno):" && find ts-deno -name "*.ts" -not -path "*/node_modules/*" -type f -exec wc -l {} + && echo && echo "Python:" && find python -name "*.py" -not -path "*/.venv/*" -not -path "*/__pycache__/*" -type f -exec wc -l {} + && echo && echo "Go:" && find golang -name "*.go" -type f -exec wc -l {} +
```

**Results Breakdown:**

- **Bun (248 LOC)**: Most concise, TypeScript's expressive syntax eliminates boilerplate
- **Deno (263 LOC)**: Nearly identical to Bun, slightly more due to test file inclusion
- **Python (358 LOC)**: More verbose due to explicit error handling and type hints
- **Go (382 LOC)**: Most verbose; explicit error checking and type declarations add significant code

## 🏗️ Project Structure

```
.
├── ts-bun/              # TypeScript with Bun runtime
│   ├── main.ts          # Entry point & orchestration
│   ├── types.ts         # Shared type definitions
│   ├── cpu-tasks.ts     # CPU-bound operations
│   ├── network-tasks.ts # Network operations
│   ├── file-tasks.ts    # File I/O operations
│   ├── package.json     # Bun configuration
│   ├── run.sh           # Benchmark runner
│   ├── generate_csv.sh  # CSV data generator
│   └── data.csv         # Test data (generated)
│
├── ts-deno/             # TypeScript with Deno runtime
│   ├── (same structure)
│
├── python/              # Python implementation
│   ├── main.py          # Entry point & orchestration
│   ├── types_def.py     # Type definitions
│   ├── cpu_tasks.py     # CPU-bound operations
│   ├── network_tasks.py # Network operations
│   ├── file_tasks.py    # File I/O operations
│   ├── pyproject.toml   # Python configuration
│   ├── run.sh           # Benchmark runner
│   ├── generate_csv.sh  # CSV data generator
│   └── data.csv         # Test data (generated)
│
└── golang/              # Go implementation
    ├── main.go
    ├── cpu_tasks.go
    ├── network_tasks.go
    ├── file_tasks.go
    ├── run.sh
    ├── generate_csv.sh
    └── data.csv
```

## 🚀 Quick Start

### 1. TypeScript with Bun (ts-bun/)

```bash
# Install Bun
curl -fsSL https://bun.sh/install | bash

# Navigate to directory
cd ts-bun/

# Generate test data
chmod +x generate_csv.sh
./generate_csv.sh

# Run benchmark
chmod +x run.sh
./run.sh
```

### 2. TypeScript with Deno (ts-deno/)

```bash
# Install Deno
curl -fsSL https://deno.land/install.sh | sh

# Navigate to directory
cd ts-deno/

# Generate test data
chmod +x generate_csv.sh
./generate_csv.sh

# Run benchmark
chmod +x run.sh
./run.sh
```

### 3. Python (python/)

```bash
# Install Python (if needed)
# macOS: brew install python3
# Linux: apt install python3

# Navigate to directory
cd python/

# Generate test data
chmod +x generate_csv.sh
./generate_csv.sh

# Run benchmark
chmod +x run.sh
./run.sh
```

### 4. Go (golang/)

```bash
# Install Go (if needed)
# macOS: brew install go
# Linux: apt install golang

# Navigate to directory
cd golang/

# Generate test data
chmod +x generate_csv.sh
./generate_csv.sh

# Run benchmark
chmod +x run.sh
./run.sh
```

## 📊 Benchmark Details

### Module Loading

Each implementation is split into separate modules:

- **Types/Interfaces**: Shared data structures
- **CPU Tasks**: Computational operations
- **Network Tasks**: HTTP requests
- **File Tasks**: CSV reading and searching
- **Main**: Orchestration and timing

This tests how each runtime handles module imports and initialization.

### CPU Operations

1. **Fibonacci(35)**: Recursive algorithm (tests call stack & computation)
2. **Array Operations (10x)**:
   - Generate 10,000 random numbers
   - Sort, map, filter, reduce
   - Repeated 10 times
3. **JSON Operations**:
   - Serialize/deserialize 100 user objects
   - Repeated 100 times

### File Operations

1. **CSV Reading**: Load entire CSV file (~5MB with 50,000 rows)
2. **String Search**: Case-insensitive regex search for target word
3. **Result Writing**: Write findings to `search_results.txt`

### Network Operations

- **API**: JSONPlaceholder (<https://jsonplaceholder.typicode.com>)
- **Pattern**: 5 concurrent requests per round
- **Rounds**: 4 rounds (20 total requests)
- **Method**: Promise.all() (TS) / WaitGroups (Go)

## 📈 Measurements

### Internal (Program Output)

- Module loading overhead
- Per-phase timing (CPU, File, Network)
- Total execution time
- Operation breakdown

### External (Shell Script)

- **Real time**: Wall-clock time (includes startup)
- **User time**: CPU time in user mode
- **Sys time**: CPU time in kernel mode
- **Memory**: Peak RSS (Linux) or max resident (macOS)

## 🎯 Usage

### Generate Test Data

```bash
# In each directory (ts-bun, ts-deno, golang)
./generate_csv.sh
```

This creates a `data.csv` file with 50,000 rows (~5MB) containing the word "example" multiple times.

### Run Single Benchmark

```bash
cd ts-bun  # or ts-deno, python, or golang
./run.sh
```

### Custom Search Word

```bash
# Edit run.sh and change:
SEARCH_WORD="example"  # Change to your word
```

### Multiple Runs (for averaging)

```bash
# Edit run.sh and change:
RUNS=5        # Number of benchmark runs
WARMUP_RUNS=2 # Number of warmup runs
```

## 📝 Comparing Results

### Key Metrics to Compare

1. **Startup Time**:
   - Real time - (Internal total time)
   - Shows runtime initialization overhead

2. **Module Loading**:
   - Time difference between runtime start and first operation
   - Faster = better module system

3. **CPU Performance**:
   - Total time for Fibonacci + Array + JSON operations
   - Pure computational speed

4. **File I/O**:
   - CSV read + search + write time
   - Tests filesystem performance and string operations

5. **Network Performance**:
   - Total time for 20 concurrent requests
   - Tests async/concurrency handling

6. **Memory Efficiency**:
   - Maximum resident set size
   - Lower = better memory management

7. **Consistency**:
   - Variance between runs
   - Lower variance = more predictable

## 🎛️ Customization

### Adjust CSV Size

In `generate_csv.sh`:

```bash
ROWS=50000  # Try 10000, 100000, 500000
```

### Change Search Word

In `run.sh`:

```bash
SEARCH_WORD="example"  # Change to match your CSV content
```

### Adjust Workload Intensity

In CPU tasks module:

```typescript
// Fibonacci complexity
fibonacci(35)  // Try 30 (faster) or 40 (slower)

// Array size
const size = 10000;  // Try 5000, 20000

// JSON iterations
for (let i = 0; i < 100; i++)  // Try 50, 200
```

In network tasks module:

```typescript
// Rounds and concurrency
for (let round = 1; round <= 4; round++)  // Try 2, 6, 10
  fetchConcurrent(5)  // Try 3, 10, 20
```

## 🔍 Expected Results

### Typical Performance Characteristics

**Go:**

- ✅ Fastest startup (~5-20ms)
- ✅ Best memory efficiency (~30-50MB)
- ✅ Consistent performance (low variance)
- ✅ Excellent concurrency (goroutines)
- ⚠️ More verbose code

**Bun:**

- ✅ Fast TypeScript execution
- ✅ Modern JavaScript APIs
- ✅ Good startup time (~20-50ms)
- ⚠️ Higher memory than Go (~100-200MB)
- ✅ Native TypeScript support

**Deno:**

- ✅ Secure by default
- ✅ Native TypeScript
- ✅ Built-in tooling
- ⚠️ Slower startup than Bun (~50-100ms)
- ⚠️ Permission system overhead

**Python:**

- ✅ Excellent file I/O performance
- ✅ Good memory efficiency (~50MB)
- ⚠️ Slow recursive CPU operations (Fibonacci)
- ⚠️ Higher network latency handling
- ⚠️ Moderate startup time (~130ms)

### What to Look For

1. **Go should win**: Startup time, memory usage, CPU tasks
2. **Bun should be close**: Overall performance, competitive with Go
3. **Deno should be solid**: Good but slower startup, reliable
4. **Python should excel**: File I/O operations, memory usage
5. **All should handle I/O well**: Network varies due to external API latency

## 📦 Files Generated

- `data.csv` - Test data (50,000 rows, ~5MB)
- `search_results.txt` - Search results (updated each run)
- `benchmark_results.txt` - Timing data (if you save it)

## 🛡️ No External Dependencies

- **TypeScript**: Only Bun/Deno built-in APIs
- **Python**: Standard library only (asyncio, json, csv, re)
- **Go**: Only standard library
- **Network**: Free public API (JSONPlaceholder)

## ⚠️ Important Notes

1. **Use the same CSV file** across all implementations for fair comparison
2. **Run on the same machine** to eliminate hardware differences
3. **Close other applications** to reduce interference
4. **Run multiple times** to account for variance
5. **Consider warmup runs** - first run is often slower

## 🤝 Next Steps

After running all benchmarks:

1. **Collect Results**:

    ```bash
    # Save all results
    cd ts-bun && ./run.sh > ../results-bun.txt 2>&1
    cd ts-deno && ./run.sh > ../results-deno.txt 2>&1
    cd python && ./run.sh > ../results-python.txt 2>&1
    cd golang && ./run.sh > ../results-go.txt 2>&1
    ```

2. **Compare**: Look at total time, memory, and variance

3. **Decide**: Choose based on:
   - Performance requirements
   - Team expertise
   - Ecosystem needs
   - Deployment considerations

## 📄 License

MIT License - feel free to use and modify!
