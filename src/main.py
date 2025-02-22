from fastapi import FastAPI
from src.routes.repo import RepoRouter

app = FastAPI()

# INCLUDE SUB-ROUTES ###################################################################
app.include_router(RepoRouter)
########################################################################################


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app=app, port="8000")
