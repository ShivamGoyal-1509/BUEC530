Here is a properly formatted GitHub README.md file that will display correctly in your repository:

Smart Home API - Assignment 2 (BUEC 530)

Overview

This repository contains the implementation of a RESTful API for a Smart Home System, designed as part of Assignment 2 for BUEC 530. The API allows users to manage houses, rooms, and IoT devices while focusing on:
			•	Error handling & input validation
			•	Unit testing with pytest
			•	API failure simulation
			•	GitHub Actions for CI/CD automation

Table of Contents
			•	Tech Stack
			•	Project Structure
			•	Installation & Setup
			•	API Endpoints
			•	Error Handling
			•	Running Tests
			•	GitHub Actions CI/CD
			•	Contributors

Tech Stack
			•	Python 3.8+
			•	FastAPI (for API development)
			•	Pydantic (for data validation)
			•	Uvicorn (ASGI web server)
			•	Pytest (for unit testing)
			•	GitHub Actions (for CI/CD automation)

Project Structure

		BUEC530/
		│── main.py               # Main API implementation
		│── models.py             # Data models
		│── tests/                # Unit tests
		│   ├── test_api.py
		│── requirements.txt      # Dependencies list
		│── .github/workflows/    # GitHub Actions CI/CD
		│── README.md             # API documentation

Installation & Setup

1. Clone the Repository

git clone https://github.com/ShivamGoyal-1509/BUEC530.git
cd BUEC530

2. Create & Activate a Virtual Environment

		python -m venv venv
		source venv/bin/activate  # On macOS/Linux
		venv\Scripts\activate  # On Windows

3. Install Dependencies

		pip install -r requirements.txt

4. Run the API

uvicorn main:app --reload

	•	The API will be available at http://127.0.0.1:8000
	•	Open http://127.0.0.1:8000/docs to view Swagger UI.

API Endpoints

1. User Management

		Method	Endpoint	Description
		POST	/users/register	Register a new user
		POST	/users/login	Authenticate a user
		GET	/users/{user_id}	Retrieve user details
		DELETE	/users/{user_id}	Delete a user

Example User Data

		{
  		"id": "12345",
  		"name": "John Doe",
  		"email": "johndoe@example.com",
  		"password": "hashed_password"
		}

2. House Management

		Method	Endpoint	Description
		POST	/houses	Create a new house
		GET	/houses/{house_id}	Get house details
		PUT	/houses/{house_id}	Update house details
		DELETE	/houses/{house_id}	Delete a house

Example House Data

		{
		  "id": "house123",
		  "name": "My Smart Home",
		  "address": "123 Main St",
		  "owner_id": "12345"
		}

3. Room Management

		Method	Endpoint	Description
		POST	/houses/{house_id}/rooms	Add a room to a house
		GET	/houses/{house_id}/rooms/{room_id}	Get room details
		PUT	/houses/{house_id}/rooms/{room_id}	Update room info
		DELETE	/houses/{house_id}/rooms/{room_id}	Remove a room

Example Room Data

		{
		  "id": "room567",
		  "name": "Living Room",
		  "house_id": "house123"
		}

4. Device Management

		Method	Endpoint	Description
		POST	/rooms/{room_id}/devices	Add a device to a room
		GET	/rooms/{room_id}/devices/{device_id}	Get device details
		PUT	/rooms/{room_id}/devices/{device_id}	Update device settings
		DELETE	/rooms/{room_id}/devices/{device_id}	Remove a device

Example Device Data

		{
		  "id": "device987",
		  "name": "Smart Thermostat",
		  "type": "temperature_sensor",
		  "room_id": "room567",
		  "status": "ON",
		  "temperature": 22.5
		}

Error Handling

		Error Code	Description
		400	Bad Request - Invalid data provided
		401	Unauthorized - Incorrect credentials
		404	Not Found - Requested resource does not exist
		500	Internal Server Error - Unexpected issue

Running Tests

We use pytest for unit testing.
Run the tests using:

		pytest tests/
		
		Example Test (in tests/test_api.py)
		
		from fastapi.testclient import TestClient
		from main import app
		
		client = TestClient(app)
		
		def test_register_user():
		    response = client.post("/users/register", json={
		        "name": "John Doe",
		        "email": "johndoe@example.com",
		        "password": "securepass"
		    })
		    assert response.status_code == 200

GitHub Actions CI/CD

We have automated testing using GitHub Actions.

		Workflow File: .github/workflows/api.yml
		
		name: API Tests
		
		on: [push, pull_request]
		
		jobs:
		  test:
		    runs-on: ubuntu-latest
		    steps:
		      - uses: actions/checkout@v3
		      - name: Set up Python
		        uses: actions/setup-python@v3
		        with:
		          python-version: '3.10'
		      - name: Install dependencies
		        run: pip install -r requirements.txt
		      - name: Run Tests
		        run: pytest tests/

How it Works
	•	Runs automated tests on every push or pull request.
	•	Ensures code stability before merging.

Contributors

👤 Shivam Goyal
📌 GitHub: ShivamGoyal-1509

