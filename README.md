# Decentro_Task
Automated tests for ReqRes API endpoints using Python and unittest, covering CRUD operations, authentication, and error handling." 

"Test cases ensure API reliability and functionality, with clear documentation for setup and execution steps." <br>

**ReqRes API Automation Tests<br>**

This repository contains automated tests for testing ReqRes API endpoints using Python and the unittest module.<br>

**Chosen Endpoints<br>**

The following endpoints from ReqRes are tested in this repository:<br>

GET /api/users: Get a list of users.

GET /api/users/{id}: Get a single user by ID.

POST /api/users: Create a new user.

PUT /api/users/{id}: Update user information by ID.

DELETE /api/users/{id}: Delete a user by ID.

POST /api/login: Login endpoint for authentication.

**Prerequisites**

Before running the tests, ensure you have the following installed:


requests library (install using pip install requests)

**Setup Instructions**

Clone the repository to your local machine:

git clone https://github.com/your-username/reqres-api-tests.git

Navigate to the project directory:

cd reqres-api-tests

Install the required Python packages:

pip install -r requirements.txt

**Test Execution**

Run the automated tests using the following command:


python reqres_tests.py

The test results will be displayed in the terminal or command prompt.

**Testing Procedures**

The automated tests cover various scenarios for interacting with the ReqRes API, including:

GET requests to retrieve user data

POST requests to create users

PUT requests to update user information

DELETE requests to delete users

Handling invalid payloads, missing fields, and non-existent resources

Authentication scenarios (login successful and unsuccessful)
