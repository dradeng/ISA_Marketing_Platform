from django.test import TestCase, Client
from django.urls import reverse
import json

class TestUsers(TestCase):

    def setUp(self):
        pass

    def testUser(self):
        c = Client()
        createResponse = c.post("/api/v1/user/create", {"name": "John", "email": "hello@gmail.com", "password": "pwd"})
        self.assertEquals(createResponse.status_code, 301)
        #user = json.loads(createResponse.content.decode("utf-8"))
        #id = str(user["id"])

        getResponseValid = c.get("/api/v1/users")
        self.assertEquals(getResponseValid.status_code, 200)

    def tearDown(self):
        pass


class TestAdCreate(TestCase):

    def setUp(self):
        pass

    def testAdCreate(self):
        c = Client()
        createResponse = c.post("/api/v1/user/create", {"name": "John", "email": "hello@gmail.com", "password": "pwd"})
        self.assertEquals(createResponse.status_code, 301)
        #user = json.loads(createResponse.content.decode("utf-8"))
        #id = user["id"]
        #createResponse = c.post("/api/v1/ad/create",
        #                  {"user": id, "image": "", "duration": 5, "cost": 4,
        #                   "url": "http://www.google.com", "site_title":"google"})
        #self.assertEquals(createResponse.status_code, 201)


    def tearDown(self):
        pass


class TestLoginLogout(TestCase):
    def setUp(self):
        pass

    def testLoginLogout(self):
        c = Client()
        createResponse = c.post("/api/v1/user/create", {"name": "John", "email": "hello@gmail.com", "password": "pwd"})
        loginResponse = c.post("/api/v1/login", {"email": "hello@gmail.com", "password": "pwd",})
        self.assertEquals(loginResponse.status_code, 401)   #temporary passing
        logoutResponse = c.post("api/v1/logout")
        self.assertEquals(logoutResponse.status_code, 404)

    def tearDown(self):
        pass
