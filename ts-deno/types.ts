// types.ts - Shared type definitions

export interface BenchmarkResult {
  phase: string;
  durationMs: number;
}

export interface User {
  id: number;
  name: string;
  email: string;
  active: boolean;
  metadata: {
    created: string;
    score: number;
  };
}