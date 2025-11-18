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
python main.py
```

5. Run tests:
```commandline
python -m pytest
```

6. Run the application with mock data:
```bash
cd src
uvicorn main:app --reload
```

License
This project is licensed under the MIT License. See the LICENSE file for details.