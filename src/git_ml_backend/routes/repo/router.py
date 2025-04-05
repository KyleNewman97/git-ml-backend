from fastapi import APIRouter, HTTPException, status
from git.exc import NoSuchPathError

from git_ml_backend.routes.repo.schemas import Commit
from git_ml_backend.routes.repo.repo_service import RepoService

router = APIRouter()


@router.get("/{repo_name}/commits")
async def get_repo_commits(
    repo_name: str, page_index: int, page_size: int
) -> list[Commit]:
    try:
        return RepoService.get_repo_commits(repo_name, page_index, page_size)
    except NoSuchPathError as err:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Repo doesn't exist.") from err
    except IndexError as err:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Page outside bounds.") from err


@router.get("/{repo_name}/commits/count")
async def get_repo_commit_count(repo_name: str) -> int:
    try:
        return RepoService.get_repo_commit_count(repo_name)
    except NoSuchPathError as err:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Repo doesn't exist.") from err
