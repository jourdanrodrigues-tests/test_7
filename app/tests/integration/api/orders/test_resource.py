from rest_framework import status
from rest_framework.test import APITestCase

from app.models import User, Order, Pizza


class BaseAPITestCase(APITestCase):
    def authenticate_and_get_user(self):
        user = User.objects.create_user(username='cool_user', password='cool_password')
        token_key = user.get_token().key
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token_key)

        return user


class TestList(BaseAPITestCase):
    def test_when_user_is_logged_then_returns_its_orders(self):
        user = self.authenticate_and_get_user()

        pizza = Pizza.objects.create()
        Order.objects.create(
            customer=user,
            pizza=pizza,
            pizza_size=Order.THIRTY_CM_PIZZA,
            address='1st St.',
        )

        response = self.client.get('/api/orders/')

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_when_user_is_not_logged_then_returns_unauthorized_response(self):
        response = self.client.get('/api/orders/')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TestCreate(BaseAPITestCase):
    def test_when_data_is_correct_and_user_is_logged_then_returns_order_data_and_created_status(self):
        self.authenticate_and_get_user()

        pizza = Pizza.objects.create()

        post_data = {
            'pizza': pizza.id,
            'pizza_size': Order.FIFTY_CM_PIZZA,
            'address': '2nd St.',
        }

        response = self.client.post('/api/orders/', post_data)
        data = response.data

        expected_data = post_data.copy()
        expected_data['id'] = data['id']

        self.assertDictEqual(data, expected_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestUpdate(BaseAPITestCase):
    def test_when_data_is_correct_and_user_is_logged_then_returns_order_data_and_created_status(self):
        user = self.authenticate_and_get_user()

        pizza = Pizza.objects.create()
        order = Order.objects.create(
            customer=user,
            pizza=pizza,
            pizza_size=Order.FIFTY_CM_PIZZA,
            address='1st St.',
        )
        # These will be fetched again
        del order.address
        del order.pizza_size

        patch_data = {
            'pizza_size': Order.THIRTY_CM_PIZZA,
            'address': '2nd St.',
        }

        response = self.client.patch('/api/orders/{}/'.format(order.id), patch_data)

        self.assertEqual(order.address, patch_data['address'])
        self.assertEqual(order.pizza_size, patch_data['pizza_size'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
