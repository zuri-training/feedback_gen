from django.test import TestCase, Client
from . models import User
# Create your tests here.

def login(self, data):
    self.email = 'dummy' + data + 'gmail.com'
    self.password = 'TeamRhino123'
    user = User.objects.create(email=self.email)
    user.set_password(self.password)
    user.save

    c = Client()
    c.login(email=self.email, password=self.password)
    return c, user

@classmethod
def setUpClass(self):
    self.client_object, self.user = login(self, 'dummy')
    self.content_type = "application/json"

def setUp(self):
    self.response = self.client_object.post('/account/history/', data=json.dumps(self.payload), content_type=self.content_type)
    type(self).check_id = self.response.json()['id']
    self.assertEqual(self.response.status_code, 201)
    