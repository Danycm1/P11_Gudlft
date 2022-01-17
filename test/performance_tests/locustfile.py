from locust import HttpUser, task


class ProjectPerfTest(HttpUser):

    @task
    def show_summary(self):
        self.client.post("/showSummary", {"email": "john@simplylift.co"})

    @task
    def display_points(self):
        self.client.get("/displayPoints")

    @task
    def purchase_places(self):
        self.client.post("/purchasePlaces", {'club': 'Simply Lift', 'competition': "Openclassrooms", 'places': 5})

    @task
    def logout(self):
        self.client.get("/logout")
