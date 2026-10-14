from src.schema import ReviewResult 

def severity_score(severity: str) -> int:
  
    severity_mapping = {
        'low': 1,
        'medium': 2,
        'high': 3,
        'critical': 4
    }
    
    return severity_mapping[severity]

def get_highest_severity(result: ReviewResult) -> str:
    if not result.issues:
        return 'low'  # No issues found, return 'low' severity

    highest_severity = max(result.issues, key=lambda issue: severity_score(issue.severity))

    return highest_severity.severity
