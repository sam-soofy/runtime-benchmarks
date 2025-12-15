# Setup Guide - Modular Benchmark Suite

## 📁 Directory Structure for ts-deno/

```
ts-deno/
├── main.ts              # Entry point - orchestrates all benchmarks
├── types.ts             # Shared TypeScript interfaces
├── cpu-tasks.ts         # CPU-bound operations (Fib, arrays, JSON)
├── network-tasks.ts     # Network operations (concurrent fetches)
├── file-tasks.ts        # File I/O (CSV read, search, write)
├── package.json         # Deno configuration
├── run.sh              # Benchmark runner script
├── generate_csv.sh     # CSV data generator
├── data.csv            # Generated test data (50K rows, ~5MB)
└── search_results.txt  # Output from CSV search (generated)
```

## 🔧 Setup Steps

### Step 1: Create Directory Structure

```bash
mkdir -p ts-deno
cd ts-deno
```

### Step 2: Create All Files

Save each artifact I provided:

1. **main.ts** - Entry point
2. **types.ts** - Type definitions
3. **cpu-tasks.ts** - CPU operations module
4. **network-tasks.ts** - Network operations module
5. **file-tasks.ts** - File operations module
6. **package.json** - Package configuration
7. **run.sh** - Benchmark runner
8. **generate_csv.sh** - CSV generator

### Step 3: Make Scripts Executable

```bash
deno init
deno install
chmod +x run.sh
chmod +x generate_csv.sh
```

### Step 4: Generate Test Data

```bash
./generate_csv.sh
```

This creates `data.csv` with 50,000 rows containing:

- User IDs, names, emails
- Companies, cities, countries
- Descriptions (every 5th row contains "example")

### Step 5: Run Benchmark

```bash
./run.sh
```

## 🎯 What Each Module Does

### main.ts (Orchestrator)

- Imports all modules
- Measures overall timing
- Coordinates benchmark phases
- Displays summary results

### types.ts (Shared Types)

- `BenchmarkResult`: Timing data structure
- `User`: JSON operation data structure
- Ensures type consistency across modules

### cpu-tasks.ts (CPU Operations)

```typescript
export function fibonacci(n: number): number
export function arrayOperations(): void
export function jsonOperations(): void
export async function runCpuTasks(): Promise<BenchmarkResult[]>
```

### network-tasks.ts (Network Operations)

```typescript
async function fetchConcurrent(count: number): Promise<void>
export async function runNetworkTasks(): Promise<BenchmarkResult[]>
```

### file-tasks.ts (File Operations)

```typescript
export async function searchCsvFile(filePath: string, searchWord: string): Promise<void>
export function readCsvLines(filePath: string): string[]
```

## 🚀 Running the Benchmark

### Basic Run

```bash
./run.sh
```

Performs:

- 1 warmup run (discarded)
- 3 measured runs
- Timing with `time` command
- Memory stats (if available)

### Custom Search Word

```bash
# Edit run.sh, line 13:
SEARCH_WORD="your_word"
```

Or pass as argument in main.ts:

```bash
deno run main.ts "your_word"
```

### More Iterations

```bash
# Edit run.sh:
RUNS=5        # Number of benchmark runs
WARMUP_RUNS=2 # Number of warmup runs
```

## 📊 Understanding Output

### Console Output Example

```
🚀 Starting Benchmark (Deno Runtime)
==================================================

💻 CPU Operations:
  ✓ Fibonacci(35): 245.32ms
  ✓ Array Operations (10x): 89.45ms
  ✓ JSON Operations: 156.78ms

📁 File Operations:
  ✓ Found 15234 matches for "example"
  ✓ CSV Search & Write: 234.56ms

📡 Network Operations:
  Round 1/4: 567.89ms
  Round 2/4: 523.45ms
  Round 3/4: 534.12ms
  Round 4/4: 545.67ms

==================================================
📊 Summary:
   Total Execution Time: 2897.24ms
   CPU Operations: 491.55ms
   File Operations: 234.56ms
   Network Operations: 2171.13ms
==================================================
```

### Time Command Output (Linux with /usr/bin/time -v)

```
Command being timed: "deno run main.ts example"
User time (seconds): 2.45
System time (seconds): 0.23
Elapsed (wall clock) time: 2.897
Maximum resident set size (kbytes): 102400
```

### Time Command Output (macOS)

```
real    0m2.897s
user    0m2.450s
sys     0m0.230s
```

## 🔍 Troubleshooting

### Issue: "data.csv not found"

**Solution**: Run `./generate_csv.sh` first

### Issue: "Deno command not found"

**Solution**: Install Deno:

```bash
curl -fsSL https://deno.sh/install | bash
source ~/.bashrc  # or ~/.zshrc
```

### Issue: "Permission denied"

**Solution**: Make scripts executable:

```bash
chmod +x run.sh generate_csv.sh
```

### Issue: Network requests timeout

**Solution**:

- Check internet connection
- Increase timeout in network-tasks.ts
- Reduce concurrent requests from 5 to 3

### Issue: High variance between runs

**Solution**:

- Close other applications
- Increase warmup runs
- Run more iterations (5-10)
- Check system load (`top` or `htop`)

## 🎛️ Configuration Options

### CSV Generator (generate_csv.sh)

```bash
ROWS=50000        # Number of CSV rows
SEARCH_WORD="example"  # Word to embed in data
```

### Benchmark Runner (run.sh)

```bash
RUNS=3            # Measured iterations
WARMUP_RUNS=1     # Warmup iterations
SEARCH_WORD="example"  # Word to search in CSV
```

### CPU Tasks (cpu-tasks.ts)

```typescript
fibonacci(35)     // Complexity: 30=fast, 35=medium, 40=slow
size = 10000      // Array size: affects memory/time
iterations = 100  // JSON operations count
```

### Network Tasks (network-tasks.ts)

```typescript
rounds = 4        // Number of fetch rounds
concurrent = 5    // Requests per round
```

## 📈 Next Steps

1. **Test Deno Implementation**: `cd ts-deno && ./run.sh`
2. **Review Results**: Check timing and memory usage
3. **Create Deno Version**: Port the same code to ts-deno/
4. **Create Go Version**: Implement equivalent in golang/
5. **Compare**: Run all three and analyze differences

## 💡 Tips

- **Consistent Environment**: Run all benchmarks on same machine
- **Quiet System**: Close browsers, IDEs, etc. during benchmark
- **Multiple Runs**: Average results from 3-5 runs
- **Save Results**: `./run.sh > results.txt 2>&1`
- **Track Changes**: Git commit each version for comparison

## 🎓 Learning Points

This modular structure tests:

1. **Module System**: How fast can runtime load/parse multiple files?
2. **File I/O**: Buffer management, string operations
3. **Memory Management**: GC overhead, allocation patterns
4. **Concurrency**: Promise handling (TS) vs goroutines (Go)
5. **Startup Overhead**: Runtime initialization cost

Each language/runtime will excel in different areas!
