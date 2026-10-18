# Project Overview
A CLI tool that reviews the git diff between two branches or commits using an LLM with structured output, and reports issues by severity — designed to run in CI pipelines.

# Features
categorize errors in low mwdium high critical 
give us report using openai api
error handeling 

# Installation
using uv instalation
uv sync

# Usage
uv run main.py --base main --target feature-branch

# Technologies
uv 
python 
dotenv
langchain
langchain-openai
pydantic
Pytest

# Project Structure
git-diff-reviewer/
├── main.py
├── src/
│   ├── git_utils.py
│   ├── schema.py
│   ├── reviewer.py
│   ├── scoring.py
│   └── report.py
├── tests/
│   ├── test_scoring.py
│   ├── test_report.py
│   └── test_reviewer.py
├── pyproject.toml
└── README.md

# Known Limitations
This tool only analyzes the lines visible in the git diff, not the full codebase context.
As a result, it cannot detect issues that depend on code outside the diff — for example,
a function signature that changed but is still called incorrectly elsewhere, or a missing
import that only becomes a problem when combined with unchanged code. This mirrors the same
scope limitation found in tools like GitHub Copilot PR Review and CodeRabbit.

# Tests
uv run pytest

# Future Improvements
- Support LLM providers other than OpenAI
- Analyze multiple files with broader cross-file context
- Direct integration with GitHub Actions (e.g., auto-comment on PRs)