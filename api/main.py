from fastapi import FastAPI
from api.routers import school, branch, student, sample


app = FastAPI()

app.include_router(
    school.router
)

app.include_router(
    branch.router
)

app.include_router(
    student.router
)

app.include_router(
    sample.router
)


# @app.get("/")
# def get_index():
#     return "This is index"
