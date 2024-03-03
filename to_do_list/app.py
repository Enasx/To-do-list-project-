from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json


app = FastAPI()


class Task(BaseModel):
    task_id: int
    task: str


def get_list():
    with open("list_module.json", "r") as file:
       list_data = json.load(file)
    return [Task(**task_data) for task_data in list_data]

def write_tasks(list):
    list_data = [{"task_id": task.task_id, "task": task.task} for task in list] 
    with open("list_module.json", "w") as file:
        json.dump(list_data, file)

@app.get("/list/")
async def read_list():
    return get_list()

@app.post("/add/")
async def add_task(new_task: str):
    list = get_list()
    if len(list) == 0:
        new_task_id=1
    else:
        new_task_id = max(task.task_id for task in list) + 1
    task_model = Task(task_id=new_task_id, task=new_task)
    list.append(task_model)
    write_tasks(list)
    return task_model


""" @app.post("/complete/")
async def complete_task(task_id: int):
    list=get_list()
    if task_id < 0 or task_id >= len(list): #make it a search func
        raise HTTPException(status_code=404, detail="Task not found")
    completed_task = list.pop(task_id)
    write_tasks(list)
    return completed_task """


@app.post("/complete/")
async def complete_task(task_idd: int):
    list=get_list()
    for index, task in enumerate(list):
        if task.task_id == task_idd:
        #if task.task_id == task_idd:
            completed_task = list.pop(index)
            write_tasks(list)
            return completed_task
    
    raise HTTPException(status_code=404, detail="Task not found")


@app.get("/delete/")
async def delete_list():
    global list
    list = []
    write_tasks(list)
    return list






