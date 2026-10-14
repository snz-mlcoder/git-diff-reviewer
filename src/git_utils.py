import subprocess
def get_diff(repo_path:str,base: str, target: str)->str:
    result = subprocess.run(
        ["git", "diff", base, target],
        cwd=repo_path,
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        raise Exception(f"Git diff command failed with error: {result.stderr}")

    return result.stdout
