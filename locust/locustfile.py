from locust import HttpUser, task, between

class WebsiteTestUser(HttpUser):
    wait_time = between(0.5, 3.0)

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        pass

    @task(1)
    def hello_world(self):
        self.client.get("https://bookish-telegram-jp4v5qwqrjr2qjxp-8000.app.github.dev/")
    
    @task(2)
    def nocodb(self):
        self.client.get("https://bookish-telegram-jp4v5qwqrjr2qjxp-8000.app.github.dev/nocodb-data/")

    @task(5)
    def admin(self):
        self.client.post("https://bookish-telegram-jp4v5qwqrjr2qjxp-8000.app.github.dev/admin/login/?next=/admin/", {"username": "admin", "password": "123123"})

    @task(3)
    def virtuals(self):
        self.client.get("https://bookish-telegram-jp4v5qwqrjr2qjxp-8000.app.github.dev/polls/students/")

    @task(4)
    def polls(self):
        self.client.get("https://bookish-telegram-jp4v5qwqrjr2qjxp-8000.app.github.dev/polls/")
    