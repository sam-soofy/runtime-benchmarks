"""
types_def.py - Shared type definitions
"""

from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class BenchmarkResult:
    """Stores timing results for each benchmark phase"""

    phase: str
    duration_ms: float


@dataclass
class User:
    """User data structure for JSON operations"""

    id: int
    name: str
    email: str
    active: bool
    metadata: Dict[str, Any]
