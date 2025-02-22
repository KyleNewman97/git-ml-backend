from pydriller import Repository


class RepoService:
    @staticmethod
    def get_repo_commits(repo_name: str):
        repo = Repository(repo_name)

        commits: list = []
        for commit in repo.traverse_commits():
            commits.append((commit.author, commit.msg, commit.hash, commit.author_date))
        pass
