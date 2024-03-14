import requests
import sys

base_url = "http://localhost:8000"


if len(sys.argv) > 1:
    operation = sys.argv[1]
    data = {}
    if operation == "add":
        if len(sys.argv) < 3:
            raise Exception("Please provide a task to add.")
            # Concatenate all arguments starting from index 2
        else:
            new_task = ' '.join(sys.argv[2:])
            data = {"new_task": new_task}
    elif operation == "complete":
        if len(sys.argv) < 3:
            raise Exception("Please provide task id to complete.")
            # Concatenate all arguments starting from index 2
        else:
            task_id = sys.argv[2]
            data = {"task_id": int(task_id)}
else:
    # Handle invalid operation
    raise Exception("Invalid operation. Please select from these operations: list, add, complete or delete.")

# Make requests based on the chosen operation
if operation in ["list", "delete"]:
    response = requests.get(f"{base_url}/{operation}/")
elif operation in ["add", "complete"]:
    response = requests.post(f"{base_url}/{operation}/", params=data)

# Process the server response
if response.status_code == 200:
    print(response.json())
else:
    # Print an error message if the server returns an unexpected response
    print(response.text)
