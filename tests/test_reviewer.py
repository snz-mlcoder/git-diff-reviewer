from unittest.mock import patch, MagicMock
from src.schema import ReviewIssue, ReviewResult
from src.reviewer import review_diff

def test_review_diff_returns_structured_result():
    fake_result = ReviewResult(
        issues=[
            ReviewIssue(file="test.py", severity="high", description="fake issue", category="bug"),
        ],
        summary="Fake summary"
    )

    with patch('src.reviewer.ChatOpenAI') as mock_chat_openai:
        mock_llm = MagicMock()
        mock_llm.with_structured_output.return_value.invoke.return_value = fake_result
        mock_chat_openai.return_value = mock_llm

        result = review_diff("fake diff text")

    assert result == fake_result