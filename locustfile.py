from locust import HttpUser, task, between

class APIUser(HttpUser):
    wait_time = between(1, 2)


    @task
    def get_all_posts(self):
        self.client.get("/posts")

    @task
    def create_post(self):
        payload = {"title": "Stress Test", "completed": False}
        self.client.post("/posts", json=payload)

    @task
    def get_invalid_post(self):
        self.client.get("/posts/invalid_id")