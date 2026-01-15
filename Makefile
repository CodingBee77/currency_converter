install: requirements.txt
	@echo "Installing dependencies..."
	pip install -r requirements.txt

run:
	@echo "Starting the script..."
	python run_script.py

app:
	@echo "Starting the application..."
	uvicorn src.main:app --reload

test:
	@echo "Running tests..."
	python -m pytest tests/

format:
	@echo "Formatting code with isort, black, and flake8..."
	isort . && black . && flake8 .