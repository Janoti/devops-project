from locust import HttpUser, between, task


class LoadTester(HttpUser):
    wait_time = between(5, 15)

    @task
    def list(self):
        self.client.get("/users")

    @task
    def search(self):
        self.client.get("/users/11111111111")

    @task
    def create(self):
        self.client.post("/users", json={"nome":"bacon", "cpf": "999999999999", "sobrenome": "pig", "email": "porco@pigo.com", "data_nasc":"10/10/10"})
