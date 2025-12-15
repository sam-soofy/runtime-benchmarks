#!/bin/bash

# Benchmark Runner for Bun Runtime
# This script runs the benchmark multiple times and collects statistics

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Configuration
RUNS=3
WARMUP_RUNS=1
SEARCH_WORD="example"

echo -e "${BLUE}╔════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║  Benchmark Suite - TypeScript with Bun        ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════╝${NC}"
echo ""

# Check if bun is installed
if ! command -v bun &> /dev/null; then
    echo -e "${RED}⚠️  Bun is not installed!${NC}"
    echo "Please install Bun: curl -fsSL https://bun.sh/install | bash"
    exit 1
fi

# Display runtime version
echo -e "${GREEN}Runtime Version:${NC}"
bun --version
echo ""

# Check if data.csv exists
if [ ! -f "data.csv" ]; then
    echo -e "${YELLOW}⚠️  data.csv not found!${NC}"
    echo "Please provide a data.csv file or the benchmark will skip CSV search."
    echo "You can create one with: ./generate_csv.sh"
    echo ""
fi

# Clean up old results
rm -f search_results.txt

# Warmup runs
echo -e "${YELLOW}🔥 Warmup Runs (${WARMUP_RUNS}x)...${NC}"
for i in $(seq 1 $WARMUP_RUNS); do
    bun run main.ts "$SEARCH_WORD" > /dev/null 2>&1 || true
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
            /usr/bin/time -v bun run main.ts "$SEARCH_WORD" 2>&1 | tee -a "$RESULTS_FILE"
        else
            time bun run main.ts "$SEARCH_WORD" 2>&1 | tee -a "$RESULTS_FILE"
        fi
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS: Use time -l for memory stats
        { time bun run main.ts "$SEARCH_WORD"; } 2>&1 | tee -a "$RESULTS_FILE"
    else
        # Fallback: Basic time
        time bun run main.ts "$SEARCH_WORD" 2>&1 | tee -a "$RESULTS_FILE"
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

echo -e "${BLUE}Full results saved to: ${RESULTS_FILE}${NC}"
echo -e "${YELLOW}Tip: Review the results file for detailed timing information${NC}"
echo ""

# Try to extract and display summary if possible
echo -e "${GREEN}📈 Quick Summary:${NC}"
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "   Check the 'Elapsed (wall clock) time' and 'Maximum resident set size' in output above"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    echo "   Check the 'real' time and memory stats in output above"
fi

# Cleanup
echo ""
echo -e "${BLUE}Results are in: ${RESULTS_FILE}${NC}"
echo "To save permanently: cp $RESULTS_FILE ./benchmark_results.txt"