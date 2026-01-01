from dataclasses import dataclass
from typing import Optional


@dataclass
class OutputDTO:
    success: bool
    error: Optional[str] = None
