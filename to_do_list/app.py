# Import necessary modules and classes
from fastapi import FastAPI, HTTPException
from db_interface import DBInterface

# Create a FastAPI app instance and a DBInterface instance
app = FastAPI()
db_interface = DBInterface()


# Helper function to retrieve the list of tasks from the database
def get_list():
    list_data = db_interface.get_all_tasks()
    return list_data


# Endpoint to retrieve the list of tasks
@app.get("/list/")
async def read_list():
    return get_list()


# Endpoint to add a new task
@app.post("/add/")
async def add_task(new_task: str):
    db_interface.create_task(new_task)
    return new_task


# Endpoint to complete a task by deleting it
@app.post("/complete/")
async def complete_task(task_id: int):
    print(task_id, type(task_id))
    task = db_interface.delete_task(task_id)
    if task is not None:  # If statment to handle wrong entry of task_id
        return f"Task {task_id} deleted successfully!"
    else:
        raise HTTPException(status_code=404, detail="Task not found")


# Endpoint to delete all tasks
@app.get("/delete/")
async def delete_list():
    db_interface.delete_all_tasks()
    return get_list()

# @app.on_event("startup")
# async def startup_event():
#     db_interface.initialize_database()
