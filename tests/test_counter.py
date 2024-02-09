"""
Test Cases for Counter Web Service

Create a service that can keep a track of multiple counters
- API must be RESTful - see the status.py file. Following these guidelines, you can make assumptions about
how to call the web service and assert what it should return.
- The endpoint should be called /counters
- When creating a counter, you must specify the name in the path.
- Duplicate names must return a conflict error code.
- The service must be able to update a counter by name.
- The service must be able to read the counter
"""
from unittest import TestCase

# we need to import the unit under test - counter
from src.counters import app

# we need to import the file that contains the status codes
from src import status

class CounterTest(TestCase):
    """Create Counter tests"""
    def setUp(self):
        self.client = app.test_client()

    def test_create_a_counter(self):
        """It should create a counter"""
        client = app.test_client()
        result = client.post('/counters/test')
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)

    def test_duplicate_a_counter(self):
        """It should return an error for duplicates"""
        result = self.client.post('/counters/bar')
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        result = self.client.post('/counters/bar')
        self.assertEqual(result.status_code, status.HTTP_409_CONFLICT)
    def test_update_a_counter(self):
        """It should update a counter"""
        # Create a counter named 'update'
        create_result = self.client.post('/counters/update')
        self.assertEqual(create_result.status_code, status.HTTP_201_CREATED)

        # Set the value of counter 'update'
        get_result = self.client.get('/counters/update')
        initial_value = get_result.json['update']

        # Update the counter 'update'
        update_result = self.client.put('/counters/update')
        self.assertEqual(update_result.status_code, status.HTTP_200_OK)

        # Retrieve the updated value of the counter 'update'
        get_updated_result = self.client.get('/counters/update')
        updated_value = get_updated_result.json['update']

        # Check the counter value is +1
        self.assertEqual(updated_value, initial_value + 1)
    def test_read_counter(self):
        """It should read a counter"""
        result = self.client.post('/counters/example')
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        result = self.client.get('/counters/example')
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(result.json['example'], 0)

