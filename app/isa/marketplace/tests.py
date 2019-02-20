from django.test import TestCase, Client
from django.urls import reverse
from myapp.models import Ad, User


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="testuser1", name="Test User", email="test@email.com", password="password")
        User.objects.create(username="testuser2", name="Other User", email="email@email.com", password="drowssap")

    def test_users_stored_correctly(self):
        user1 = User.objects.get(username="testuser1")
        user2 = User.objects.get(name="Other User")
        self.assertEqual(user1.id, '1')
        self.assertEqual(user1.email, 'test@email.com')
        self.assertEqual(user2.username, 'testuser2')

class AdTestCase(TestCase):
    def setUp(self):
        Ad.objects.create(image="url_of_some_sort", duration="200", user=User.objects.get(pk=1), cost="10", url="google.com", site_title="Google")
        Ad.objects.create(image="youtube image", duration="100", user=User.objects.get(pk=1), cost="20", url="youtube.com", site_title="YouTube")

    def test_ads_stored_correctly(self):
        google = Ad.objects.get(duration="200")
        youtube = Ad.objects.get(site_title="YouTube")
        self.assertEqual(google.id, '1')
        self.assertEqual(youtube.image, 'youtube image')
        self.assertEqual(youtube.duration, '100')


# class GetOrderDetailsTestCase(TestCase):
#     #setUp method is called before each test in this class
#     def setUp(self):
#         pass #nothing to set up

#     def success_response(self):
#         #assumes user with id 1 is stored in db
#         response = self.client.get()

#         #checks that response contains parameter order list & implicitly
#         # checks that the HTTP status code is 200
#         self.assertContains(response, 'order_list')

#     #user_id not given in url, so error
#     def fails_invalid(self):
#         response = self.client.get(reverse('all_orders_list'))
#         self.assertEquals(response.status_code, 404)

#     #tearDown method is called after each test
#     def tearDown(self):
#         pass #nothing to tear down