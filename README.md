# Currency Converter 💸

A Python-based currency converter application that fetches exchange rates and performs currency conversions. The project includes unit and integration tests to ensure reliability.

## Features

- Fetches real-time exchange rates using an external API.
- Supports mock data for testing and offline usage.
- Converts amounts between different currencies.
- Includes unit and integration tests using the `pytest` library.

## Project structure

src/: Contains the main application code.

tests/: Contains unit and integration tests.

main.py: Entry point for the application.

## Requirements

- Python 3.8+
- `pip` for managing dependencies

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   

2. Install dependencies:  
```commandline
pip install -r requirements.txt
```

4. Usage of the script
Run the application:
```commandline
python run_script.py
```

5. Run tests:
```commandline
python -m pytest
```

Run single test file:
```commandline
python -m pytest tests/integration/test_conversions.py::test_get_conversions
```

6. Run the application:
```bash
uvicorn src.main:app --reload
```

 
Shortcuts for development:
- Run tests with detailed output:
  ```bash
  python -m pytest -v
  ```

- Check code formatting with Black:
  ```bash
  black . && isort . && flake8 .
  ```

License
This project is licensed under the MIT License. See the LICENSE file for details.