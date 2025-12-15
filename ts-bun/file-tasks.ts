// file-tasks.ts - File I/O operations
import { readFileSync, writeFileSync, existsSync } from 'fs';

// Search for a word in CSV file and write results
export async function searchCsvFile(filePath: string, searchWord: string): Promise<void> {
  // Check if file exists
  if (!existsSync(filePath)) {
    const message = `CSV file not found: ${filePath}\nSkipping CSV search.`;
    console.log(`  ⚠️  ${message}`);
    writeFileSync('search_results.txt', message);
    return;
  }
  
  // Read the entire CSV file
  const content = readFileSync(filePath, 'utf-8');
  
  // Count occurrences of the search word (case-insensitive)
  const regex = new RegExp(searchWord, 'gi');
  const matches = content.match(regex);
  const count = matches ? matches.length : 0;
  
  // Prepare result message
  const resultMessage = count > 0 
    ? `Found ${count} matches for "${searchWord}"`
    : `No matches found for "${searchWord}"`;
  
  // Write results to file
  writeFileSync('search_results.txt', resultMessage);
  
  console.log(`  ✓ ${resultMessage}`);
}

// Additional file utility: Read lines from CSV
export function readCsvLines(filePath: string): string[] {
  if (!existsSync(filePath)) {
    return [];
  }
  
  const content = readFileSync(filePath, 'utf-8');
  return content.split('\n').filter(line => line.trim().length > 0);
}