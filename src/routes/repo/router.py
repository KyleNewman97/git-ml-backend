from fastapi import APIRouter

router = APIRouter()


@router.get("/{repo_name}/commits")
async def get_repo_commits(rep_name: str):
    pass
