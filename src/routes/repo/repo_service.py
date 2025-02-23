from pydriller import Repository
from src.routes.repo.schemas import Commit


class RepoService:
    @staticmethod
    def get_repo_commits(repo_name: str) -> list[Commit]:
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
        repo = Repository(repo_name)

        commits: list[Commit] = []
        for commit in repo.traverse_commits():
            commits.append(
                Commit(
                    author=commit.author,
                    date_time=commit.author_date,
                    hash=commit.hash,
                    message=commit.msg,
                )
            )
        return commits
