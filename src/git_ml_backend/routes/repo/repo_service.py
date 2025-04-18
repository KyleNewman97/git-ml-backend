from pathlib import Path

from git import Repo
from pydriller import Repository

from git_ml_backend.env import ENV
from git_ml_backend.routes.repo.schemas import Commit


class RepoService:
    @staticmethod
    def get_repo_commits(
        repo_name: str, page_index: int, page_size: int, base_dir: Path = ENV.base_dir
    ) -> list[Commit]:
        """
        Get a list of all repo commit messages.

        Parameters
        ----------
        repo_name:
            The name of the repo to get commit messages for.

        page_index:
            Used for paginated requests. Indicates the index of the sub-page to get.

        page_size:
            Used for paginated requests. Indicates the size of the pages to get.

        Returns
        -------
        commits:
            A list of commits containing information about each commit.

        Raises
        ------
        NoSuchPathError:
            Raised when the git repo cannot be found.

        IndexError:
            Raised when the requested page is outside the bounds of commits.
        """
        if page_index < 0:
            raise IndexError("Accessing page below limit.")

        repo_path = base_dir / repo_name
        repo = Repository(repo_path.as_posix(), order="reverse")

        start_index = page_index * page_size
        end_index = start_index + page_size

        commits: list[Commit] = []
        for idx, commit in enumerate(repo.traverse_commits()):
            # Skip irrelevant commits
            if idx < start_index:
                continue
            if end_index <= idx:
                break

            commits.append(
                Commit(
                    author=commit.author.name,
                    date_time=commit.author_date,
                    hash=commit.hash,
                    message=commit.msg,
                )
            )

        # Find the commits to return
        if start_index != 0 and idx <= start_index:
            raise IndexError("Accessing page above limit.")

        return commits

    @staticmethod
    def get_repo_commit_count(repo_name: str, base_dir: Path = ENV.base_dir) -> int:
        """
        Finds the number of commits in the primary branch of the repo.

        Parameters
        ----------
        repo_name:
            The name of the repo.

        Returns
        -------
        num_commits:
            The number of commits on the repo.
        """
        repo_path = base_dir / repo_name
        repo = Repo(repo_path.as_posix())

        return int(repo.git.rev_list("--count", "HEAD"))
