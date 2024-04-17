import requests
import unittest

class TestReqResAPI(unittest.TestCase):
    base_url = 'https://reqres.in/api/users'

    def test_get_user_list(self):
        response = requests.get(self.base_url)
        self.assertEqual(response.status_code, 200)
        user_list = response.json()['data']
        self.assertTrue(len(user_list) > 0)  # Check if the user list is not empty

    def test_get_single_user(self):
        user_id = 2  # Assuming user ID 2 exists
        response = requests.get(f'{self.base_url}/{user_id}')
        self.assertEqual(response.status_code, 200)
        user_data = response.json()['data']
        self.assertEqual(user_data['id'], user_id)

    def test_create_user(self):
        user_payload = {'name': 'John Doe', 'job': 'Engineer'}
        response = requests.post(self.base_url, json=user_payload)
        self.assertIn(response.status_code, [201, 202])  # Assuming 201 or 202 for successful creation
        created_user = response.json()
        self.assertEqual(created_user['name'], user_payload['name'])
        self.assertEqual(created_user['job'], user_payload['job'])

    def test_create_user_invalid_payload(self):
        invalid_payload = {'name': 123, 'job': 'Engineer'}  # Invalid data type for 'name'
        response = requests.post(self.base_url, json=invalid_payload)
        self.assertNotEqual(response.status_code, 400)  # Expecting a status code other than 400

    def test_create_user_missing_fields(self):
        user_payload = {'name': 'John Doe'}  # Incomplete payload without 'job' field
        response = requests.post(self.base_url, json=user_payload)
        self.assertNotEqual(response.status_code, 400)  # Expecting a status code other than 400

    def test_update_user(self):
        user_id = 2  # Assuming user ID 2 exists
        updated_payload = {'name': 'Updated Name', 'job': 'Manager'}
        response = requests.put(f'{self.base_url}/{user_id}', json=updated_payload)
        self.assertEqual(response.status_code, 200)
        updated_user = response.json()
        self.assertEqual(updated_user['name'], updated_payload['name'])
        self.assertEqual(updated_user['job'], updated_payload['job'])

    def test_update_user_invalid_id(self):
        invalid_user_id = 9999  # Assuming user ID 9999 does not exist
        updated_payload = {'name': 'Updated Name', 'job': 'Manager'}
        response = requests.put(f'{self.base_url}/{invalid_user_id}', json=updated_payload)
        self.assertNotEqual(response.status_code, 404)  # Expecting a status code other than 404

    def test_update_user_invalid_payload(self):
        user_id = 2  # Assuming user ID 2 exists
        invalid_payload = {'name': 123, 'job': 'Manager'}  # Invalid data type for 'name'
        response = requests.put(f'{self.base_url}/{user_id}', json=invalid_payload)
        self.assertNotEqual(response.status_code, 400)  # Expecting a status code other than 400

    def test_update_user_missing_payload(self):
        user_id = 2  # Assuming user ID 2 exists
        response = requests.put(f'{self.base_url}/{user_id}')  # Missing payload in PUT request
        self.assertNotEqual(response.status_code, 400)  # Expecting a status code other than 400

    def test_delete_user(self):
        user_id = 9999  # Assuming user ID 9999 does not exist
        response = requests.delete(f'{self.base_url}/{user_id}')
        self.assertEqual(response.status_code, 204)  # Expecting 204 even if user doesn't exist

    def test_get_nonexistent_user(self):
        response = requests.get(f'{self.base_url}/9999')  # Assuming user ID 9999 does not exist
        self.assertEqual(response.status_code, 404)  # Expecting 404 for not found

    def test_login_successful(self):
        login_payload = {'email': 'eve.holt@reqres.in', 'password': 'cityslicka'}
        response = requests.post('https://reqres.in/api/login', data=login_payload)
        self.assertEqual(response.status_code, 200)
        login_response = response.json()
        self.assertIn('token', login_response)

    def test_login_unsuccessful(self):
        login_payload = {'email': 'peter@klaven'}
        response = requests.post('https://reqres.in/api/login', data=login_payload)
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
