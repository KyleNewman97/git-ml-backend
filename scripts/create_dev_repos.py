import os
from pathlib import Path
from uuid import uuid4

import dotenv
from git import Repo


def create_repo(root_dir: Path, repo_name: str, num_commits: int = 100) -> Repo:
    repo_dir = root_dir / repo_name
    repo = Repo.init(repo_dir, mkdir=True)

    # Add some commits
    for _ in range(num_commits):
        file = repo_dir / f"{uuid4()}.txt"
        file.write_text(f"File {file.name}")
        repo.index.add([file.relative_to(repo_dir)])
        repo.index.commit(f"Added {file.name}")


if __name__ == "__main__":
    dotenv.load_dotenv()
    base_dir = Path(os.getenv("BASE_DIR"))

    create_repo(base_dir, "example")
