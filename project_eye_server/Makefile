# Variables
POETRY = poetry

# Commands
.PHONY: install run clean

# Set up dependencies using Poetry
install:
	@echo "Installing dependencies..."
	@$(POETRY) install

# Start the server
run: install
	@echo "Starting the server..."
	@$(POETRY) run uvicorn app.main:app --reload

# Clean up all dependencies
clean:
	@echo "Cleaning up environment..."
	@rm -rf .venv
	@rm -rf __pycache__
	@find . -name "*.pyc" -delete
