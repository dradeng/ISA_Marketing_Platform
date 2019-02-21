from django.test import TestCase, Client
from django.urls import reverse
from marketplace.models import Ad, User
import json


# class UserTestCase(TestCase):
#     def setUp(self):
#         User.objects.create(username="testuser1", first_name="Test", last_name="User", email="test@email.com", password="password")
#         User.objects.create(username="testuser2", first_name="Other", last_name="User", email="email@email.com", password="drowssap")

#     def test_users_stored_correctly(self):
#         user1 = User.objects.get(username="testuser1")
#         user2 = User.objects.get(first_name="Other")
#         self.assertEqual(user1.first_name, "Test")
#         self.assertEqual(user1.email, 'test@email.com')
#         self.assertEqual(user2.username, 'testuser2')

# class AdTestCase(TestCase):
#     def setUp(self):
#         User.objects.create(username="testuser1", first_name="Test", last_name="User", email="test@email.com", password="password")
#         Ad.objects.create(image="url_of_some_sort", duration=200, user=User.objects.get(username="testuser1"), cost=10, url="google.com", site_title="Google")
#         Ad.objects.create(image="youtube image", duration=100, user=User.objects.get(id=1), cost=20, url="youtube.com", site_title="YouTube")

#     def test_ads_stored_correctly(self):
#         google = Ad.objects.get(duration=200)
#         youtube = Ad.objects.get(site_title="YouTube")
#         self.assertEqual(google.url, "google.com")
#         self.assertEqual(youtube.image, 'youtube image')
#         self.assertEqual(youtube.duration, 100)


class TestUsers(TestCase):

    def setUp(self):
        pass

    def testUser(self):
        c = Client()
        createResponse = c.post("/api/v1/users/create", {"first_name": "John", "last_name": "Doe", "email": "hello@gmail.com", "password": "pwd", "username": "JDoe"})
        self.assertEquals(createResponse.status_code, 201)
        user = json.loads(createResponse.content.decode("utf-8"))
        id = str(user["id"])

        getResponseValid = c.get("/api/v1/users?username=JDoe")
        self.assertEquals(getResponseValid.status_code, 200)

        getResponseValid = c.get("/api/v1/users?username=JDoe")
        self.assertEquals(getResponseValid.status_code, 200)
        updateResponse = c.post("/api/v1/users/"+id+"/update", {"email": "newemail@yahoo.com"})
        self.assertEquals(updateResponse.status_code, 200)
        deleteResponseValid = c.get("/api/v1/users/"+id+"/delete")
        self.assertEquals(deleteResponseValid.status_code, 200)
        deleteResponseInValid = c.post("/api/v1/users/3/delete")
        self.assertEquals(deleteResponseInValid.status_code, 405)

    def tearDown(self):
        pass

