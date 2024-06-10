from locust import HttpUser, task, between
import random

class TodoUser(HttpUser):
    wait_time = between(1, 2)
    hott = "http://127.0.0.1:8000"
    
    def on_start(self):
        # Create some initial todos
        for i in range(5):
            self.create_todo()

    def create_todo(self):
        label = f"todo-{random.randint(1, 1000)}"
        self.client.post("/todos", json={"label": label})

    @task
    def get_todos(self):
        self.client.get("/todos")

    @task
    def get_todo(self):
        todo_id = random.randint(1, 5)
        self.client.get(f"/todos/{todo_id}")

    @task
    def update_todo(self):
        todo_id = random.randint(1, 5)
        new_label = f"updated-todo-{random.randint(1, 1000)}"
        self.client.post("/todos", json={"id": todo_id, "label": new_label})

    @task
    def delete_todo(self):
        todo_id = random.randint(1, 5)
        self.client.post(f"/todos/{todo_id}")

# if __name__ == "__main__":
#     import os
#     os.system("locust -f locustfile_2.py")
