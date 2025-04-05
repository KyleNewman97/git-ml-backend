import os
from pathlib import Path

import dotenv
from pydantic import BaseModel


class Env(BaseModel):
    base_dir: Path


dotenv.load_dotenv()
ENV = Env(base_dir=os.getenv("BASE_DIR"))
