import datetime
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from ...models.zipline_app.zipline_app import ZlModel
from .other import create_asset, create_order, create_account, a1

class OrderViewsTests(TestCase):
    def setUp(self):
      ZlModel.clear()
      self.acc1 = create_account(symbol="TEST01")
      self.a1a = create_asset(a1["symbol"],a1["exchange"],a1["name"])
 
    def test_list(self):
        url = reverse('zipline_app:orders-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_new_get(self):
        url = reverse('zipline_app:orders-new')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        o1 = create_order(order_text="test?",days=-1, asset=self.a1a, amount=10, account=self.acc1)

        url = reverse('zipline_app:orders-delete', args=(self.a1a.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_new_post(self):
        # http://stackoverflow.com/questions/40005411/django-django-test-client-post-request
        time = '2015-01-01 00:00:00' #timezone.now() + datetime.timedelta(days=-0.5)

        url = reverse('zipline_app:orders-new')
        response = self.client.post(url,{'pub_date':time,'asset':self.a1a.id,'amount':10,'account':self.acc1.id})
        self.assertEqual(response.status_code, 302)
#        print(response.context)
#        self.assertFormError(response, 'form', 'pub_date', 'Enter a valid date/time.')
        #self.assertFormError(response, 'form', 'asset', 'Enter a valid date/time.')
        #self.assertFormError(response, 'form', 'amount', 'Enter a valid date/time.')
        #self.assertFormError(response, 'form', 'account', 'Select a valid choice. That choice is not one of the available choices.')

