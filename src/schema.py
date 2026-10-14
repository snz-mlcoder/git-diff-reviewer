from pydantic import BaseModel
from typing import Literal

class ReviewIssue(BaseModel):
    file: str
    severity: Literal["low", "medium", "high", "critical"]
    category: Literal["bug", "security", "performance", "style", "documentation"]
    description: str

class ReviewResult(BaseModel):
    issues: list[ReviewIssue]
    summary: str