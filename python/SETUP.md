# Python Benchmark Setup

## 📁 Directory Structure

```
python/
├── main.py              # Entry point
├── types_def.py         # Type definitions (dataclasses)
├── cpu_tasks.py         # CPU-bound operations
├── network_tasks.py     # Network operations
├── file_tasks.py        # File I/O operations
├── requirements.txt     # Dependencies (optional)
├── run.sh              # Benchmark runner
├── generate_csv.sh     # CSV data generator
├── data.csv            # Test data (generated)
└── search_results.txt  # Output (generated)
```

## 🚀 Quick Start

```bash
# 1. Create directory
mkdir python && cd python

# 2. Save all Python files (main.py, types_def.py, etc.)

# 3. Make scripts executable
chmod +x run.sh generate_csv.sh

# 4. (Optional) Install aiohttp for better performance
pip3 install aiohttp
# OR
pip3 install -r requirements.txt

# 5. Generate test data
./generate_csv.sh

# 6. Run benchmark
./run.sh
```

## 📦 Dependencies

### Required
- Python 3.7+ (for dataclasses)
- Standard library modules: `asyncio`, `json`, `re`, `time`, `random`

### Optional (Recommended)
- `aiohttp` - For true async concurrent HTTP requests
  - Without it: Falls back to `urllib` (synchronous, slower)
  - With it: ~50% faster network operations

Install: `pip3 install aiohttp`

## 🎯 What Gets Tested

| Module | Operations |
|--------|------------|
| main.py | Orchestration, timing, module imports |
| cpu_tasks.py | Fibonacci, array ops, JSON serialization |
| file_tasks.py | CSV reading, regex search, file writing |
| network_tasks.py | 20 concurrent HTTP requests (4×5) |

## 📊 Expected Performance

Typical Python performance characteristics:
- **Startup**: ~50-100ms (slower than Go/Bun)
- **CPU tasks**: Slower than compiled languages (Go)
- **I/O tasks**: Competitive with proper async (aiohttp)
- **Memory**: Higher than Go, similar to Bun/Deno

## 🔧 Troubleshooting

### Missing Python 3
```bash
# macOS
brew install python3

# Ubuntu/Debian
sudo apt install python3 python3-pip

# Check version (need 3.7+)
python3 --version
```

### Import Errors
If you get `ModuleNotFoundError`:
```bash
# Make sure all .py files are in the same directory
ls *.py

# Should see:
# main.py
# types_def.py
# cpu_tasks.py
# network_tasks.py
# file_tasks.py
```

### Slow Network Operations
Install aiohttp for true concurrency:
```bash
pip3 install aiohttp
```

Without aiohttp, network requests run sequentially (~5-10x slower).

## 📈 Running the Benchmark

### Basic Run
```bash
./run.sh
```

### Custom Search Word
```bash
# Edit run.sh, line 13:
SEARCH_WORD="your_word"
```

### More Iterations
```bash
# Edit run.sh:
RUNS=5
WARMUP_RUNS=2
```

### Direct Execution
```bash
python3 main.py example
```

## 🔍 Comparing with Other Languages

Python will typically show:
- ✅ Clean, readable code
- ✅ Rich standard library
- ✅ Good I/O performance (with asyncio)
- ⚠️ Slower CPU-bound operations
- ⚠️ Higher memory usage
- ⚠️ Longer startup time

This is expected and normal for an interpreted language!

## 💡 Tips

1. **Use PyPy** for better CPU performance:
   ```bash
   pypy3 main.py example
   ```

2. **Profile specific sections**:
   ```python
   import cProfile
   cProfile.run('run_benchmark()')
   ```

3. **Check memory**:
   ```bash
   # Linux
   /usr/bin/time -v python3 main.py
   
   # macOS
   time -l python3 main.py
   ```

## ✅ Verification

After setup, test each module:

```bash
# Test imports
python3 -c "from cpu_tasks import run_cpu_tasks; print('✓ cpu_tasks')"
python3 -c "from network_tasks import run_network_tasks; print('✓ network_tasks')"
python3 -c "from file_tasks import search_csv_file; print('✓ file_tasks')"

# Generate data
./generate_csv.sh

# Run full benchmark
./run.sh
```

You should see output similar to:
```
🚀 Starting Benchmark (Python Runtime)
==================================================

💻 CPU Operations:
  ✓ Fibonacci(35): 1245.32ms
  ✓ Array Operations (10x): 189.45ms
  ✓ JSON Operations: 256.78ms

📁 File Operations:
  ✓ Found 15234 matches for "example"
  ✓ CSV Search & Write: 434.56ms

📡 Network Operations:
  Round 1/4: 867.89ms
  Round 2/4: 823.45ms
  Round 3/4: 834.12ms
  Round 4/4: 845.67ms
```
