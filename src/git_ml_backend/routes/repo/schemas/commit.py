from pydantic import BaseModel

from git_ml_backend.types import DateTime


class Commit(BaseModel):
    author: str
    date_time: DateTime
    hash: str
    message: str
