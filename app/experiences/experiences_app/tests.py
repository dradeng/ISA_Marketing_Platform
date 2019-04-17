from django.test import TestCase, Client
# from django.core.urlresolvers import reverse
import json


class TestUsers(TestCase):

    def setUp(self):
        pass

    def testUser(self):
        c = Client()
        createResponse = c.post("/api/v1/user/create", {"name": "JohnDoe", "email": "bob@gmail.com", "password": "pwd"})
        self.assertEquals(createResponse.status_code, 201)
        user = json.loads(createResponse.content.decode("utf-8"))
        id = str(user["pk"])

        getResponseValid = c.get("/api/v1/users")
        self.assertEquals(getResponseValid.status_code, 200)
        urlCall = "/api/v1/user/delete?pk="+id
        deleteResponseValid = c.get(urlCall)
        self.assertEquals(deleteResponseValid.status_code, 200)
        deleteResponseInValid = c.post(urlCall)
        self.assertEquals(deleteResponseInValid.status_code, 405)

    def tearDown(self):
        pass



class TestAds(TestCase):

    def setUp(self):
        pass

    def testBook(self):
        c = Client()
        response = c.post("/api/v1/user/create", {"name": "JohnDoe", "email": "hello@gmail.com", "password": "pwd"})
        user = json.loads(response.content.decode("utf-8"))
        id = str(user["id"])

        createResponse = c.post("/api/v1/ad/create", {"url": "google.com", "site_title": "Google", "cost": 5, "duration": 9, "image": "google.com","user":int(id)})
        self.assertEquals(createResponse.status_code, 201)
        urlCall = "/api/v1/ad/delete?pk="+id
        deleteResponseInValid = c.post(urlCall)
        self.assertEquals(deleteResponseInValid.status_code, 405)
        deleteResponseValid = c.get(urlCall)
        self.assertEquals(deleteResponseValid.status_code, 200)

    def tearDown(self):
        pass

class TestAuthentication(TestCase):

    def setUp(self):
        pass

    def testAuthentication(self):
        c = Client()

        response = c.post("/api/v1/user/create", {"name": "Sarah Jane", "email": "sjane@gmail.com", "password": "pass"})

        loginResponse = c.post("/api/v1/login", {"email": "sjane@gmail.com", "password": "pass",})

        self.assertEquals(loginResponse.status_code, 200)
        login_json = json.loads(loginResponse.content.decode("utf-8"))
        newAuth = login_json["authenticator"]

        authenticatorResponse = c.post("/api/v1/check_authenticator", {"authenticator": newAuth})
        self.assertEquals(authenticatorResponse.status_code, 200)

        logoutResponse = c.post("/api/v1/logout", {"authenticator": newAuth})
        self.assertEquals(logoutResponse.status_code, 200)

    def tearDown(self):
        pass

class TestSearch(TestCase):
    
    def setUp(self):
        pass

    def testSearch(self):
        c = Client()
        searchResponse = c.get("/api/v1/search", {"query": "Google"})
        self.assertEquals(searchResponse.status_code, 201)

    def tearDown(self):
        pass