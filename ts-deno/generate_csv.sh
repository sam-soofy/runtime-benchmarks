#!/bin/bash

# CSV Generator - Creates a large CSV file for benchmarking
# This generates realistic-looking data with the search word embedded

OUTPUT_FILE="data.csv"
ROWS=50000
SEARCH_WORD="example"

echo "📝 Generating CSV file with ${ROWS} rows..."

# Create header
echo "id,name,email,company,city,country,description" > $OUTPUT_FILE

# Sample data arrays
companies=("TechCorp" "DataSys" "CloudNet" "CodeWorks" "DevOps Inc" "example Corp" "Digital Solutions")
cities=("New York" "London" "Tokyo" "Paris" "Berlin" "Sydney" "Toronto" "example City")
countries=("USA" "UK" "Japan" "France" "Germany" "Australia" "Canada" "Example Land")

# Generate rows
for i in $(seq 1 $ROWS); do
    id=$i
    name="User ${i}"
    email="user${i}@example.com"
    company=${companies[$((i % 7))]}
    city=${cities[$((i % 8))]}
    country=${countries[$((i % 8))]}
    
    # Every 5th row gets "example" in description
    if [ $((i % 5)) -eq 0 ]; then
        description="This is an example description with example data for testing"
    else
        description="Regular description for row ${i} with various data points"
    fi
    
    echo "${id},${name},${email},${company},${city},${country},${description}" >> $OUTPUT_FILE
done

# Calculate file size
FILE_SIZE=$(du -h $OUTPUT_FILE | cut -f1)

echo "✅ Generated ${OUTPUT_FILE} (${FILE_SIZE})"
echo "   Rows: ${ROWS}"
echo "   Search word '${SEARCH_WORD}' appears multiple times"
echo ""
echo "You can now run: ./run.sh"