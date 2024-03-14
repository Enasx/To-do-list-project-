import requests

base_url = "http://localhost:8000"


# function asks the user to choose an operation
def get_input():
    print("Choose an operationn: list, add, complete, delete or exit.")
    operation = input("Operation: ")

    # Based on the chosen operation, collect relevant data
    if operation == "add":
        new_task = input("Enter the new task: ")
        data = {"new_task": new_task}
    elif operation == "complete":
        task_id = input("Enter the task ID to complete: ")
        data = {"task_id": int(task_id)}
    else:
        # For other operations (list, delete, exit), no additional data needed
        data = {}

    return operation, data


# While loop for infinite interactive session until user chose exit
while True:
    operation, data = get_input()

    if operation.lower() == "exit":
        break
    # Make requests based on the chosen operation
    if operation in ["list", "delete"]:
        response = requests.get(f"{base_url}/{operation}/")
    elif operation in ["add", "complete"]:
        response = requests.post(f"{base_url}/{operation}/", params=data)
    else:
        # Handle invalid operation
        print("Invalid operation. Please select from these operations: list, add, complete, delete or exit.")
        continue    # Continue to the next iteration of the loop

    # Process the server response
    if response.status_code == 200:
        print(response.json())
    else:
        # Print an error message if the server returns an unexpected response
        print(response.text)
