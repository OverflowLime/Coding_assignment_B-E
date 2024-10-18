# JSONPlaceholder API Client

This project is a Python application that interacts with the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/).

## Prerequisites

* Python 3.12 or higher
* pip package manager

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/OverflowLime/Coding_assignment_B-E.git
   cd Coding_assignment_B-E
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. Navigate to the `src/rest_api` directory:

   ```bash
   cd src/rest_api
   ```

2. Start the Flask application:

   ```bash
   python app.py
   ```

3. Access the API at `http://127.0.0.1:5000`.

4. For detailed examples of how to interact with the API, refer to the [API examples](#api-examples) section below.

### Running Tests

1. Ensure you're in the root directory of the project.

2. Run tests using `pytest`:

   ```bash
   pytest --cov=src/rest_api tests/
   ```

3. View the test coverage report generated by `pytest-cov`.

### Checking Type Errors

1. Run `mypy` to check for type errors:

   ```bash
   mypy src/
   ```

## API examples

`curl` calls for each of the app endpoints:

1. **Get all posts**:
   ```bash
   curl -X GET http://127.0.0.1:5000/posts
   ```

2. **Get a post by ID**:
   ```bash
   curl -X GET http://127.0.0.1:5000/posts/1
   ```

3. **Create a new post**:
   ```bash
   curl -X POST http://127.0.0.1:5000/posts \
   -H "Content-Type: application/json" \
   -d '{"title": "New Post", "body": "This is the body", "userId": 1}'
   ```

4. **Get all users**:
   ```bash
   curl -X GET http://127.0.0.1:5000/users
   ```

5. **Get all comments**:
   ```bash
   curl -X GET http://127.0.0.1:5000/comments
   ```

### Test Coverage

   To create a new test coverage report use

   ```bash
   pytest --cov=src tests/
   ```

   Current coverage:
   ```bash
   ❯ pytest --cov=src tests/
   =========================================== test session starts ===========================================
   platform linux -- Python 3.12.6, pytest-8.3.3, pluggy-1.5.0
   rootdir: /home/OverflowLime/Clone/Coding_assignment_B&E
   configfile: pyproject.toml
   plugins: requests-mock-1.12.1, cov-5.0.0
   collected 12 items

   tests/test_app.py .....                                                                             [ 41%]
   tests/test_jsonPlaceHolder.py .......                                                               [100%]

   ---------- coverage: platform linux, python 3.12.6-final-0 -----------
   Name                              Stmts   Miss  Cover
   -----------------------------------------------------
   src/rest_api/__init__.py              0      0   100%
   src/rest_api/app.py                  30      2    93%
   src/rest_api/jsonPlaceHolder.py      37      5    86%
   -----------------------------------------------------
   TOTAL                                67      7    90%
   ```