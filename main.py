from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}

# @app.get("/courses/{course_name}")
# def read_course(course_name):
#     return {"course_name": course_name}

@app.get("/courses/{course_id}")
def read_course(course_id: int):
    return {"course_id": course_id}