from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()



class Task(BaseModel):
    task_id: int
    task: str

list = [
    Task(task_id=1, task="Having Breakfast"),
    Task(task_id=2, task="Going to work"),
    Task(task_id=3, task="Gym"),
    Task(task_id=4, task="Buying Groceries"),
    Task(task_id=5, task="Cooking"),
    Task(task_id=6, task="Sleeping")
]

@app.get("/list/")
async def read_list():
    return list


@app.post("/add/")
async def add_task(new_task: Task):
    new_task_id = len(list) + 1
    new_task.task_id = new_task_id   
    list.append(new_task)
    return new_task

@app.post("/complete/")
async def complete_task(task_id: int):
    if task_id < 0 or task_id >= len(list):
        raise HTTPException(status_code=404, detail="Task not found")
    completed_task = list.pop(task_id)
    return completed_task


@app.get("/delete/")
async def delete_list():
    global list
    list = []
    return list






