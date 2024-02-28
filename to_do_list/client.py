import requests



operation="add"
new_task_data = {"task_id": 7, "task": "Reading"}
complete_task_data = {"task_id": 2}


if operation == "list" :
    response=requests.get("http://localhost:8000/list")
    

elif operation == "add" :
    response = requests.post("http://localhost:8000/add/", json=new_task_data)
      
elif operation == "complete":
    response = requests.post("http://localhost:8000/complete/", params=complete_task_data)
    
elif operation == "delete":
    response = requests.get("http://localhost:8000/delete/")

else:
    print("Invalid operation. Please select from these operations: list, add, complete, delete")
    response=None



if response :
    if response.status_code==200 :
        print(response.json()) 
    else:
        print(response.text)
    

