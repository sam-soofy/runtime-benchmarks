#!/bin/bash

# Optimized Benchmark Runner for Python Runtime
# Assumes environment is already activated with all dependencies installed

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Configuration
RUNS=3
WARMUP_RUNS=1
SEARCH_WORD="example"

echo -e "${BLUE}╔════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║  Benchmark Suite - Python Runtime             ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════╝${NC}"
echo ""

# Warmup runs (no output)
echo -e "${YELLOW}🔥 Warmup Runs (${WARMUP_RUNS}x)...${NC}"
for i in $(seq 1 $WARMUP_RUNS); do
    python3 main.py "$SEARCH_WORD" > /dev/null 2>&1
done
echo ""

# Create temporary file for results
RESULTS_FILE=$(mktemp)

echo -e "${GREEN}📊 Running ${RUNS} benchmark iterations...${NC}"
echo ""

# Run benchmarks
for i in $(seq 1 $RUNS); do
    echo -e "${BLUE}━━━ Run $i/$RUNS ━━━${NC}"
    
    # Use time command (works on both Linux and macOS)
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Linux: Use /usr/bin/time -v for detailed stats
        if command -v /usr/bin/time &> /dev/null; then
            /usr/bin/time -v python3 main.py "$SEARCH_WORD" 2>&1 | tee -a "$RESULTS_FILE"
        else
            time python3 main.py "$SEARCH_WORD" 2>&1 | tee -a "$RESULTS_FILE"
        fi
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS: Use time -l for memory stats
        { time python3 main.py "$SEARCH_WORD"; } 2>&1 | tee -a "$RESULTS_FILE"
    else
        # Fallback: Basic time
        time python3 main.py "$SEARCH_WORD" 2>&1 | tee -a "$RESULTS_FILE"
    fi
    
    echo ""
done

echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✅ Benchmark Complete!${NC}"
echo ""

# Display search results if available
if [ -f "search_results.txt" ]; then
    echo -e "${BLUE}📝 CSV Search Results:${NC}"
    cat search_results.txt
    echo ""
fi

echo -e "${BLUE}Full results: ${RESULTS_FILE}${NC}"
echo "To save: cp $RESULTS_FILE ./benchmark_results.txt"