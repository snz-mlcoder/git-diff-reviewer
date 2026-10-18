from src.scoring import get_highest_severity,severity_score
from src.schema import ReviewResult, ReviewIssue

def test_severity_score_critical():
    assert severity_score("critical") == 4

def test_severity_score_high():
    assert severity_score("high") == 3

def test_severity_score_medium():
    assert severity_score("medium") == 2

def test_severity_score_low():
    assert severity_score("low") == 1


def test_get_highest_severity():
    result = ReviewResult(
        issues=[
            ReviewIssue(file="a.py", severity="low", description="Low severity issue", category="style"),
            ReviewIssue(file="b.py", severity="critical", description="Critical severity issue", category="security"),
        ],
        summary="Test summary"
    )
    assert get_highest_severity(result) == "critical"