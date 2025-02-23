from fastapi import APIRouter
from routes.repo.schemas import Commit
from src.routes.repo.repo_service import RepoService

router = APIRouter()


@router.get("/{repo_name}/commits")
async def get_repo_commits(repo_name: str) -> list[Commit]:
    return RepoService.get_repo_commits(repo_name)
