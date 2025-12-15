// file-tasks.ts - File I/O operations

// Check if file exists
async function fileExists(filePath: string): Promise<boolean> {
  try {
    await Deno.stat(filePath);
    return true;
  } catch {
    return false;
  }
}

// Search for a word in CSV file and write results
export async function searchCsvFile(filePath: string, searchWord: string): Promise<void> {
  // Check if file exists
  if (!(await fileExists(filePath))) {
    const message = `CSV file not found: ${filePath}\nSkipping CSV search.`;
    console.log(`  ⚠️  ${message}`);
    await Deno.writeTextFile('search_results.txt', message);
    return;
  }
  
  // Read the entire CSV file
  const content = await Deno.readTextFile(filePath);
  
  // Count occurrences of the search word (case-insensitive)
  const regex = new RegExp(searchWord, 'gi');
  const matches = content.match(regex);
  const count = matches ? matches.length : 0;
  
  // Prepare result message
  const resultMessage = count > 0 
    ? `Found ${count} matches for "${searchWord}"`
    : `No matches found for "${searchWord}"`;
  
  // Write results to file
  await Deno.writeTextFile('search_results.txt', resultMessage);
  
  console.log(`  ✓ ${resultMessage}`);
}

// Additional file utility: Read lines from CSV
export async function readCsvLines(filePath: string): Promise<string[]> {
  if (!(await fileExists(filePath))) {
    return [];
  }
  
  const content = await Deno.readTextFile(filePath);
  return content.split('\n').filter(line => line.trim().length > 0);
}