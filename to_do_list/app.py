from fastapi import FastAPI, HTTPException
from db_interface import DBInterface

app = FastAPI()
db_interface = DBInterface()


def get_list():
    list_data = db_interface.get_all_tasks()
    return list_data


@app.get("/list/")
async def read_list():
    return get_list()


@app.post("/add/")
async def add_task(new_task: str):
    db_interface.create_task(new_task)
    return new_task


@app.post("/complete/")
async def complete_task(task_id: int):
    task = db_interface.delete_task(task_id)
    if task is not None:
        return f"Task {task_id} deleted successfully!"
    else:
        raise HTTPException(status_code=404, detail="Task not found")


@app.get("/delete/")
async def delete_list():
    db_interface.delete_all_tasks()
    return get_list()


# @app.on_event("startup")
# async def startup_event():
#     db_interface.initialize_database()
