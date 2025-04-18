from datetime import datetime
from typing import Annotated

from pydantic import BeforeValidator


def validate_datetime(date_time: str | datetime) -> datetime:
    if isinstance(date_time, str):
        return datetime.fromisoformat(date_time)

    if isinstance(date_time, datetime):
        return date_time

    msg = f"Got {type(date_time)} type, but only accept datetime or str."
    raise ValueError(msg)


DateTime = Annotated[datetime, BeforeValidator(validate_datetime)]
