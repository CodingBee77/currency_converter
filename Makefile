install: requirements.txt
	@echo "Installing dependencies..."
	pip install -r requirements.txt

run:
	@echo "Starting the application..."
	python ./main.py

test:
	@echo "Running tests..."
	python -m pytest tests/

format:
	@echo "Formatting code with isort, black, and flake8..."
	isort . && black . && flake8 .

pretty:
	@echo "Running code formatters..."
	isort . && black .