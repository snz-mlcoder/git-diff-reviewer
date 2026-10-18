import argparse 
import sys
from src.git_utils import get_diff
from src.reviewer import review_diff
from src.scoring import get_highest_severity
from src.report import generate_diff_review_report, save_report

def main():
    parser = argparse.ArgumentParser(description="Review git diffs between two branches/commits and generate a report."
                                     )
    parser.add_argument("--repo", default=".", help="Path to the git repository ")
    parser.add_argument("--base", required=True, help="Base branch/commit ")
    parser.add_argument("--target", required=True, help="Target branch/commit")

    args = parser.parse_args()
    try:
        diff_text = get_diff(args.repo, args.base, args.target)
        review_result = review_diff(diff_text=diff_text)

    except Exception as e:
        print(f"Error occurred while fetching diff: {e}")
        sys.exit(2)
        
    report = generate_diff_review_report(result=review_result)
    print(report)

    save_report(report=report, filepath="review_report.md")

    highest = get_highest_severity(result=review_result)
    if highest in ("high", "critical"):             
        sys.exit(1)  # Exit with a non-zero status code for high or critical severity
    else:
        sys.exit(0)  # Exit with a zero status code for low or medium severity

if __name__ == "__main__":
    main()
