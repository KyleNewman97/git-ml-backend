from datetime import datetime, timedelta, timezone

import pytest
from git.exc import NoSuchPathError

from git_ml_backend.routes.repo.repo_service import RepoService
from tests.conftest import RepoManager


class TestRepoService:
    def test_get_repo_commits_repo_nonexistent(self, repo_manager: RepoManager):
        """
        Test we get an error when the repo doesn't exist.
        """
        repo_name = "test-repo"

        with pytest.raises(NoSuchPathError):
            RepoService.get_repo_commits(repo_name, 0, 10, repo_manager.temp_path)

    def test_get_repo_commits_no_commits(self, repo_manager: RepoManager):
        """
        Test we get an empty list when the repo has no commits.
        """
        repo_name = "test-repo"
        repo_manager.create_repo(repo_name)

        commits = RepoService.get_repo_commits(repo_name, 0, 10, repo_manager.temp_path)
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
        num_commits = 82
        start_time = datetime.now(timezone.utc)
        for i in range(num_commits):
            repo_manager.add_random_file(repo_name)
            repo_manager.commit(repo_name, author, msg, start_time + timedelta(days=i))

        # Run the query
        page_size = 10
        commits = RepoService.get_repo_commits(
            repo_name, 0, page_size, repo_manager.temp_path
        )

        # Check we get the right number of commits
        assert isinstance(commits, list)
        assert len(commits) == page_size

        # Check commit info is correct
        commit = commits[0]
        assert commit.author == author
        assert commit.message == msg

        # Check the order of the commits is correct
        for idx in range(len(commits) - 1):
            assert commits[idx + 1].date_time < commits[idx].date_time

    def test_get_repo_commits_above_page_limit(self, repo_manager: RepoManager):
        """
        Test that we get an index error when trying to access a page above the limits.
        """
        # Create a repo with one random file that is committed
        repo_name = "test-repo"
        author = "Test Author"
        msg = "Test message"
        repo_manager.create_repo(repo_name)
        repo_manager.add_random_file(repo_name)
        repo_manager.commit(repo_name, author, msg)

        with pytest.raises(IndexError):
            RepoService.get_repo_commits(repo_name, 1, 1, repo_manager.temp_path)

    def test_get_repo_commits_below_page_limit(self, repo_manager: RepoManager):
        """
        Test that we get an index error when trying to access a page below the limits.
        """
        # Create a repo with one random file that is committed
        repo_name = "test-repo"
        author = "Test Author"
        msg = "Test message"
        repo_manager.create_repo(repo_name)
        repo_manager.add_random_file(repo_name)
        repo_manager.commit(repo_name, author, msg)

        with pytest.raises(IndexError):
            RepoService.get_repo_commits(repo_name, -1, 10, repo_manager.temp_path)

    def test_get_repo_commit_count_repo_nonexistent(self, repo_manager: RepoManager):
        """
        Test we get an error when the repo doesn't exist.
        """
        repo_name = "test-repo"

        with pytest.raises(NoSuchPathError):
            RepoService.get_repo_commit_count(repo_name, repo_manager.temp_path)

    def test_get_repo_commit_count(self, repo_manager: RepoManager):
        """
        Test that we can get the number of commits correctly.
        """
        # Create a repo with one random file that is committed
        repo_name = "test-repo"
        author = "Test Author"
        msg = "Test message"
        repo_manager.create_repo(repo_name)

        num_commits = 84
        for _ in range(num_commits):
            repo_manager.add_random_file(repo_name)
            repo_manager.commit(repo_name, author, msg)

        count = RepoService.get_repo_commit_count(repo_name, repo_manager.temp_path)
        assert count == num_commits
