import random
import string
from datetime import datetime
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Iterator
from uuid import uuid4

import pytest
from git import Actor, Repo


class RepoManager:
    def __init__(self):
        self.temp_dir = TemporaryDirectory()
        self.temp_path = Path(self.temp_dir.name)
        self._name_to_path: dict[str, Path] = {}
        self._name_to_repo: dict[str, Repo] = {}

    def create_repo(self, repo_name: str):
        repo_path = self.temp_path / repo_name
        repo_path.mkdir()
        self._name_to_path[repo_name] = repo_path
        self._name_to_repo[repo_name] = Repo.init(repo_path)

    def add_random_file(
        self, repo_name: str, num_lines: int = 4, line_length: int = 10
    ) -> Path:
        # Create random lines
        lines = [
            "".join(random.choice(string.ascii_letters) for _ in range(line_length))
            for _ in range(num_lines)
        ]

        repo_path = self._name_to_path[repo_name]
        file = repo_path / f"{uuid4()}.txt"
        with open(file, "w") as fp:
            fp.writelines(lines)

        return file

    def commit(
        self, repo_name: str, author: str, msg: str, commit_time: datetime | None = None
    ):
        repo = self._name_to_repo[repo_name]
        repo.index.commit(msg, author=Actor(author, None), author_date=commit_time)

    def get_repo_path(self, repo_name: str) -> Path:
        return self._name_to_path[repo_name]

    def __del__(self):
        self.temp_dir.cleanup()


@pytest.fixture()
def repo_manager() -> Iterator[RepoManager]:
    manager = RepoManager()
    yield manager
    del manager
