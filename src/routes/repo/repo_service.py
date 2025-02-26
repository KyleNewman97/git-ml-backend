from pathlib import Path

from pydriller import Repository
from git.exc import NoSuchPathError
from fastapi import HTTPException, status

from src.routes.repo.schemas import Commit


class RepoService:
    @staticmethod
    def get_repo_commits(base_dir: Path, repo_name: str) -> list[Commit]:
        """
        Get a list of all repo commit messages.

        Parameters
        ----------
        repo_name:
            The name of the repo to get commit messages for.

        Returns
        -------
        commits:
            A list of commits containing information about each commit.
        """
        repo_path = base_dir / repo_name
        repo = Repository(repo_path.as_posix())

        commits: list[Commit] = []
        try:
            for commit in repo.traverse_commits():
                commits.append(
                    Commit(
                        author=commit.author.name,
                        date_time=commit.author_date,
                        hash=commit.hash,
                        message=commit.msg,
                    )
                )
        except NoSuchPathError as err:
            msg = "Repo doesn't exist."
            raise HTTPException(status.HTTP_404_NOT_FOUND, msg)

        return commits
