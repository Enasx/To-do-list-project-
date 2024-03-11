import requests

base_url = "http://localhost:8000"


def get_input():
    print("Choose an operationn: list, add, complete, delete or exit.")
    operation = input("Operation: ")

    if operation == "add":
        new_task = input("Enter the new task: ")
        data = {"new_task": new_task}
    elif operation == "complete":
        task_id = input("Enter the task ID to complete: ")
        data = {"task_id": int(task_id)}
    else:
        data = {}

    return operation, data


while True:
    operation, data = get_input()

    if operation.lower() == "exit":
        break
    if operation in ["list", "delete"]:
        response = requests.get(f"{base_url}/{operation}/")
    elif operation in ["add", "complete"]:
        response = requests.post(f"{base_url}/{operation}/", params=data)
    else:
        print("Invalid operation. Please select from these operations: list, add, complete, delete or exit.")
        continue

    if response.status_code == 200:
        print(response.json())
    else:
        print(response.text)
