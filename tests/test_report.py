from src.report import generate_diff_review_report, save_report
from src.schema import ReviewIssue, ReviewResult

def test_generate_report_includes_issue_details():
    result = ReviewResult(
        issues=[
            ReviewIssue(file="a.py", severity="low", description="Low severity issue", category="style"),
            ReviewIssue(file="b.py", severity="critical", description="Critical severity issue", category="security"),
            ],
        summary="Test summary"
    )
    report = generate_diff_review_report(result)
    assert "a.py" in report
    assert "b.py" in report
    assert "Summary:\nTest summary" in report
    assert "- Severity: low,Description: Low severity issue,File: a.py,Category: style" in report
    assert "- Severity: critical,Description: Critical severity issue,File: b.py,Category: security" in report