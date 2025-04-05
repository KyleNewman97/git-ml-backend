from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from git_ml_backend.routes.repo import RepoRouter

app = FastAPI()

# INCLUDE SUB-ROUTES ###################################################################
app.include_router(RepoRouter)
########################################################################################

# CORS #################################################################################
origins = ["http://localhost:4000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
########################################################################################


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app=app, port="8000")
