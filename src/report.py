# Code Review Report
from src.schema import ReviewResult


def generate_diff_review_report(result: ReviewResult) -> str:
    report = f"Summary:\n{result.summary}\n\n"
    if not result.issues:
        report += "No issues found."
    else:
        report += "Identified Issues:\n"
        for issue in result.issues:
            report += f"- Severity: {issue.severity},Description: {issue.description},File: {issue.file},Category: {issue.category}\n"
    return report

def save_report(report: str, filepath: str) -> None:
    with open(filepath, 'w') as f:
        f.write(report) 