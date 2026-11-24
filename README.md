# REST API Test Suite (Python + Pytest + Requests)

Automated REST API test suite written in Python using `pytest` and `requests` to validate CRUD endpoints, response schemas, status codes, and negative edge cases against JSONPlaceholder.

## Test Coverage
- `GET /users` and `GET /users/{id}` status codes, response time checks, and required fields
- `POST /posts`, `PUT /posts/{id}`, and `DELETE /posts/{id}` CRUD validation
- Negative tests for invalid resource IDs (`404 Not Found`) and filtering edge cases
- Reusable API client wrapper and parameterized test cases

## Run Tests
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
pytest --html=reports/api_report.html --self-contained-html
```
