import pytest
from fastapi import HTTPException, status

from tests.conftest import RepoManager
from src.routes.repo.repo_service import RepoService


class TestRepoService:
    def test_get_repo_commits_repo_nonexistent(self, repo_manager: RepoManager):
        """
        Test we get a 404 error if we try to access a repo that doesn't exist.
        """
        repo_name = "test-repo"

        with pytest.raises(HTTPException) as http_error:
            RepoService.get_repo_commits(repo_manager.temp_path, repo_name)
        assert http_error.value.status_code == status.HTTP_404_NOT_FOUND

    def test_get_repo_commits_no_commits(self, repo_manager: RepoManager):
        """
        Test we get an empty list when the repo has no commits.
        """
        repo_name = "test-repo"
        repo_manager.create_repo(repo_name)

        commits = RepoService.get_repo_commits(repo_manager.temp_path, repo_name)
        assert isinstance(commits, list)
        assert len(commits) == 0

    def test_get_repo_commits_with_commits(self, repo_manager: RepoManager):
        """
        Test we correctly get repo commits.
        """
        # Create a repo with one random file that is committed
        repo_name = "test-repo"
        author = "Test Author"
        msg = "Test message"
        repo_manager.create_repo(repo_name)
        repo_manager.add_random_file(repo_name)
        repo_manager.commit(repo_name, author, msg)

        commits = RepoService.get_repo_commits(repo_manager.temp_path, repo_name)
        assert isinstance(commits, list)
        assert len(commits) == 1

        commit = commits[0]
        assert commit.author == author
        assert commit.message == msg
