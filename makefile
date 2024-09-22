# Root

## Root commit command
root-commit:
	@if [ -z "$(file_path)" ]; then echo "Error: file_path is required"; exit 1; fi
	@if [ -z "$(message)" ]; then echo "Error: message is required"; exit 1; fi
	git add $(file_path)
	git commit -m "$(message)"


# Frontend

## Frontend commit command
frontend-commit:
	@if [ -z "$(file_path)" ]; then echo "Error: file_path is required"; exit 1; fi
	@if [ -z "$(message)" ]; then echo "Error: message is required"; exit 1; fi
	git add frontend/whale-dashboard/$(file_path)
	git commit -m "$(message)"

## Frontend commit all command
frontend-commit-all:
	git add frontend/whale-dashboard/
	git commit -m "$(message)"

# Backend
backend-commit:
	@if [ -z "$(file_path)" ]; then echo "Error: file_path is required"; exit 1; fi
	@if [ -z "$(message)" ]; then echo "Error: message is required"; exit 1; fi
	git add backend/data_access/$(file_path)
	git commit -m "$(message)"

## Backend commit all command
backend-commit-all:
	git add backend/data_access
	git commit -m "$(message)"

# Pipeline