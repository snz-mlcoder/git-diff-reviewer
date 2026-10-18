from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

from dotenv import load_dotenv
from src.schema import ReviewResult

load_dotenv()

SYSTEM_PROMPT = """You are an expert code reviewer. Analyze the given git diff and identify issues:
bugs, security risks, performance problems, style violations, and missing documentation.
Only report issues visible in the diff itself."""

def review_diff(diff_text: str) -> ReviewResult:
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    structured_llm = llm.with_structured_output(ReviewResult)
    messages=[
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=diff_text)
    ]
    return structured_llm.invoke(messages)
    