from git_ml_backend.types import DateTime
from pydantic import BaseModel


class Commit(BaseModel):
    author: str
    date_time: DateTime
    hash: str
    message: str
